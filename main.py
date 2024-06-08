from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox ,QLabel,QTableWidgetItem,QErrorMessage
import sys,os
from PIL import Image
import barcode.base
import barcode.itf
from ui_main import Ui_MainWindow
from barcode import Code128
from barcode.writer import ImageWriter
from PySide6 import QtGui, QtPrintSupport ,QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
import barcode
import re
import qrcode
from directory import Directory
import qrcode
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #signals 
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.toolButton_print.clicked.connect(self.handlePrint)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
        self.ui.pushButton_clear.clicked.connect(self.clear_table)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.toolButton_preview.clicked.connect(self.handlePreview)
        self.ui.toolButton_deleterow.clicked.connect(self.delete_selected_rows)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.changeRowColor)
        #table config
        self.ui.tableWidget.setColumnWidth(0,180)
        self.ui.tableWidget.setColumnWidth(1,450)
        self.ui.tableWidget.setColumnWidth(2,180)
        self.ui.tableWidget.setColumnWidth(3,450)
        #lineeidt config
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setMaxLength(15)
        #total barcodes
        self.total = 0
        #directory config
        self.dir = Directory()
        self.scan_timer = QTimer(self)
        self.scan_timer.setSingleShot(True)
        self.scan_timer.timeout.connect(self.enable_scanning)
    # def changeRowColor(self):
    #     selected_items = self.ui.tableWidget.selectedItems()
    #     if selected_items:
    #         selected_row = selected_items[0].row()
    #         for column in range(self.ui.tableWidget.columnCount()):
    #             self.ui.tableWidget.item(selected_row, column).setBackground(QColor(255, 0, 0))  # Change color as needed
    #             self.ui.tableWidget.item(selected_row, column).setForeground(QColor(255, 255, 255))  # Change text color if needed

    #         for row in range(self.ui.tableWidget.rowCount()):
    #             if row != selected_row:
    #                 for column in range(self.ui.tableWidget.columnCount()):
    #                     self.ui.tableWidget.item(row, column).setBackground(QColor(255, 255, 255))  # Change color as needed
    #                     self.ui.tableWidget.item(row, column).setForeground(QColor(0, 0, 0))  # Change text color if needed

    def delete_selected_rows(self):
        try:
            selected_ranges = self.ui.tableWidget.selectedRanges()
            if not selected_ranges:
                QMessageBox.warning(self, "انتخاب کنید", "لطفا سطر مورد نظر را انتخاب کنید.")
                return
            
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("هشدار")
            msg_box.setText('سطر پاک خواهد شد')
            custom_button_1 = msg_box.addButton("قبول", QtWidgets.QMessageBox.AcceptRole)
            custom_button_2 = msg_box.addButton("لغو", QtWidgets.QMessageBox.RejectRole)
            msg_box.exec()
            
            if msg_box.clickedButton() == custom_button_1:
                rows_to_delete = set()
                row_items_count = {}  # Dictionary to store item count for each row
                
                for selected_range in selected_ranges:
                    for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                        rows_to_delete.add(row)
                        # Get item count for the current row
                        item_count = self.get_item_count_in_row(row)
                        row_items_count[row] = item_count  # Save item count in the dictionary
                
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
                if (item is not None and item.text()) or (widget is not None and isinstance(widget, QLabel) and widget.pixmap()):
                    item_count += 1
            return int(item_count /2 )
        except Exception as e:
            self.error_handler(f"Error item count: {e}")
        self.ui.lineEdit.setFocus()

    def clear_table(self):
        try:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("هشدار")
            msg_box.setText('تمام داده های جدول پاک خواهند شد')
            custom_button_1 = msg_box.addButton("قبول", QtWidgets.QMessageBox.AcceptRole)
            custom_button_2 = msg_box.addButton("لغو", QtWidgets.QMessageBox.RejectRole)
            msg_box.exec()
            if msg_box.clickedButton() == custom_button_1:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(['سریال', 'تصویر', 'سریال', 'تصویر'])
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
        msg.setWindowTitle("About")
        msg.setText("Developer : Amir Hossein Nikravan")
        msg.exec()
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setFocus()

    def barcode_scan(self):
        try:
            try:
                self.barcode_serial = self.ui.lineEdit.text()
            except Exception as e:
                self.error_handler(f"Error Line Edit: {e}")
            self.ui.lineEdit.clear()
            barcode.base.Barcode.default_writer_options['write_text'] = False
            if self.barcode_serial:
                
                options = {
    'dpi': 2000,
    # 'module_height': 15,
    'quiet_zone': 9,
    'text_distance': 5
}                               
                if self.total % 2 ==0 :
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI1={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI1={self.barcode_serial}")

                else:
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI2={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI2={self.barcode_serial}")
                try :
                    with open(f"./images/{self.barcode_serial}.jpeg", "wb") as f:
                        a=ImageWriter()
                        Code128(f"{self.barcode_serial}", a,).write(f,options=options)
                    with Image.open(f"./images/{self.barcode_serial}.jpeg") as img:
                        resized_img = img.resize((400, 100), Image.LANCZOS)
                        resized_img.save(f"./images/{self.barcode_serial}.jpeg")
                except Exception as e:
                    self.error_handler(f"Error Creating Barcodes: {e}")
                try:
                    pic = QtGui.QPixmap(f"./images/{self.barcode_serial}.jpeg")
                    label = QtWidgets.QLabel()
                    label.width = 10
                    label.height = 100
                    label.setPixmap(pic)
                except Exception as e:
                    self.error_handler(f"Error Creating table label: {e}")
                try:
                    if self.total % 2 ==0 :
                        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)

                        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, code)
                        self.ui.tableWidget.setCellWidget(
                            self.ui.tableWidget.rowCount() - 1, 1, label
                        )
                    else :
                        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 2, code)
                        self.ui.tableWidget.setCellWidget(
                            self.ui.tableWidget.rowCount()-1, 3, label
                        )
                    self.ui.tableWidget.setRowHeight(
                        self.ui.tableWidget.rowCount() - 1, 100
                    )
                    label.setAlignment(Qt.AlignCenter)
                except Exception as e:
                    self.error_handler(f"Error Inserting Barcodes in Table: {e}")
                self.total += 1
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
    def handlePrint(self):
        try:
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec() == QtWidgets.QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
            
        except Exception as e:
            self.error_handler(f"Error Handel Print: {e}")
        self.ui.lineEdit.setFocus()
    def handlePreview(self):
        try : 
            dialog = QtPrintSupport.QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec()
        except Exception as e:
            self.error_handler(f"Error Handel Preview: {e}")
        self.ui.lineEdit.setFocus()

    def handlePaintRequest(self, printer):
        try:
            document = QtGui.QTextDocument()
            total_barcodes = self.ui.tableWidget.rowCount()
            barcodes_per_page = 10  # 10 rows per page

            # Calculate total pages considering page breaks after every 10 rows
            total_pages = (total_barcodes + barcodes_per_page - 1) // barcodes_per_page

            html = ""
            for page_num in range(total_pages):
                qr_code = ''
                html += """
                <html>
                    <head>
                        <style>
                            .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 300px;
        height: auto;
        padding-left: 0; /* کاهش پدینگ چپی */
        padding-right: 20px; /* حفظ پدینگ راستی */
        text-align: center; /* قرار دادن تصویر در وسط */
        }
                            table {
                                border-collapse: collapse;
                                width: 100%;
                            }
                            th, td {
                                padding: 8px;
                                text-align: left;
                                border-bottom: 1px solid #ddd;
                            }
                            img {
                                max-width: 0px;
                                max-height: 80px;
                            }
                        </style>
                    </head>
                    <body>
                        <table>
                """

                # Loop through 10 rows per page
                for row_num in range(page_num * barcodes_per_page, min(page_num * barcodes_per_page + barcodes_per_page, total_barcodes)):
                    # Check if data exists in the row (avoid empty rows)
                    if row_num < total_barcodes:
                        html += "<tr>"
                        # Access data from columns 1 and 3
                        data1 = self.ui.tableWidget.item(row_num, 0).text() if self.ui.tableWidget.item(row_num, 0) else ""
                        data3 = self.ui.tableWidget.item(row_num, 2).text() if self.ui.tableWidget.item(row_num, 2) else ""

                        # Extracting the codes
                        match1 = re.search(r'=(\S+)', data1)
                        code1 = match1.group(1) if match1 else ""
                        match3 = re.search(r'=(\S+)', data3)
                        code3 = match3.group(1) if match3 else ""
                        qr_code += f'{code1},{code3}'
                        img_path1 = os.path.join("./images", f"{code1}.jpeg")
                        img_path3 = os.path.join("./images", f"{code3}.jpeg")
                        
                        if os.path.exists(img_path1):
                            with Image.open(img_path1) as img:
                                resized_img = img.resize((300, 50), Image.LANCZOS)
                                resized_img.save(img_path1)
                            html += f"<td><img src='{img_path1}' style='width: 50px;height: 50px;'></td>"
                        else:
                            html += "<td> </td>"

                        if os.path.exists(img_path3):
                            with Image.open(img_path3) as img:
                                resized_img = img.resize((300, 50), Image.LANCZOS)
                                resized_img.save(img_path3)
                            html += f"<td><img src='{img_path3}' style='width: 50px; height: 10px;object-fit: fill;'></td>"
                        else:
                            html += "<td> </td>"

                        html += "</tr>"

                html += """
                        </table>
                    </body>
                </html>
                """
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_code.rstrip(","))  # حذف کاما و فاصله اضافی در انتهای متن
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color="black", back_color="white")
                qr_img.save(f"./images/page_{page_num}_qr_code.png")  # ذخیره کد QR به عنوان یک تصویر
                with Image.open(f"./images/page_{page_num}_qr_code.png") as img:
                    resized_img = img.resize((100, 100), Image.LANCZOS)
                    resized_img.save(f"./images/page_{page_num}_qr_code.png")
                # اضافه کردن تصویر کد QR به سند HTML
                html += f"<img src='./images/page_{page_num}_qr_code.png'  class='centered-image'>"
                if page_num < total_pages - 1:
                    html += "<br style='page-break-after: always;'/>"

            document.setHtml(html)
            printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.NativeFormat)
            document.print_(printer)
        except Exception as e:
            self.error_handler(f"Error Handel Paint Request: {e}")

    def disable_scanning(self):
        try:
            delay = self.ui.doubleSpinBox.value() * 1000  # Convert seconds to milliseconds
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
    def error_handler(self,msg):
        try :
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(msg)
            msg_box.exec()
        except Exception as e:
            msg_box2 = QtWidgets.QMessageBox(self)
            msg_box2.setIcon(QMessageBox.Critical)
            msg_box2.setWindowTitle("Error")
            msg_box2.setText(f'error handler :{msg}')
            msg_box2.exec()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
