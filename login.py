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
        try:
            self.username = self.ui.lineEdit_username.text()
            self.password = self.ui.lineEdit_pass.text()
            if self.database.login(self.username, self.password):
                self.accept()
            else:
                QMessageBox.critical(self, "خطا", "نام کاربری یا رمز عبور اشتباه است.")
                self.ui.lineEdit_username.clear()
                self.ui.lineEdit_pass.clear()
                self.ui.lineEdit_username.setFocus()
        except Exception as e:
            self.error_handler(f"Error login validation: {e}")
    def detail(self):
        try:
            self.database.cursor.execute(
                "SELECT first_name , last_name ,username FROM user WHERE username=? AND password=?",
                (self.username, self.password),
            )
            detail = self.database.cursor.fetchone()
            return detail
        except Exception as e:
            self.error_handler(f"Error Login detail: {e}")
    def error_handler(self, msg):
        try:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(msg)
            msg_box.exec()
        except Exception as e:
            msg_box2 = QMessageBox(self)
            msg_box2.setIcon(QMessageBox.Critical)
            msg_box2.setWindowTitle("Error")
            msg_box2.setText(f"error handler :{msg}")
            msg_box2.exec()
