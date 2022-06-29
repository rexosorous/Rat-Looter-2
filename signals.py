# dependencies
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject



class Signals(QObject):
    """Holds all the signals to be emitted and connected.

    Note:
        These signals must be class attributes and an instance of this class must be created for the signals to work
    """
    set_progress_max_signal = pyqtSignal(int)
    update_progress_signal = pyqtSignal()
    append_log_signal = pyqtSignal(str)