'''
TODO
* dict factory
* faction filtering (right now this does not exclude tasks based on faction)
* wipe function
    - reset item qtys
    - reset task completion
    - reset faction
* all tasks should filter by faction
* get items by name (checking likeness in name and shortname)
* get tasks by completion status
'''



# python standard libraries
import sqlite3

# dependencies
import qasync

# local modules
from API_Handler import API_Handler



class DB_Handler:
    FILENAME = 'loot.db'
    def __init__(self, signals):
        self.signals = signals
        self.conn = sqlite3.connect(self.FILENAME)
        self.conn.row_factory = sqlite3.Row
        self.db = self.conn.cursor()
        self.api = API_Handler()



    def get_item_quantities(self, id: str=None, search: str = "") -> sqlite3.Row:
        if id:
            self.db.execute('SELECT itemID, itemName, ownedNFIR, ownedFIR, taskNFIR, taskFIR, needNFIR, needFIR, Item.imageDir FROM Item_Quantities INNER JOIN Item ON Item.ID=ItemID WHERE itemID=?', (id,))
        else:
            search = f'%{search}%'
            self.db.execute('SELECT itemID, itemName, ownedNFIR, ownedFIR, taskNFIR, taskFIR, needNFIR, needFIR, Item.imageDIR FROM Item_Quantities INNER JOIN Item ON Item.ID=ItemID WHERE name LIKE ? OR normalizedName LIKE ? OR shortName LIKE ?', (search, search, search))
        return self.db.fetchall()



    def set_item_quantities(self, itemID: str, ownedNFIR: int, ownedFIR: int):
        self.db.execute('UPDATE Item SET qtyNFIR=?, qtyFIR=? WHERE ID=?', (ownedNFIR, ownedFIR, itemID))
        self.conn.commit()



    def get_task(self, id: str=None, search: str="") -> sqlite3.Row:
        if id:
            self.db.execute('SELECT Task.ID, Task.name, Trader.name, completed FROM Task INNER JOIN Trader ON Trader.ID=TraderID WHERE Task.ID=?', (id,))
        else:
            search = f'%{search}%'
            self.db.execute('SELECT Task.ID, Task.name, Trader.name, completed FROM Task INNER JOIN Trader ON Trader.ID=TraderID WHERE Task.name LIKE ?', (search,))
        return self.db.fetchall()



    def set_task_completion(self, taskID: str, status: bool):
        self.db.execute('UPDATE Task SET completed=? WHERE ID=?', (status, taskID))
        self.conn.commit()



