from add_user import Ui_Dialog
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
class AddUser(object):
    def __init__(self,dialog):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(dialog)
