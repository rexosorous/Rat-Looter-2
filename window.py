# dependencies
from PyQt5.QtWidgets import QMainWindow
import qasync

# local modules
from DB_Handler import DB_Handler
from ui.home_window import Ui_MainWindow
from main_view import MainView
from update_view import UpdateView
from signals import Signals


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signals = Signals()
        self.db = DB_Handler(self.signals)

        self.main_view = MainView(self.db)
        self.mainLayout.addWidget(self.main_view)

        self.update_view = UpdateView(self.db, self.signals)
        self.update_view.setHidden(True)
        self.mainLayout.addWidget(self.update_view)

        self.connect_events()



    def connect_events(self):
        self.updateDatabaseButton.triggered.connect(self.update_database)
        self.updateItemImagesButton.triggered.connect(self.update_images)
        self.wipeButton.triggered.connect(self.wipe)
        self.update_view.closeButton.released.connect(self.show_main_view)



    def show_main_view(self):
        self.update_view.setHidden(True)
        self.main_view.setHidden(False)



    def show_update_view(self):
        self.update_view.clear()
        self.update_view.closeButton.setVisible(False)
        self.main_view.setHidden(True)
        self.update_view.setHidden(False)


    @qasync.asyncSlot()
    async def update_database(self):
        self.show_update_view()
        self.update_view.label.setText('Updating Database')
        await self.db.update_tables()
        self.update_view.closeButton.setVisible(True)




    @qasync.asyncSlot()
    async def update_images(self):
        self.show_update_view()
        self.update_view.label.setText('Updating Images')
        await self.db.update_images()
        self.update_view.closeButton.setVisible(True)




    @qasync.asyncSlot()
    async def wipe(self):
        self.db.wipe()