##############################################################################################################################
############################################### CREATING AND POPULATING TABLES ###############################################
##############################################################################################################################

    def create_tables(self):
        self.db.execute('CREATE TABLE IF NOT EXISTS Item (ID TEXT PRIMARY KEY, name TEXT, normalizedName TEXT, shortName TEXT, imageURL TEXT, imageDir TEXT, qtyNFIR INTEGER DEFAULT 0, qtyFIR INTEGER DEFAULT 0)')
        self.db.execute('CREATE TABLE IF NOT EXISTS Task (ID TEXT PRIMARY KEY, name TEXT, TraderID TEXT, faction INTEGER, completed INTEGER DEFAULT 0)')
        self.db.execute('CREATE TABLE IF NOT EXISTS Task_Item (ID TEXT PRIMARY KEY, TaskID TEXT, ItemID TEXT, qty INTEGER, quality TEXT, fir INTEGER)')
        self.db.execute('CREATE TABLE IF NOT EXISTS Trader (ID TEXT PRIMARY KEY, name TEXT)')
        self.db.execute('CREATE TABLE IF NOT EXISTS Faction (ID INTEGER PRIMARY KEY, name TEXT)')
        self.conn.commit()


    def create_views(self):
        self.db.execute('''
        CREATE VIEW IF NOT EXISTS Item_Quantities (
            itemID,
            itemName,
            ownedNFIR,
            ownedFIR,
            taskNFIR,
            taskFIR,
            needNFIR,
            needFIR
        )
        AS
            SELECT
                item.ID,
                item.Name,
                item.qtyNFIR,
                item.qtyFIR,
                SUM(CASE WHEN Task_Item.fir=0 THEN Task_Item.qty ELSE 0 END),
                SUM(CASE WHEN Task_Item.fir=1 THEN Task_Item.qty ELSE 0 END),
                (SUM(CASE WHEN Task_Item.fir=0 THEN Task_Item.qty ELSE 0 END) - item.qtyNFIR),
                (SUM(CASE WHEN Task_Item.fir=1 THEN Task_Item.qty ELSE 0 END) - item.qtyFIR)
            FROM Item
            INNER JOIN Task_Item ON Item.ID=ItemID
            INNER JOIN Task ON Task.ID=TaskID
            WHERE Task.completed=0
            GROUP BY item.ID''')
        self.conn.commit()



    @qasync.asyncSlot()
    async def initialize_tables(self):
        '''
        Initializes the tables with all the data they need.
        '''
        all_data = self.api.get_everything()
        await self.populate_faction_table()
        await self.populate_trader_table(all_data['traders'])
        await self.populate_item_table(all_data['items'])
        await self.populate_task_table(all_data['tasks'], all_data['hideoutStations'])



    @qasync.asyncSlot()
    async def update_tables(self):
        '''
        Updates tables with any new data. Works by pulling data from api.tarkov.dev, trusting it completely, and rewriting all records.
        Faction should not be changed at all
        Trader and Task_Item should be rewritten completely
        Item and Task should be UPSERT'ed (see note)

        Note:
            Does not effect Item.imageDir, Item.qtyNFIR, Item.qtyFIR, and Task.completed attributes.
        '''
        all_data = self.api.get_everything()
        self.signals.set_progress_max_signal.emit(sum(len(x) for x in all_data.values()))
        self.db.execute('DELETE FROM Task_Item')
        self.db.execute('DELETE FROM Trader')
        await self.initialize_tables()



    @qasync.asyncSlot()
    async def update_images(self):
        '''
        COMPLETELY downloads new images from api.tarkov.dev. Since we won't know if there are new images, we just have to download them all.
        This process can take up to 5 minutes.
        '''
        self.db.execute('SELECT name, imageURL, imageDir FROM Item')
        data = self.db.fetchall()
        self.signals.set_progress_max_signal.emit(len(data))
        for count, item in enumerate(data):
            self.signals.update_progress_signal.emit()
            self.signals.append_log_signal.emit(f'downloading item {count}/{len(data)}: {item["name"]}')
            # print(f'downloading image {count} / {len(urls)}')
            await self.api.download_image(item['imageURL'], item['imageDir'])



    @qasync.asyncSlot()
    async def populate_faction_table(self):
        self.db.execute('INSERT OR IGNORE INTO Faction VALUES(0, "Any")')
        self.db.execute('INSERT OR IGNORE INTO Faction VALUES(1, "BEAR")')
        self.db.execute('INSERT OR IGNORE INTO Faction VALUES(2, "USEC")')
        self.db.execute('INSERT OR IGNORE INTO Faction VALUES(3, "Scav")')
        self.conn.commit()



    @qasync.asyncSlot()
    async def populate_trader_table(self, data):
        data
        self.db.execute('INSERT OR IGNORE INTO Trader VALUES ("0", "Hideout")')
        for count, trader in enumerate(data):
            self.signals.update_progress_signal.emit()
            self.signals.append_log_signal.emit(f'working on trader #{count}/{len(data)}: {trader["name"]}')
            self.db.execute('INSERT OR IGNORE INTO Trader VALUES (?, ?)', (trader['id'], trader['name']))
        self.conn.commit()



    @qasync.asyncSlot()
    async def populate_item_table(self, data):
        for count, item in enumerate(data):
            # print(f'working on item {count} / {len(data)}')
            self.signals.update_progress_signal.emit()
            self.signals.append_log_signal.emit(f'working on item #{count}/{len(data)}: {item["name"]}')
            filename = f'images/{item["id"]}{item["iconLink"][item["iconLink"].rfind("."):]}'
            self.db.execute('''INSERT INTO Item VALUES (?, ?, ?, ?, ?, ?, 0, 0)
                                ON CONFLICT(ID) DO UPDATE SET name=?, normalizedName=?, shortName=?, imageURL=?''',
                                (item['id'], item['name'], item['normalizedName'], item['shortName'], item['iconLink'], filename,
                                item['name'], item['normalizedName'], item['shortName'], item['iconLink']))
        self.conn.commit()



    @qasync.asyncSlot()
    async def populate_task_table(self, task_data, hideout_data):
        # Task table and Task_Item table
        for count, task in enumerate(task_data):
            self.signals.update_progress_signal.emit()
            self.signals.append_log_signal.emit(f'working on task #{count}/{len(task_data)}: {task["name"]}')
            if collect_objs := [x for x in task['objectives'] if x and x['type'] == 'giveItem']:
                factions = {
                    'Any': 0,
                    'BEAR': 1,
                    'USEC': 2,
                    'Scav': 3
                }
                # Task Table
                self.db.execute('''INSERT INTO Task VALUES (?, ?, ?, ?, 0)
                                    ON CONFLICT(ID) DO UPDATE SET name=?, TraderID=?, faction=?''',
                                    (task['id'], task['name'], task['trader']['id'], factions[task['factionName']],
                                    task['name'], task['trader']['id'], factions[task['factionName']]))

                # Task_Item Table
                for obj in collect_objs:
                    # quality is determined by dogtag levels or the durability of equipment and should be turned into text form
                    # if there doesn't need to be anything, this should just be null
                    # BEAR dogtag: 59f32bb586f774757e1e8442
                    # USEC dogtag: 59f32c3b86f77472a31742f0
                    quality = None
                    if 'wearable' in obj['item']['types']:
                        quality = f'{obj["minDurability"]}% - {obj["maxDurability"]}%'
                    elif obj['item']['id'] in ['59f32bb586f774757e1e8442', '59f32c3b86f77472a31742f0']: # dogtags
                        quality = f'lv {obj["dogTagLevel"]}+'
                    self.db.execute('INSERT INTO Task_Item VALUES (?, ?, ?, ?, ?, ?)', (obj['id'], task['id'], obj['item']['id'], obj['count'], quality, obj['foundInRaid']))
        self.conn.commit()

        # Task table and Task_Item table extended for hideout
        for count, station in enumerate(hideout_data):
            self.signals.update_progress_signal.emit()
            self.signals.append_log_signal.emit(f'working on hideout #{count}/{len(hideout_data)}: {task["name"]}')
            for lv in station['levels']:
                if lv['itemRequirements']:
                    # Task Table
                    self.db.execute(f'''INSERT INTO Task VALUES (?, ?, "0", 0, 0)
                                        ON CONFLICT(ID) DO UPDATE SET name=?''',
                                        (lv['id'], f'{station["name"]} Level {lv["level"]}',
                                        f'{station["name"]} Level {lv["level"]}'))

                    # Task_Item Table
                    for req in lv['itemRequirements']:
                        self.db.execute('INSERT INTO Task_Item VALUES (?, ?, ?, ?, ?, ?)', (req['id'], lv['id'], req['item']['id'], req['count'], None, False))
        self.conn.commit()