import sys
import sqlite3
import shutil
import os
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFileDialog,
    QMainWindow,
    QTableWidgetItem,
)
from datetime import datetime
import jdatetime


# from ui_main import Ui_MainWindow
class Report:
    def __init__(self, db, ui):
        self.database = db
        self.ui = ui

    def print_action(self, user):

        self.current_user = user
        rows = self.database.get_user_action(self.current_user)
        self.ui.tableWidget_history.setRowCount(0)
        all_data = self.database.fetch_one(self.current_user)
        # print(rows)
        checkbox_texts = [
            "تغییر مدل",
            "مدیریت کاربران",
            "گزارش گیری",
            "تولید جعبه",
            "مدیریت دیتابیس",
        ]
        permissions_text = []
        # Iterate over rows to populate table
        # for  row_data in enumerate(all_data):
        for col_idx in range(4, 9):  # Assuming permissions are in columns 4 to 8
            if all_data[col_idx] == 1:
                permission_index = (
                    col_idx - 4
                )  # Calculate corresponding index in checkbox_texts
                if permission_index < len(checkbox_texts):
                    permissions_text.append(checkbox_texts[permission_index])
            #     pass
            # print(all_data)

            # Create text from permissions_text list
        permissions_str = " , ".join(permissions_text)
        self.ui.label_acclastname.setText(all_data[1])
        self.ui.label_accname.setText(all_data[0])
        self.ui.label_accusername.setText(all_data[3])
        self.ui.label_accperm.setText(permissions_str)
        # self.ui.tableWidget_history.setColumnCount(3)
        self.ui.tableWidget_history.setColumnWidth(0, 110)
        self.ui.tableWidget_history.setColumnWidth(1, 110)
        self.ui.tableWidget_history.setColumnWidth(2, 1510)
        # self.ui.tableWidget_history.setHorizontalHeaderLabels(
        #     [ "تاریخ", "ساعت", "فعالیت"]
        # )
        for num_row, (date, time, action) in enumerate(rows):
            self.ui.tableWidget_history.setRowCount(
                self.ui.tableWidget_history.rowCount() + 1
            )
            self.ui.tableWidget_history.setRowHeight(num_row,20)
            self.ui.tableWidget_history.setItem(num_row, 0, QTableWidgetItem(self.date_convertor(date)))
            self.ui.tableWidget_history.setItem(num_row, 1, QTableWidgetItem(time))
            self.ui.tableWidget_history.setItem(num_row, 2, QTableWidgetItem(action))

    def report_barcode(self):
        try:
            rows = self.database.get_barcode_scan()
            self.ui.tableWidget_report_barcode.setColumnCount(4)
            self.ui.tableWidget_report_barcode.setHorizontalHeaderLabels(
                ["نام کاربری", "تاریخ", "ساعت", "بارکد"]
            )
            self.ui.tableWidget_report_barcode.setColumnWidth(0, 110)
            self.ui.tableWidget_report_barcode.setColumnWidth(1, 110)
            self.ui.tableWidget_report_barcode.setColumnWidth(2, 110)
            self.ui.tableWidget_report_barcode.setColumnWidth(3, 1550)
            self.ui.tableWidget_report_barcode.setRowCount(0)
            for num_row, (username, date, time, barcode) in enumerate(rows):
                self.ui.tableWidget_report_barcode.setRowCount(
                    self.ui.tableWidget_report_barcode.rowCount() + 1
                )
                self.ui.tableWidget_report_barcode.setItem(
                    num_row, 0, QTableWidgetItem(username)
                )
                self.ui.tableWidget_report_barcode.setItem(
                    num_row, 1, QTableWidgetItem(self.date_convertor(date))
                )
                self.ui.tableWidget_report_barcode.setItem(
                    num_row, 2, QTableWidgetItem(time)
                )
                self.ui.tableWidget_report_barcode.setItem(
                    num_row, 3, QTableWidgetItem(barcode)
                )
        except Exception as e:
            self.error_handler(f"Error report barcode: {e}")

    def date_convertor(self, date):
        # Example Gregorian date as string
        gregorian_date_str = date

        # Parse Gregorian date string to datetime object
        gregorian_date = datetime.strptime(gregorian_date_str, "%Y/%m/%d").date()

        # Convert Gregorian date to Persian date
        persian_date = jdatetime.date.fromgregorian(date=gregorian_date)

        # Get year, month, day from Persian date
        year = persian_date.year
        month = persian_date.month
        day = persian_date.day
        return f"{year}/{month}/{day}"

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
