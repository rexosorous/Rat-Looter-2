# dependencies
from PyQt5.QtWidgets import QWidget
import qasync

# local modules
from ui.update_widget import Ui_Form



class UpdateView(QWidget, Ui_Form):
    """The update screen

    Args:
        db (DB_Handler.DB_Handler)
        signals (signals.Signals)

    Attributes:
        progressBar (QProgressBar)
        log (QTextBrowser)
    """
    def __init__(self, db, signals):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.signals = signals
        self.connect_events()



    def connect_events(self):
        self.signals.set_progress_max_signal.connect(self.set_progress_max)
        self.signals.update_progress_signal.connect(self.update_progress)
        self.signals.append_log_signal.connect(self.append_log)



    def set_progress_max(self, value: int):
        self.progressBar.setMaximum(value)



    def update_progress(self):
        self.progressBar.setValue(self.progressBar.value()+1)



    def append_log(self, msg: str):
        self.log.append(msg)



    def clear(self):
        self.progressBar.setValue(0)
        self.log.clear()