# dependencies
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QMessageBox, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# local modules
from ui.home_widget import Ui_Form



class MainView(QWidget, Ui_Form):
    """The main screen

    Args:
        db (DB_Handler)

    Attributes:
        itemSearchbar (QLineEdit)
        itemList (QListWidget)
        itemImage (QLabel)
        itemName (QTextBrowser)
        itemNeedFIR (QSpinBox)
        itemNeedNFIR (QSpinBox)
        itemTaskFIR (QSpinBox)
        itemTaskNFIR (QSpinBox)
        itemOwnedFIR (QSpinBox)
        itemOwnedNFIR (QSpinBox)
        itemSubmitButton (QPushButton)

        taskSearchbar (QLineEdit)
        taskTable (QTableWidget)
        taskName (QLineEdit)
        taskGiver (QLineEdit)
        taskCompleted (QCheckBox)
        taskSubmitButton (QPushButton)
    """
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.connect_events()
        self.db = db
        self.populate_tables()

        self.itemImage.setPixmap(QPixmap('images/unknown-item-icon.jpg'))
        self.selected_item = None   # QListWdidgetItem
        self.selected_task = None   # QTableWidgetItem



    def connect_events(self):
        self.itemSearchbar.returnPressed.connect(self.item_search)
        self.itemList.itemClicked.connect(self.item_select)
        self.itemSubmitButton.released.connect(self.item_submit)

        self.taskSearchbar.returnPressed.connect(self.task_search)
        self.taskTable.itemClicked.connect(self.task_select)
        self.taskSubmitButton.released.connect(self.task_submit)



    def populate_tables(self, data=None):
        if not data:
            data = self.db.get_task()
        for row, task in enumerate(data):
            self.taskTable.insertRow(row)
            self.taskTable.setItem(row, 0, QTableWidgetItem(task[0]))
            self.taskTable.setItem(row, 1, QTableWidgetItem(task[1]))
            self.taskTable.setItem(row, 2, QTableWidgetItem(task[2]))
            self.taskTable.setItem(row, 3, QTableWidgetItem("Yes" if task[3] else "No"))
        self.taskTable.hideColumn(0)
        self.taskTable.verticalHeader().setVisible(False)
        self.taskTable.resizeColumnsToContents()



##############################################################################################################################
###################################################### DROPDOWN SECTION ######################################################
##############################################################################################################################

    def update_database_confirm(self):
        popup = QMessageBox()
        popup.setWindowTitle('Updating Database')
        popup.setIcon(QMessageBox.Question)
        popup.setText('This process may take a few minutes, during which you will not be able to stop or use this program.\n\nAre you ready?')
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        popup.buttonClicked.connect(self.update_database)
        run = popup.exec_()


    def update_database(self, button):
        if button.text() != '&Yes':
            return
        popup = QMessageBox()
        popup.setWindowModality(Qt.ApplicationModal)
        popup.setWindowTitle('Updating Database')
        layout = popup.layout()
        progress_bar = QProgressBar()
        progress_bar.setMaximum(4)
        layout.addWidget(progress_bar)
        popup.setText('Please Don\'t Press the "Ok" button or exit this window.')

        run = popup.exec_()



##############################################################################################################################
######################################################## ITEM SECTION ########################################################
##############################################################################################################################

    def item_search(self):
        self.itemList.clear()
        search = self.itemSearchbar.text()
        data = self.db.get_item_quantities(search=search)
        for item in data:
            list_item = QListWidgetItem(item['itemName'])
            list_item.setData(1, item['itemID'])
            self.itemList.addItem(list_item)
        if len(data) == 1:
            self.itemList.setCurrentItem(self.itemList.item(0))
            self.item_select(self.itemList.item(0))



    def item_select(self, item: QListWidgetItem):
        data = self.db.get_item_quantities(id=item.data(1))[0]
        self.itemImage.setPixmap(QPixmap(data['imageDir']))
        self.itemName.setText(data['itemName'])
        self.itemTaskFIR.setValue(data['taskFIR'])
        self.itemTaskNFIR.setValue(data['taskNFIR'])
        self.itemOwnedFIR.setValue(data['ownedFIR'])
        self.itemOwnedNFIR.setValue(data['ownedNFIR'])

        self.itemNeedFIR.setValue(data['needFIR'])
        self.itemNeedNFIR.setValue(data['needNFIR'] if data['needFIR'] >= 0 else data['needNFIR']+data['needFIR'])
        self.selected_item = item



    def item_submit(self):
        fir = self.itemOwnedFIR.value()
        nfir = self.itemOwnedNFIR.value()
        self.db.set_item_quantities(self.selected_item.data(1), nfir, fir)
        self.item_select(self.selected_item)



##############################################################################################################################
######################################################## TASK SECTION ########################################################
##############################################################################################################################

    def task_search(self):
        self.taskTable.setRowCount(0)
        data = self.db.get_task(search=self.taskSearchbar.text())
        self.populate_tables(data)



    def task_select(self, item: QTableWidgetItem):
        id_table_item = self.taskTable.item(item.row(), 0)
        id = id_table_item.data(0)
        task_data = self.db.get_task(id=id)[0]
        self.taskName.setText(task_data[1])
        self.taskGiver.setText(task_data[2])
        self.taskCompleted.setChecked(True if task_data[3] else False)
        self.selected_task = id_table_item



    def task_submit(self):
        self.db.set_task_completion(self.selected_task.data(0), self.taskCompleted.isChecked())
        self.taskTable.item(self.selected_task.row(), 3).setText("Yes" if self.taskCompleted.isChecked() else "No")