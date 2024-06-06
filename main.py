from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox ,QLabel,QTableWidgetItem
import sys,os
from PIL import Image
import barcode.base
import barcode.itf
from ui_main import Ui_MainWindow
from barcode import Code128
from barcode.writer import ImageWriter
from PySide6 import QtGui, QtPrintSupport ,QtWidgets
# from PyQt6 import QtGui
import barcode
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.pushButton_print.clicked.connect(self.handlePrint)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.pushButton_preview.clicked.connect(self.handlePreview)
        self.ui.tableWidget.setColumnWidth(0,200)
        self.ui.tableWidget.setColumnWidth(1,450)
        self.ui.tableWidget.setColumnWidth(2,200)
        self.ui.tableWidget.setColumnWidth(3,450)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setMaxLength(15)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
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
                barcode.base.Barcode.default_writer_options['text'] = f"IMEI={self.barcode_serial}"
                options = {
    # 'dpi': 200,
    # 'module_height': 1,
    'quiet_zone': 8,
    'text_distance': 5
}
                with open(f"./images/{self.barcode_serial}.jpeg", "wb") as f:
                    Code128(f"{self.barcode_serial}", writer=ImageWriter(),).write(f,options=options)
                with Image.open(f"./images/{self.barcode_serial}.jpeg") as img:
                    # Resize the image using LANCZOS filter for high-quality downsampling
                    resized_img = img.resize((300, 100), Image.LANCZOS)
                    # Save the resized image to the output path
                    resized_img.save(f"./images/{self.barcode_serial}.jpeg")
                    # print(f"Image saved to {output_path}"
                pic = QtGui.QPixmap(f"./images/{self.barcode_serial}.jpeg")
                
                label = QtWidgets.QLabel()
                label.width = 10
                label.height = 100
                label.setPixmap(pic)
                self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
                code = QTableWidgetItem(f"IMEI={self.barcode_serial}")
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, code)
                self.ui.tableWidget.setCellWidget(
                    self.ui.tableWidget.rowCount() - 1, 1, label
                )
                self.ui.tableWidget.setRowHeight(
                    self.ui.tableWidget.rowCount() - 1, 100
                )
        except Exception as e:
            print(f"Error inserting data into table: {e}")
        self.ui.lineEdit.setFocus()
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
        cursor = QtGui.QTextCursor(document)
        total_barcodes = self.ui.tableWidget.rowCount()
        barcodes_per_page = 10
        total_pages = (total_barcodes + barcodes_per_page - 1) // barcodes_per_page
        num_rows = 5
        num_cols = 2
        for page_num in range(total_pages):
            # Start a new page
            cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
            cursor.insertBlock()
            start_index = page_num * barcodes_per_page
            end_index = min(start_index + barcodes_per_page, total_barcodes)
            num_rows_batch = (end_index - start_index + num_cols - 1) // num_cols
            num_cols_batch = min(num_cols, end_index - start_index)
            for row_index in range(num_rows_batch):
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertBlock()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.EndOfBlock)
                cursor.insertText('\n')
                for col_index in range(num_cols_batch):
                    barcode_index = start_index + row_index * num_cols_batch + col_index
                    if barcode_index < end_index:
                        item_text = self.ui.tableWidget.item(barcode_index, 0).text()
                        with open(f".\\images\\{item_text}.jpeg", "wb") as f:
                            Code128(item_text, writer=ImageWriter()).write(f)
                        pic = QtGui.QPixmap(f".\\images\\{item_text}.jpeg")
                        image_format = QtGui.QTextImageFormat()
                        image_format.setWidth(310)
                        image_format.setHeight(200)
                        image_format.setName(f".\\images\\{item_text}.jpeg")  # Set the image file path
                        cursor.insertImage(image_format)
            if page_num < total_pages - 1:
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertBlock()
        printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.NativeFormat)
        document.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
