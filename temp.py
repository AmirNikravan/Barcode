from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox ,QLabel,QTableWidgetItem
import sys,os
from PIL import Image
import barcode.base
import barcode.itf
from ui_main import Ui_MainWindow
from barcode import Code128
from barcode.writer import ImageWriter
from PySide6 import QtGui, QtPrintSupport ,QtWidgets
from PySide6.QtCore import *
import barcode
import re
from directory import Directory
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Signals
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.toolButton_print.clicked.connect(self.handlePrint)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
        self.ui.pushButton_clear.clicked.connect(self.clear_table)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.toolButton_preview.clicked.connect(self.handlePreview)
        self.ui.toolButton_deleterow.clicked.connect(self.delete_selected_rows)
        
        # Table config
        self.ui.tableWidget.setColumnWidth(0, 180)
        self.ui.tableWidget.setColumnWidth(1, 450)
        self.ui.tableWidget.setColumnWidth(2, 180)
        self.ui.tableWidget.setColumnWidth(3, 450)
        
        # LineEdit config
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setMaxLength(15)
        
        # Total barcodes
        self.total = 0
        
        # Directory config
        self.dir = Directory()

        # Timer for scan delay
        self.scan_timer = QTimer(self)
        self.scan_timer.setSingleShot(True)
        self.scan_timer.timeout.connect(self.enable_scanning)
        
    def delete_selected_rows(self):
        selected_ranges = self.ui.tableWidget.selectedRanges()
        if not selected_ranges:
            QMessageBox.warning(self, "انتخاب کنید", "لطفا سطر مورد نظر را انتخاب کنید.")
            return
        
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("هشدار")
        msg_box.setText('سطر پاک خواهد شد')
        custom_button_1 = msg_box.addButton("قبول", QMessageBox.AcceptRole)
        custom_button_2 = msg_box.addButton("لغو", QMessageBox.RejectRole)
        msg_box.exec()
        
        if msg_box.clickedButton() == custom_button_1:
            rows_to_delete = set()
            row_items_count = {}
            
            for selected_range in selected_ranges:
                for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                    rows_to_delete.add(row)
                    item_count = self.get_item_count_in_row(row)
                    row_items_count[row] = item_count
        
            for row in sorted(rows_to_delete, reverse=True):
                self.ui.tableWidget.removeRow(row)
            self.total -= sum(row_items_count.values())
        elif msg_box.clickedButton() == custom_button_2:
            return
        
    def get_item_count_in_row(self, row_index):
        item_count = 0
        for col_index in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row_index, col_index)
            widget = self.ui.tableWidget.cellWidget(row_index, col_index)
            if (item is not None and item.text()) or (widget is not None and isinstance(widget, QLabel) and widget.pixmap()):
                item_count += 1
        return int(item_count / 2)

    def clear_table(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("هشدار")
        msg_box.setText('تمام داده های جدول پاک خواهند شد')
        custom_button_1 = msg_box.addButton("قبول", QMessageBox.AcceptRole)
        custom_button_2 = msg_box.addButton("لغو", QMessageBox.RejectRole)
        msg_box.exec()
        
        if msg_box.clickedButton() == custom_button_1:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(['سریال', 'تصویر', 'سریال', 'تصویر'])
            self.total = 0
        elif msg_box.clickedButton() == custom_button_2:
            return

    def closeEvent(self, event):
        self.dir.closeEvent(event)
        event.accept()

    def showAboutMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Developer: Amir Hossein Nikravan")
        msg.exec()
        self.ui.lineEdit.setFocus()

    def barcode_scan(self):
        if self.scan_timer.isActive():
            return
        
        try:
            self.barcode_serial = self.ui.lineEdit.text()
            self.ui.lineEdit.clear()
            barcode.base.Barcode.default_writer_options['write_text'] = False
            
            if self.barcode_serial:
                options = {
                    'module_height': 15,
                    'quiet_zone': 9,
                    'text_distance': 5
                }
                
                if self.total % 2 == 0:
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI1={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI1={self.barcode_serial}")
                else:
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI2={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI2={self.barcode_serial}")
                
                img_path = os.path.join("images", f"{self.barcode_serial}.jpeg")
                
                with open(img_path, "wb") as f:
                    Code128(f"{self.barcode_serial}", writer=ImageWriter()).write(f, options=options)
                
                with Image.open(img_path) as img:
                    resized_img = img.resize((400, 100), Image.LANCZOS)
                    resized_img.save(img_path)
                
                pic = QtGui.QPixmap(img_path)
                
                label = QLabel()
                label.setPixmap(pic)
                
                if self.total % 2 == 0:
                    self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
                    self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, code)
                    self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 1, label)
                else:
                    self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, code)
                    self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 3, label)
                
                self.ui.tableWidget.setRowHeight(self.ui.tableWidget.rowCount() - 1, 100)
                label.setAlignment(Qt.AlignCenter)
                
                self.total += 1
                self.disable_editing(self.ui.tableWidget.rowCount() - 1)

                # Disable scanning for the specified duration
                self.disable_scanning()
        except Exception as e:
            print(f"Error inserting data into table: {e}")
        self.ui.lineEdit.setFocus()

    def disable_editing(self, row):
        for col in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, col)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def handlePrint(self):
        dialog = QPrintDialog()
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())
        self.ui.lineEdit.setFocus()

    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec()
        self.ui.lineEdit.setFocus()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        total_barcodes = self.ui.tableWidget.rowCount()
        barcodes_per_page = 10
        total_pages = (total_barcodes + barcodes_per_page - 1) // barcodes_per_page

        html = ""
        for page_num in range(total_pages):
            html += """
            <html>
                <head>
                    <style>
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
                            max-width: 50px;
                            max-height: 80px;
                        }
                    </style>
                </head>
                <body>
                    <table>
            """
            
            for row_num in range(page_num * barcodes_per_page, min(page_num * barcodes_per_page + barcodes_per_page, total_barcodes)):
                if row_num < total_barcodes:
                    html += "<tr>"
                    data1 = self.ui.tableWidget.item(row_num, 0).text() if self.ui.tableWidget.item(row_num, 0) else ""
                    data3 = self.ui.tableWidget.item(row_num, 2).text() if self.ui.tableWidget.item(row_num, 2) else ""
                    html += f"<td>{data1}</td>"
                    html += f"<td><img src='{os.path.join(os.getcwd(), 'images', data1.split('=')[1] + '.jpeg')}'></td>"
                    html += f"<td>{data3}</td>"
                    html += f"<td><img src='{os.path.join(os.getcwd(), 'images', data3.split('=')[1] + '.jpeg')}'></td>"
                    html += "</tr>"
                    
            html += """
                    </table>
                </body>
            </html>
            """
            
            if page_num < total_pages - 1:
                html += "<div style='page-break-after:always;'></div>"

        document.setHtml(html)
        document.print(printer)
        
    def disable_scanning(self):
        delay = self.ui.doubleSpinBox.value() * 1000  # Convert seconds to milliseconds
        self.ui.pushButton_scan.setEnabled(False)
        self.ui.lineEdit.setEnabled(False)
        self.scan_timer.start(delay)

    def enable_scanning(self):
        self.ui.pushButton_scan.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
