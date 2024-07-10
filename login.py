from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_login import *


class Login(QDialog):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toolButton_enter.clicked.connect(self.validation)
        self.ui.toolButton_cancel.clicked.connect(self.close)
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.validation)

    def validation(self):
        self.username = self.ui.lineEdit_username.text()
        self.password = self.ui.lineEdit_pass.text()
        if self.database.login(self.username, self.password):
            self.accept()
        else:
            QMessageBox.critical(self, "خطا", "نام کاربری یا رمز عبور اشتباه است.")
            self.ui.lineEdit_username.clear()
            self.ui.lineEdit_pass.clear()
            self.ui.lineEdit_username.setFocus()

    def detail(self):
        self.database.cursor.execute(
            "SELECT first_name , last_name ,username FROM user WHERE username=? AND password=?",
            (self.username, self.password),
        )
        detail = self.database.cursor.fetchone()
        return detail
