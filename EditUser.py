from edit_user import Ui_Dialog
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QDialog,
)
from PySide6.QtCore import Qt
from db import DataBase


class EditUser(QDialog):
    def __init__(self, table, db, select, fun):
        super().__init__()
        self.database = db
        self.selected_items = select
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Setup the UI for 'self'
        self.table = table
        self.fun = fun
        self.ui.toolButton_confirm.clicked.connect(
            self.update_user
        )  # Connect confirm button to accept method
        self.ui.toolButton_cancel.clicked.connect(self.close)
        self.edit()

    def edit(self):
        row = self.table.row(self.selected_items[0])
        username_item = self.table.item(
            row, 2
        )  # Assuming username is in column index 2
        if username_item is not None:
            username = username_item.text()
            user_info = self.database.fetch_user(username)
            if user_info:
                self.populate_form(user_info)
            else:
                QMessageBox.warning(
                    self, "Error", "User information could not be fetched."
                )

    def populate_form(self, user_info):
        self.ui.lineEdit_usersname.setText(user_info["first_name"])
        self.ui.lineEdit_userslastname.setText(user_info["last_name"])
        self.ui.lineEdit_username.setText(user_info["username"])
        self.ui.lineEdit_password.setText(user_info["password"])
        self.ui.checkBox_model.setChecked(user_info["pmodel"])
        self.ui.checkBox_user.setChecked(user_info["puser"])
        self.ui.checkBox_gozaresh.setChecked(user_info["pgozaresh"])
        self.ui.checkBox_tolid.setChecked(user_info["ptoolid"])
        self.ui.checkBox_db.setChecked(user_info["pdb"])

    def an(self):
        self.close()

    def update_user(self):
        self.close()
        user_info = {
            "first_name": self.ui.lineEdit_usersname.text(),
            "last_name": self.ui.lineEdit_userslastname.text(),
            "username": self.ui.lineEdit_username.text(),
            "password": self.ui.lineEdit_password.text(),
            "pmodel": self.ui.checkBox_model.isChecked(),
            "puser": self.ui.checkBox_user.isChecked(),
            "pgozaresh": self.ui.checkBox_gozaresh.isChecked(),
            "ptoolid": self.ui.checkBox_tolid.isChecked(),
            "pdb": self.ui.checkBox_db.isChecked(),
        }
        self.database.update_user(user_info)
        QMessageBox.information(self, "ویرایش", "ویرایش کاربر با موفقیت انجام شد")
        self.fun()
        self.accept()
