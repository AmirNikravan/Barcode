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
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.pushButton_print.clicked.connect(self.handlePrint)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.pushButton_preview.clicked.connect(self.handlePreview)
        self.ui.tableWidget.setColumnWidth(0,180)
        self.ui.tableWidget.setColumnWidth(1,450)
        self.ui.tableWidget.setColumnWidth(2,180)
        self.ui.tableWidget.setColumnWidth(3,450)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setMaxLength(15)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
        self.total = 1
        self.ui.pushButton_clear.clicked.connect(self.clear_table)
        self.dir = Directory()
    def clear_table(self):
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
            self.total = 1
        elif msg_box.clickedButton() == custom_button_2:
            return
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
    def barcode_scan(self):
        # print(self.lineEdit.text())
        try:
            self.barcode_serial = self.ui.lineEdit.text()
            self.ui.lineEdit.clear()
            barcode.base.Barcode.default_writer_options['write_text'] = False
            if self.barcode_serial:
                
                options = {
    # 'dpi': 200,
    'module_height': 15,
    'quiet_zone': 9,
    'text_distance': 5
}                               
                if self.total % 2 ==1 :
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI1={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI1={self.barcode_serial}")

                else:
                    barcode.base.Barcode.default_writer_options['text'] = f"IMEI2={self.barcode_serial}"
                    code = QTableWidgetItem(f"IMEI2={self.barcode_serial}")

                with open(f"./images/{self.barcode_serial}.jpeg", "wb") as f:
                    Code128(f"{self.barcode_serial}", writer=ImageWriter(),).write(f,options=options)
                with Image.open(f"./images/{self.barcode_serial}.jpeg") as img:
                    # Resize the image using LANCZOS filter for high-quality downsampling
                    resized_img = img.resize((400, 100), Image.LANCZOS)
                    # Save the resized image to the output path
                    resized_img.save(f"./images/{self.barcode_serial}.jpeg")
                    # print(f"Image saved to {output_path}"
                pic = QtGui.QPixmap(f"./images/{self.barcode_serial}.jpeg")
                
                label = QtWidgets.QLabel()
                label.width = 10
                label.height = 100
                label.setPixmap(pic)
                if self.total % 2 ==1 :
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

                self.total += 1
                self.disable_editing(self.ui.tableWidget.rowCount() - 1)

        except Exception as e:
            print(f"Error inserting data into table: {e}")
        self.ui.lineEdit.setFocus()
    def disable_editing(self, row):
        for col in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, col)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec() == QtWidgets.QDialog.accepted:
            self.handlePaintRequest(dialog.printer())
        self.ui.lineEdit.setFocus()
    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec()
        self.ui.lineEdit.setFocus()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        total_barcodes = self.ui.tableWidget.rowCount()
        barcodes_per_page = 10  # 10 rows per page

        # Calculate total pages considering page breaks after every 10 rows
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

                    # Get the image path based on the barcode code
                    img_path1 = os.path.join("./images", f"{code1}.jpeg")
                    img_path3 = os.path.join("./images", f"{code3}.jpeg")

                    # Check if the image exists
                    if os.path.exists(img_path1):
                        with Image.open(img_path1) as img:
                            # Resize the image using LANCZOS filter for high-quality downsampling
                            resized_img = img.resize((300, 100), Image.LANCZOS)
                            # Save the resized image to the output path
                            resized_img.save(img_path1)
                            # print(f"Image saved to {output_path}"
                        # Include the image path directly in the HTML and set the size
                        html += f"<td><img src='{img_path1}' style='max-width: 50px; max-height: 50px;'></td>"
                    else:
                        html += "<td>No Image</td>"

                    if os.path.exists(img_path3):
                        with Image.open(img_path3) as img:
                            # Resize the image using LANCZOS filter for high-quality downsampling
                            resized_img = img.resize((300, 50), Image.LANCZOS)
                            # Save the resized image to the output path
                            resized_img.save(img_path3)
                            # print(f"Image saved to {output_path}"
                        # Include the image path directly in the HTML and set the size
                        html += f"<td><img src='{img_path3}' style='max-width: 50px; max-height: 50px;'></td>"
                    else:
                        html += "<td>No Image</td>"
                        
                    html += "</tr>"

            html += """
                    </table>
                </body>
            </html>
            """

            if page_num < total_pages - 1:
                html += "<br style='page-break-after: always;'/>"

        document.setHtml(html)
        printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.NativeFormat)
        document.print_(printer)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
