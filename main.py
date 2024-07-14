from PySide6.QtWidgets import *
import traceback
import sys, os
from PIL import Image
import barcode.base
import barcode.itf
from ui_main import Ui_MainWindow
from barcode import Code128
from barcode.writer import SVGWriter, ImageWriter
from PySide6 import QtGui, QtPrintSupport, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
import svgwrite
import barcode
import re
import qrcode
from directory import Directory
import qrcode
import qrcode.image.svg
import svg_stack as ss
from lxml import etree
import svgwrite
from AddUser import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from db import DataBase
from EditUser import EditUser
import jdatetime
from login import *

import datetime


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.barcodes = []
        super().__init__(parent)
        self.ui = Ui_MainWindow()

        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(self.handlePrint)
        self.ui.setupUi(self)
        self.database = DataBase(self.ui.tableWidget_excel)
        self.current_user = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)  # Update every second
        self.setWindowTitle("IMEI SCANNER")
        self.update_labels()
        self.box = 1
        # signals
        self.ui.toolButton_navigscan.clicked.connect(lambda: self.navigation("scan"))
        self.ui.toolButton_naviguser.clicked.connect(lambda: self.navigation("user"))
        self.ui.toolButton_navigreport.clicked.connect(
            lambda: self.navigation("report")
        )
        self.ui.toolButton_navigaccount.clicked.connect(
            lambda: self.navigation("account")
        )
        self.ui.toolButton_navigdatabase.clicked.connect(
            lambda: self.navigation("database")
        )
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.toolButton_print.clicked.connect(self.handlePrint)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
        self.ui.pushButton_clear.clicked.connect(self.clear_table)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.toolButton_deleterow.clicked.connect(self.delete_selected_rows)
        self.ui.toolButton_newuser.clicked.connect(self.adduser)
        self.ui.toolButton_deleteuser.clicked.connect(self.delete_selected_rows2)
        self.ui.toolButton_edituser.clicked.connect(self.edituser)
        self.ui.toolButton_exportdb.clicked.connect(lambda: self.dbhandel("exportdb"))
        self.ui.toolButton_inputdb.clicked.connect(lambda: self.dbhandel("importdb"))
        self.ui.toolButton_exit.clicked.connect(self.logout)
        self.ui.tableWidget_list_users.itemSelectionChanged.connect(
            self.on_table_item_selection_changed
        )
        self.ui.toolButton_inputexcel.clicked.connect(self.importexcel)
        self.ui.toolButton_dbcheck.clicked.connect(self.validation)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.changeRowColor)
        # table config
        self.ui.tableWidget.setColumnWidth(0, 180)
        self.ui.tableWidget.setColumnWidth(1, 400)
        self.ui.tableWidget.setColumnWidth(2, 180)
        self.ui.tableWidget.setColumnWidth(3, 250)
        self.ui.tableWidget_list_users.setColumnWidth(4, 800)
        self.ui.tableWidget_history.setColumnWidth(1, 1400)
        for col in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setSortingEnabled(False)

        self.ui.tableWidget_list_users.setStyleSheet(
            """
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #d0d0d0;
            }
            QTableWidget::item:selected {
                background-color: #b3d9ff; /* Light blue */
            }
        """
        )
        self.ui.tableWidget_excel.setColumnWidth(0, 220)
        self.ui.tableWidget_excel.setColumnWidth(1, 220)
        # lineeidt config

        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setMaxLength(15)
        # total barcodes
        self.total = 0
        # directory config
        self.dir = Directory()
        self.scan_timer = QTimer(self)
        self.scan_timer.setSingleShot(True)
        self.scan_timer.timeout.connect(self.enable_scanning)
        # self.handellogin()
        self.handlecombo()
        # self.show_table()
        self.validation()

    def show_main_window(self):
        try:
            self.show()
        except Exception as e:
            self.error_handler(f"Error show main window: {e}")

    def format_number(self, n, width=7):
        try:
            return f"{n:0{width}}"
        except Exception as e:
            self.error_handler(f"Error format number: {e}")

    def logout(self):
        try:
            action = "کاربر خارج شد"
            self.database.action(
                self.current_user, f"{self.date_text}-{self.time_text}", action
            )
            self.current_user = None  # Clear current user session
            # Additional actions to reset UI or return to login state if necessary
            # For example, hide user-specific UI elements, disable certain actions

            # Optionally, show the login dialog again after logout
            self.handellogin()
        except Exception as e:
            self.error_handler(f"Error LOGOUT: {e}")

    def handelpermissions(self):
        try:
            self.permissions = self.database.permission(self.current_user)
            if self.permissions["model"] == 0:
                self.ui.comboBox_model.setEnabled(False)
                self.ui.comboBox_color.setEnabled(False)
                self.ui.comboBox_sku.setEnabled(False)
            else:
                self.ui.comboBox_color.setEnabled(True)
                self.ui.comboBox_sku.setEnabled(True)
                self.ui.comboBox_model.setEnabled(True)
            if self.permissions["user"] == 0:
                self.ui.toolButton_naviguser.setEnabled(False)
            else:
                self.ui.toolButton_naviguser.setEnabled(True)
            if self.permissions["report"] == 0:
                self.ui.toolButton_navigreport.setEnabled(False)
            else:
                self.ui.toolButton_navigreport.setEnabled(True)
            if self.permissions["toolid"] == 0:
                self.ui.toolButton_navigbox.setEnabled(False)
            else:
                self.ui.toolButton_navigbox.setEnabled(True)
            if self.permissions["db"] == 0:
                self.ui.toolButton_navigdatabase.setEnabled(False)
            else:
                self.ui.toolButton_navigdatabase.setEnabled(True)
        except Exception as e:
            self.error_handler(f"Error fetching user: {e}")

    def handellogin(self):
        try:
            dialog = Login(self.database)
            if dialog.exec() == QDialog.Accepted:
                self.show_main_window()
                self.detail = dialog.detail()
                self.current_user = self.detail[2]
                self.ui.label_name.setText(f"{self.detail[0]} {self.detail[1]}")
                # self.permissions = self.database.permission(detail[2])
                self.handelpermissions()
                action = "کاربر وارد سیستم شد"
                self.database.action(
                    self.current_user, f"{self.date_text}-{self.time_text}", action
                )
                self.print_action()
                self.ui.stackedWidget.setCurrentIndex(0)
                QMessageBox.information(
                    self, "ورود", f"کاربر {self.detail[0]} {self.detail[1]} خوش آمدید."
                )

            else:
                # print('Login failed')
                sys.exit(0)
                # return
        except Exception as e:
            self.error_handler(f"Error handellogin: {e}")

    def update_labels(self):
        try:
            current_date = jdatetime.date.today()
            current_time = QTime.currentTime()
            # locale = QLocale(QLocale.Persian, QLocale.Iran)

            self.date_text = jdatetime.date.today()
            self.date_text = current_date.strftime("%Y/%m/%d")
            self.time_text = current_time.toString("hh:mm:ss A")
            day_names = [
                "شنبه",
                "یکشنبه",
                "دوشنبه",
                "سه شنبه",
                "چهارشنبه",
                "پنجشنبه",
                "جمعه",
            ]
            day_text = day_names[current_date.weekday()]

            self.ui.label_time.setText(self.time_text)
            self.ui.label_date.setText(self.date_text)
            self.ui.label_day.setText(day_text)
        except Exception as e:
            self.error_handler(f"Error upadte labels: {e}")

    def importexcel(self):
        try:
            self.database.importexcel()
        except Exception as e:
            self.error_handler(f"Erro main importexcel: {e}")

    def dbhandel(self, result):
        try:
            if result == "exportdb":
                self.database.exportdb()
            if result == "importdb":
                self.database.importdb()
        except Exception as e:
            self.error_handler(f"Error dbhandel: {e}")

    def on_table_item_selection_changed(self):
        try:
            selected_items = self.ui.tableWidget_list_users.selectedItems()

            # Clear previous selection
            self.clear_previous_selection()

            # Apply selection style to the entire selected row
            for item in selected_items:
                row = item.row()
                col = item.column()
                self.apply_selection_style(row, col)
        except Exception as e:
            self.error_handler(f"Error on table selection changed: {e}")

    def clear_previous_selection(self):
        try:
            for row in range(self.ui.tableWidget_list_users.rowCount()):
                for col in range(self.ui.tableWidget_list_users.columnCount()):
                    item = self.ui.tableWidget_list_users.item(row, col)
                    if item:
                        item.setBackground(
                            QColor("white")
                        )  # Change to your default background color
        except Exception as e:
            self.error_handler(f"Error clear previous selection: {e}")

    def apply_selection_style(self, row, col):
        try:
            for c in range(self.ui.tableWidget_list_users.columnCount()):
                item = self.ui.tableWidget_list_users.item(row, c)
                if item:
                    item.setBackground(QColor("#b3d9ff"))
        except Exception as e:
            self.error_handler(f"Error apply selection style: {e}")
    def show_table(self):
        if self.validation() == False:
            return
        rows = self.database.fetch_all()
        if not rows:
            return

        # Clear existing table contents
        self.ui.tableWidget_list_users.clearContents()

        # Set the number of rows and columns in the table widget
        self.ui.tableWidget_list_users.setRowCount(len(rows))
        self.ui.tableWidget_list_users.setColumnCount(
            5
        )  # Assuming 4 general info columns + 1 permissions column

        checkbox_texts = [
            "تغییر مدل",
            "مدیریت کاربران",
            "گزارش گیری",
            "تولید جعبه",
            "مدیریت دیتابیس",
        ]

        # Iterate over rows to populate table
        for row_idx, row_data in enumerate(rows):
            # Display general information (first 4 columns)
            for col_idx in range(4):
                item = QTableWidgetItem(str(row_data[col_idx]))
                self.ui.tableWidget_list_users.setItem(row_idx, col_idx, item)

            # Check permissions (last column)
            permissions_text = []
            for col_idx in range(4, 9):  # Assuming permissions are in columns 4 to 8
                if row_data[col_idx] == 1:
                    permission_index = (
                        col_idx - 4
                    )  # Calculate corresponding index in checkbox_texts
                    if permission_index < len(checkbox_texts):
                        permissions_text.append(checkbox_texts[permission_index])

            # Create text from permissions_text list
            permissions_str = " , ".join(permissions_text)
            item = QTableWidgetItem(permissions_str)
            self.ui.tableWidget_list_users.setItem(row_idx, 4, item)

    def delete_selected_rows2(self):
        selected_ranges = self.ui.tableWidget_list_users.selectedRanges()
        if not selected_ranges:
            QMessageBox.warning(
                self, "سطر انتخاب نشده", "لطفا کاربر مورد نظر را انتخاب کنید"
            )
            return

        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("هشدار")
        msg_box.setText("آیا میخواهید کاربر مورد نظر را حذف کنید؟")
        accept_button = msg_box.addButton("حذف", QMessageBox.AcceptRole)
        msg_box.addButton("لغو", QMessageBox.RejectRole)
        msg_box.exec()

        if msg_box.clickedButton() == accept_button:
            rows_to_delete = set()

            for selected_range in selected_ranges:
                for row in range(
                    selected_range.topRow(), selected_range.bottomRow() + 1
                ):
                    rows_to_delete.add(row)

            try:
                for row in sorted(rows_to_delete, reverse=True):
                    username_item = self.ui.tableWidget_list_users.item(
                        row, 2
                    )  # Assuming username is in column index 2
                    if username_item is not None:
                        username = username_item.text()
                        if username:
                            self.database.delete_user(username)
                            self.ui.tableWidget_list_users.removeRow(row)
            except Exception as e:
                QMessageBox.critical(
                    self, "خطا در حذف", f"خطا در حذف کاربر از پایگاه داده: {str(e)}"
                )

            QMessageBox.information(self, "حذف", "کاربر مورد نظر با موفقیت حذف شد")

    def adduser(self):

        dialog = AddUser(self.ui.tableWidget_list_users, self.database)
        dialog.exec()

    def edituser(self):
        selected_items = self.ui.tableWidget_list_users.selectedItems()
        if not selected_items:
            QMessageBox.warning(
                self, "سطر انتخاب نشده", "لطفا یک کاربر را برای ویرایش انتخاب کنید"
            )
            return
        dialog = EditUser(
            self.ui.tableWidget_list_users,
            self.database,
            selected_items,
            self.show_table,
        )

        result = dialog.exec()

        if result == QDialog.Accepted:
            self.handelpermissions()
            print("User clicked OK")
        elif result == QDialog.Rejected:
            print("User clicked Cancel or closed the dialog")

    # def refresh_table(self):
    #     rows = self.database.fetch_all()
    #     self.ui.tableWidget_list_users.setRowCount(len(rows))
    #     self.ui.tableWidget_list_users.setColumnCount(len(rows[0]))
    #     for row_idx, row_data in enumerate(rows):
    #         for col_idx, col_data in enumerate(row_data):
    #             item = QTableWidgetItem(str(col_data))
    #             self.ui.tableWidget_list_users.setItem(row_idx, col_idx, item)
    def navigation(self, text):
        if text == "scan":
            self.ui.stackedWidget.setCurrentIndex(0)
        if text == "user":
            self.show_table()
            self.ui.stackedWidget.setCurrentIndex(1)
        if text == "database":
            self.ui.stackedWidget.setCurrentIndex(2)
        if text == "account":
            self.print_action()
            self.ui.stackedWidget.setCurrentIndex(3)
        if text == "report":
            self.ui.stackedWidget.setCurrentIndex(4)

    def generate_svg_with_text(text, filename, width="100mm", height="50mm"):
        # Ensure width and height are strings with units
        if isinstance(width, (int, float)):
            width = f"{width}mm"
        if isinstance(height, (int, float)):
            height = f"{height}mm"

        # Create a new SVG drawing with specified width and height
        dwg = svgwrite.Drawing(filename, size=(width, height))

        # Add text to the SVG
        dwg.add(
            dwg.text(
                text,
                insert=(10, 20),
                fill="black",
                font_family="Arial",
                font_size="12px",
            )
        )

        # Save the SVG file
        dwg.save()

    def delete_selected_rows(self):
        try:
            selected_ranges = self.ui.tableWidget.selectedRanges()
            if not selected_ranges:
                QMessageBox.warning(
                    self, "انتخاب کنید", "لطفا سطر مورد نظر را انتخاب کنید."
                )
                return

            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("هشدار")
            msg_box.setText("سطر پاک خواهد شد")
            custom_button_1 = msg_box.addButton(
                "قبول", QtWidgets.QMessageBox.AcceptRole
            )
            custom_button_2 = msg_box.addButton("لغو", QtWidgets.QMessageBox.RejectRole)
            msg_box.exec()

            if msg_box.clickedButton() == custom_button_1:
                rows_to_delete = set()
                row_items_count = {}  # Dictionary to store item count for each row

                for selected_range in selected_ranges:
                    for row in range(
                        selected_range.topRow(), selected_range.bottomRow() + 1
                    ):
                        rows_to_delete.add(row)
                        # Get item count for the current row
                        item_count = self.get_item_count_in_row(row)
                        row_items_count[row] = (
                            item_count  # Save item count in the dictionary
                        )

                for row in sorted(rows_to_delete, reverse=True):
                    self.ui.tableWidget.removeRow(row)

                self.total -= item_count
            elif msg_box.clickedButton() == custom_button_2:
                return

        except Exception as e:
            self.error_handler(f"Error Deleting Row: {e}")
        self.ui.lineEdit.setFocus()

    def get_item_count_in_row(self, row_index):
        try:
            item_count = 0
            for col_index in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row_index, col_index)
                widget = self.ui.tableWidget.cellWidget(row_index, col_index)
                if (item is not None and item.text()) or (
                    widget is not None
                    and isinstance(widget, QLabel)
                    and widget.pixmap()
                ):
                    item_count += 1
            return int(item_count / 2)
        except Exception as e:
            self.error_handler(f"Error item count: {e}")
        self.ui.lineEdit.setFocus()

    def clear_table(self):
        try:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("هشدار")
            msg_box.setText("تمام داده های جدول پاک خواهند شد")
            custom_button_1 = msg_box.addButton(
                "قبول", QtWidgets.QMessageBox.AcceptRole
            )
            custom_button_2 = msg_box.addButton("لغو", QtWidgets.QMessageBox.RejectRole)
            msg_box.exec()
            if msg_box.clickedButton() == custom_button_1:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["سریال", "تصویر", "سریال", "تصویر"]
                )
                self.total = 0
            elif msg_box.clickedButton() == custom_button_2:
                return
        except Exception as e:
            self.error_handler(f"Error Clearning Table: {e}")
        self.ui.lineEdit.setFocus()

    def closeEvent(self, event):
        # Call the closeEvent method of the Directory instance
        self.dir.closeEvent(event)
        event.accept()

    def showAboutMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("درباره")
        msg.setText(
            "طراح و توسعه دهنده : <a href='https://www.linkedin.com/in/amir-hossein-nikravan-92877b232/'>امیر حسین نیک روان</a>"
        )
        msg.exec()
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setFocus()

    def validation(self):
        try:
            status = self.database.validation()
            self.ui.label_count.setText(str(self.database.count_rows_in_excel()))
            if status[1] == True:
                self.ui.label_excel_status.setText("متعبر")
            if status[0] == False:

                self.ui.toolButton_deleteuser.setEnabled(False)
                self.ui.toolButton_edituser.setEnabled(False)
                self.ui.toolButton_newuser.setEnabled(False)

                self.ui.label_db_status.setText("نامتعبر")
                self.ui.pushButton_scan.setEnabled(False)
                self.ui.lineEdit.setEnabled(False)
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setFocus()
                return False
            else:
                # self.ui.label_db_status.clear()
                self.ui.label_db_status.setText("معتبر")
                self.ui.toolButton_deleteuser.setEnabled(True)
                self.ui.toolButton_edituser.setEnabled(True)
                self.ui.toolButton_newuser.setEnabled(True)
                self.ui.pushButton_scan.setEnabled(True)
                self.ui.lineEdit.setEnabled(True)
            if status[1] == False:
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setFocus()
                self.ui.pushButton_scan.setEnabled(False)
                self.ui.lineEdit.setEnabled(False)
                self.ui.label_excel_status.setText("نامتعبر")
                # self.ui
            else:
                self.ui.pushButton_scan.setEnabled(True)
                self.ui.lineEdit.setEnabled(True)
                self.ui.label_excel_status.setText("متعبر")

            return status[0] and status[1]
        except Exception as e:
            self.error_handler(f"Error main validation: {e}")    
    def barcode_scan(self):
        try:
            if (self.ui.tableWidget.item(9, 2)) != None:
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setFocus()
                QMessageBox.information(self, "سطر", "تعداد IMEI ها تکمیل است.")
                return
            try:
                self.barcode_serial = self.ui.lineEdit.text()
                if len(self.barcode_serial) != 15 or re.search(
                    "[^0-9]", self.barcode_serial
                ):
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setFocus()
                    return
            except Exception as e:
                self.error_handler(f"Error Line Edit: {e}")
            self.ui.lineEdit.clear()
            barcode.base.Barcode.default_writer_options["write_text"] = False
            if self.barcode_serial:
                imei2 = self.database.search_imei(self.barcode_serial)
                if not imei2:
                    QMessageBox.warning(
                        self,
                        "هشدار",
                        f"بارکد {self.barcode_serial} در اکسل وجود ندارد.",
                    )
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setFocus()
                    return
                for row in range(self.ui.tableWidget.rowCount()):
                    item = self.ui.tableWidget.item(row, 0)
                    if item:
                        text = item.text()
                        pattern = re.compile(r"IMEI\s*:\s*(\d+)", re.IGNORECASE)
                        match = pattern.search(text)
                        imei_number = match.group(1) if match else ""
                        if self.barcode_serial == imei_number:
                            QMessageBox.warning(
                                self,
                                "هشدار",
                                f"بارکد {self.barcode_serial} قبلا وارد شده است.",
                            )
                            self.ui.lineEdit.clear()
                            self.ui.lineEdit.setFocus()
                            return
                action = f"بارکد {self.barcode_serial} اسکن شد"
                self.database.action(
                    self.current_user, f"{self.date_text}-{self.time_text}", action
                )
                options = {
                    "dpi": 2000,
                    "module_width": 0.3,
                    "module_height": 8,
                    "quiet_zone": 1,
                    "text_distance": 5,
                    "font_size": 8.5,
                    "font_path": "ARIAL.TTF",
                }
                options2 = {
                    "dpi": 2000,
                    "module_width": 0.02,
                    "module_height": 0.59,
                    "quiet_zone": 1.5,
                    "text_distance": 0.3,
                    "font_size": 0.7,
                    "font_path": "ARIAL.TTF",
                }

                code = QTableWidgetItem(f"IMEI: {self.barcode_serial}")
                font = QFont()
                font.setFamily("Arial")  # Set the font family
                font.setPointSize(12)
                code.setFont(font)
                code2 = QTableWidgetItem(f"IMEI: {imei2}")
                code2.setFont(font)
                try:
                    with open(f"./images/{self.barcode_serial}.png", "wb") as f:
                        barcode.base.Barcode.default_writer_options["text"] = (
                            f"IMEI: {self.barcode_serial}"
                        )
                        writer = ImageWriter()

                        barcode_class = barcode.get_barcode_class("code128")
                        barcode_instance = barcode_class(
                            f"{self.barcode_serial}", writer
                        )
                        try:
                            barcode_instance.write(f, options=options2)
                        except Exception as e:
                            print(f"Error creating ImageWriter: {e}")
                            traceback.print_exc()

                    with open(f"./images/{imei2}.png", "wb") as f:
                        barcode.base.Barcode.default_writer_options["text"] = (
                            f"IMEI: {imei2}"
                        )
                        writer = ImageWriter()

                        barcode_class = barcode.get_barcode_class("code128")
                        barcode_instance = barcode_class(f"{imei2}", writer)
                        try:
                            barcode_instance.write(f, options=options2)
                        except Exception as e:
                            print(f"Error creating ImageWriter: {e}")
                            traceback.print_exc()

                    with open(f"./images/{self.barcode_serial}.svg", "wb") as f:
                        barcode.base.Barcode.default_writer_options["text"] = (
                            f"IMEI: {self.barcode_serial}"
                        )
                        writer = SVGWriter()
                        barcode_class = barcode.get_barcode_class("code128")
                        barcode_instance = barcode_class(
                            f"{self.barcode_serial}", writer
                        )
                        barcode_instance.write(f, options=options)
                        # Print detailed traceback for debuggin
                    with open(f"./images/{imei2}.svg", "wb") as f:
                        barcode.base.Barcode.default_writer_options["text"] = (
                            f"IMEI: {imei2}"
                        )
                        writer = SVGWriter()
                        barcode_class = barcode.get_barcode_class("code128")
                        barcode_instance = barcode_class(f"{imei2}", writer)
                        barcode_instance.write(f, options=options)
                        # Print detailed traceback for debuggin

                except Exception as e:
                    self.error_handler(f"Error Creating Barcodes: {e}")
                try:
                    pic = QtGui.QPixmap(f"./images/{self.barcode_serial}.png")
                    label = QtWidgets.QLabel()
                    label.width = 10
                    label.height = 100
                    label.setPixmap(pic)
                    pic2 = QtGui.QPixmap(f"./images/{imei2}.png")
                    label2 = QtWidgets.QLabel()
                    label2.width = 10
                    label2.height = 100
                    label2.setPixmap(pic2)
                except Exception as e:
                    self.error_handler(f"Error Creating table label: {e}")
                try:

                    self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)

                    self.ui.tableWidget.setItem(
                        self.ui.tableWidget.rowCount() - 1, 0, code
                    )
                    self.ui.tableWidget.setCellWidget(
                        self.ui.tableWidget.rowCount() - 1, 1, label
                    )
                    self.ui.tableWidget.setItem(
                        self.ui.tableWidget.rowCount() - 1, 2, code2
                    )
                    self.ui.tableWidget.setCellWidget(
                        self.ui.tableWidget.rowCount() - 1, 3, label2
                    )
                    self.ui.tableWidget.setRowHeight(
                        self.ui.tableWidget.rowCount() - 1, 100
                    )
                    label.setAlignment(Qt.AlignCenter)
                    self.database.barcode_scan(
                        self.current_user,
                        f"{self.date_text}-{self.time_text}",
                        f"{self.barcode_serial}",
                    )
                    print(imei2)
                    self.database.barcode_scan(
                        self.current_user,
                        f"{self.date_text}-{self.time_text}",
                        f"{imei2}",
                    )
                except Exception as e:
                    self.error_handler(f"Error Inserting Barcodes in Table: {e}")
                self.total += 2
                self.disable_editing(self.ui.tableWidget.rowCount() - 1)
                self.disable_scanning()
                self.ui.lineEdit.setFocus()

        except Exception as e:
            self.error_handler(f"Error Barcode Scan Fucntion: {e}")
        self.ui.lineEdit.setFocus()

    def disable_editing(self, row):
        try:
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        except Exception as e:
            self.error_handler(f"Error disable editing: {e}")

    def handlecombo(self):
        try:
            self.data = {
                "select": {},
                "NOKIA 105TA-1557 DS": {
                    "1GF019CPG6F02": ["Cyan"],
                    "1GF019CPA2F01": ["Charcoal"],
                    "1GF019CPA2F02": ["Charcoal"],
                },
                "NOKIA 106TA-1564 DS": {
                    "1GF019BPA2F02": ["Charcoal"],
                    "1GF019BPJ1F02": ["Emerald Green"],
                    "1GF019BPB1F02": ["Terracotta Red"],
                },
                "NOKIA 110TA-1567 DS": {
                    "1GF019FPA2F02": ["Charcoal"],
                    "1GF019FPG3F02": ["Cloudy Blue"],
                },
            }

            self.ui.comboBox_model.addItems(self.data.keys())
            self.ui.comboBox_model.currentIndexChanged.connect(self.update_skus)
            self.ui.comboBox_sku.currentIndexChanged.connect(self.update_colors)
        except Exception as e:
            self.error_handler(f"Error handel combo: {e}")
    def update_skus(self):
        selected_model = self.ui.comboBox_model.currentText()
        skus = self.data.get(selected_model, {}).keys()
        self.ui.comboBox_sku.clear()
        self.ui.comboBox_sku.addItems(skus)
        self.update_colors()

    def update_colors(self):
        selected_model = self.ui.comboBox_model.currentText()
        selected_sku = self.ui.comboBox_sku.currentText()
        colors = self.data.get(selected_model, {}).get(selected_sku, [])
        self.ui.comboBox_color.clear()
        self.ui.comboBox_color.addItems(colors)

    def print_box(self, text):
        options = {
            "dpi": 2000,
            "module_width": 0.3,
            "module_height": 8,
            "quiet_zone": 1,
            "text_distance": 5,
            "font_size": 7.5,
            "font_path": "ARIAL.TTF",
        }
        with open(f"./images/box.svg", "wb") as f:
            barcode.base.Barcode.default_writer_options["text"] = (
                f"Carton Number: {text}"
            )
            writer = SVGWriter()
            barcode_class = barcode.get_barcode_class("code128")
            barcode_instance = barcode_class(text, writer)
            barcode_instance.write(f, options=options)

    def handlePrint(self):
        try:
            if (self.ui.tableWidget.item(9, 2)) == None:
                QMessageBox.warning(self, "تعداد IMEI", "بارکد ها ناقص می باشند")
                return
            if self.ui.comboBox_model.currentText() == "select":
                msg_box = QtWidgets.QMessageBox(self)
                msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                msg_box.setWindowTitle("هشدار")
                msg_box.setText("لطفا مدل را وارد کنید")
                msg_box.exec()
                return
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec() == QtWidgets.QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
                self.clear_table()
        except Exception as e:
            self.error_handler(f"Error Handel Print: {e}")
        self.ui.lineEdit.setFocus()

    def create_svg(self, text, filename, font, x, y):
        # Create an SVG drawing
        dwg = svgwrite.Drawing(f"{filename}", profile="tiny", size=("200px", "15px"))

        # Add text to the drawing
        dwg.add(dwg.text(text, insert=(x, y), fill="black", font_size=f"{font}px"))

        # Save the SVG file
        dwg.save()

    def handlePaintRequest(self, printer):

        doc = ss.Document()
        final_layout = ss.VBoxLayout()
        try:
            model = self.ui.comboBox_model.currentText()
            sku = self.ui.comboBox_sku.currentText()
            color = self.ui.comboBox_color.currentText()
        except Exception as e:
            self.error_handler(f"Error Handel print: {e}")
        # if model == "select":
        #     msg_box = QtWidgets.QMessageBox(self)
        #     msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        #     msg_box.setWindowTitle("هشدار")
        #     msg_box.setText("لطفا مدل را وارد کنید")
        #     msg_box.exec()
        #     return
        try:
            bala_layout = ss.VBoxLayout()
            bala_rast = ss.VBoxLayout()
            bala_chap = ss.VBoxLayout()
            bala_vasat = ss.HBoxLayout()
            bala_final = ss.HBoxLayout()
            self.create_svg(
                f"Manufacture Date: {datetime.datetime.now().year}/{datetime.datetime.now().month}",
                "./images/date.svg",
                10,
                1,
                1,
            )
            self.create_svg(
                f"Part Number: {sku}",
                "./images/pn.svg",
                10,
                1,
                1,
            )
            print(model)
            if model == "NOKIA 110TA-1567 DS":
                model_text = "1.752"
            else:
                print(234234)
                model_text = "1.750"
            print(model_text)
            self.create_svg(
                f"Weight: {model_text}kg",
                "./images/wieght.svg",
                10,
                1,
                1,
            )
            self.create_svg(
                "Quantity: 10/10",
                "./images/quantity.svg",
                10,
                1,
                1,
            )
            formatted_text = self.format_number(self.box)
            formatted_text = "SAMTEL" + formatted_text
            self.box += 1
            self.print_box(formatted_text)
            bala_rast.addSVG(
                f"./svgs/blank11.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_rast.addSVG(f"./images/date.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_rast.addSVG(f"./images/pn.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_rast.addSVG(
                f"./images/wieght.svg", alignment=ss.AlignTop | ss.AlignLeft
            )

            bala_rast.addSVG(f"./images/box.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_rast.addSVG(
                f"./images/quantity.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_chap.addSVG(f"./svgs/blank5.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_layout.addSVG(
                f"./svgs/blank6.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_layout.addSVG(f"./svgs/logo.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_layout.addSVG(
                f"./svgs/b{sku}.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_layout.addSVG(
                f"./svgs/{sku}.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_layout.addSVG(
                f"./svgs/blank3.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            bala_vasat.addSVG(
                f"./svgs/blank10.svg", alignment=ss.AlignTop | ss.AlignLeft
            )

            bala_final.addLayout(bala_chap)
            bala_final.addLayout(bala_layout)
            bala_final.addLayout(bala_vasat)
            bala_final.addLayout(bala_rast)
            full_table_layout = ss.HBoxLayout()
            table1_layout = ss.HBoxLayout()
            table2_layout = ss.HBoxLayout()
            l11 = ss.VBoxLayout()
            l12 = ss.VBoxLayout()
            lfirst = ss.VBoxLayout()
            l13 = ss.VBoxLayout()
            l14 = ss.VBoxLayout()
            l21 = ss.VBoxLayout()
            l22 = ss.VBoxLayout()
            l23 = ss.VBoxLayout()
            l24 = ss.VBoxLayout()
        except Exception as e:
            self.error_handler(f"Error bala_layout: {e}")
        try:
            table = self.ui.tableWidget
            imei1 = ""
            imei2 = ""
            for row in range(table.rowCount()):
                # Assuming you want to access items from the first and second columns
                item_column1 = table.item(row, 0)  # First column item
                item_column2 = table.item(row, 2)  # Second column item

                if item_column1:
                    text_column1 = item_column1.text()
                    pattern = re.compile(r"IMEI\s*:\s*(\d+)", re.IGNORECASE)
                    match = pattern.search(text_column1)
                    imei_number = match.group(1) if match else ""
                    # Build the path
                    imei1 += str(imei_number)
                    path1 = f"./images/{imei_number}.svg"
                    # Print the path
                    if row == 0:
                        lfirst.addSVG(
                            "./svgs/blank7.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                        l11.addSVG(
                            "./svgs/imei1.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                        l11.addSVG(
                            "./svgs/blank4.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                    if row < 5:
                        l12.addSVG(path1, alignment=ss.AlignTop | ss.AlignLeft)
                    else:
                        l13.addSVG(
                            "./svgs/blank8.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                        l14.addSVG(path1, alignment=ss.AlignTop | ss.AlignLeft)

                vasat = ss.HBoxLayout()
                vasat.addSVG("./svgs/blank2.svg", alignment=ss.AlignTop | ss.AlignLeft)
                # Construct SVG elements for the second column
                if item_column2:
                    text_column2 = item_column2.text()
                    pattern = re.compile(r"imei\s*:\s*(\d+)", re.IGNORECASE)

                    # Extract number using regular expression
                    match = pattern.search(text_column2)
                    imei_number = match.group(1) if match else "t"
                    imei2 += str(imei_number)
                    # Build the path
                    path2 = f"./images/{imei_number}.svg"
                    if row == 0:
                        l21.addSVG(
                            "./svgs/imei2.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                        l21.addSVG(
                            "./svgs/blank4.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )

                    if row < 5:
                        l22.addSVG(path2, alignment=ss.AlignTop | ss.AlignLeft)
                    else:
                        l23.addSVG(
                            "./svgs/blank8.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                        l24.addSVG(path2, alignment=ss.AlignTop | ss.AlignLeft)
        except Exception as e:
            self.error_handler(f"Error output tables: {e}")
        try:

            def create_qr_code(data, filename):
                factory = qrcode.image.svg.SvgImage  # Specify SVG image factory
                qr = qrcode.QRCode(
                    version=1,  # Controls the size of the QR Code: 1 is the smallest
                    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
                    box_size=14,  # Size of each box in pixels
                    border=4,  # Thickness of the border (default is 4)
                )
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(image_factory=factory)
                img.save(filename)

            create_qr_code(imei1, "./images/qrcode1.svg")
            create_qr_code(imei2, "./images/qrcode2.svg")
            full_qr_layout = ss.HBoxLayout()
            full_qr_layout.addSVG(
                "./svgs/blankbefore.svg", alignment=ss.AlignTop | ss.AlignLeft
            )

            full_qr_layout.addSVG(
                "./images/qrcode1.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            full_qr_layout.addSVG(
                "./svgs/blank1.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
            full_qr_layout.addSVG(
                "./images/qrcode2.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
        except Exception as e:
            self.error_handler(f"Error creating Qr code: {e}")
        try:
            table1_layout.addLayout(lfirst)
            table1_layout.addLayout(l11)
            table1_layout.addLayout(l12)
            table1_layout.addLayout(l13)
            table1_layout.addLayout(l14)
            table2_layout.addLayout(l21)
            table2_layout.addLayout(l22)
            table2_layout.addLayout(l23)
            table2_layout.addLayout(l24)
            full_table_layout.addLayout(table1_layout)
            full_table_layout.addLayout(vasat)

            full_table_layout.addLayout(table2_layout)
            final_layout.addLayout(bala_final)
            final_layout.addLayout(full_table_layout)
            final_layout.addLayout(full_qr_layout)
            doc.setLayout(final_layout)

            doc.save("qt_api_test.svg")
        except Exception as e:
            self.error_handler(f"Error creating layout: {e}")
        # os.startfile('qt_api_test.svg')

        # Function to convert SVG to PDF

        # Example usage
        # input_svg = "qt_api_test.svg"
        # output_pdf = "output.pdf"
        try:
            self.convert_svg_to_pdf()
        except Exception as e:
            self.error_handler(f"Error convert_svg_to_pdf: {e}")

    def svg_to_pdf(self, input_svg_path, output_pdf_path):
        try:
            drawing = svg2rlg(input_svg_path)
            renderPDF.drawToFile(drawing, output_pdf_path)
        except Exception as e:
            self.error_handler(f"Error svg_to_pdf: {e}")

    def save_file_dialog(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save PDF",
                "",
                "PDF Files (*.pdf);;All Files (*)",
                options=options,
            )
            return file_path
        except Exception as e:
            self.error_handler(f"Error save file dialog: {e}")

    def convert_svg_to_pdf(self):
        try:
            input_svg = "qt_api_test.svg"  # Your SVG file
            output_pdf = (
                f"{self.save_file_dialog()}.pdf"  # Get save file path from dialog
            )
            if output_pdf:
                self.svg_to_pdf(input_svg, output_pdf)
        except Exception as e:
            self.error_handler(f"Error convert svg to pdf: {e}")

    def disable_scanning(self):
        try:
            delay = (
                self.ui.doubleSpinBox.value() * 1000
            )  # Convert seconds to milliseconds
            self.ui.pushButton_scan.setEnabled(False)
            self.ui.lineEdit.setEnabled(False)
            self.scan_timer.start(delay)
        except Exception as e:
            self.error_handler(f"Error disabale scanning: {e}")

    def enable_scanning(self):
        try:
            self.ui.pushButton_scan.setEnabled(True)
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit.setFocus()
        except Exception as e:
            self.error_handler(f"Error enable scanning: {e}")

    def print_action(self):
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
        for num_row, (time, action) in enumerate(rows):
            self.ui.tableWidget_history.setRowCount(
                self.ui.tableWidget_history.rowCount() + 1
            )
            self.ui.tableWidget_history.setItem(num_row, 0, QTableWidgetItem(time))
            self.ui.tableWidget_history.setItem(num_row, 1, QTableWidgetItem(action))

    def error_handler(self, msg):
        try:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(msg)
            msg_box.exec()
        except Exception as e:
            msg_box2 = QtWidgets.QMessageBox(self)
            msg_box2.setIcon(QMessageBox.Critical)
            msg_box2.setWindowTitle("Error")
            msg_box2.setText(f"error handler :{msg}")
            msg_box2.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.handellogin()
    sys.exit(app.exec())
