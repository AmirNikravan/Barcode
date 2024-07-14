from add_user import Ui_Dialog
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QDialog,
)
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from db import DataBase


class AddUser(QDialog):
    def __init__(self, table, db):
        self.database = db
        super().__init__()
        self.table = table
        self.ui = Ui_Dialog()
        self.inform = []
        self.checkbox_texts = []
        self.status_add = int
        self.ui.setupUi(self)
        self.ui.toolButton_confirm.clicked.connect(self.adduser)
        self.ui.toolButton_cancel.clicked.connect(self.close)

    def adduser(self):
        try:
            self.inform.append(self.ui.lineEdit_usersname.text())
            self.inform.append(self.ui.lineEdit_userslastname.text())
            self.inform.append(self.ui.lineEdit_username.text())
            self.inform.append(self.ui.lineEdit_password.text())
            self.inform.append(self.ui.checkBox_model.isChecked())
            self.inform.append(self.ui.checkBox_user.isChecked())
            self.inform.append(self.ui.checkBox_gozaresh.isChecked())
            self.inform.append(self.ui.checkBox_tolid.isChecked())
            self.inform.append(self.ui.checkBox_db.isChecked())
            self.checkbox_texts = [
                self.ui.checkBox_model.text(),
                self.ui.checkBox_user.text(),
                self.ui.checkBox_gozaresh.text(),
                self.ui.checkBox_tolid.text(),
                self.ui.checkBox_db.text(),
            ]
            checkbox_states = self.inform[-5:]
            checked_texts = [
                self.checkbox_texts[i]
                for i in range(len(checkbox_states))
                if checkbox_states[i]
            ]
            self.status_add = self.database.add_user(self.inform)
            if self.status_add == 1:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                items = [
                    self.inform[0],
                    self.inform[1],
                    self.inform[2],
                    self.inform[3],
                    ", ".join(checked_texts),
                ]

                for col, item in enumerate(items):
                    self.table.setItem(row_position, col, QTableWidgetItem(item))
                QMessageBox.information(self, "اضافه", "کاربر جدید با موقیت ساخته شد")
            self.accept()
        except Exception as e:
            self.error_handler(f"Error add user: {e}")
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
            msg_box2.setText(f"error handler adduser:{msg}")
            msg_box2.exec()
