from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QLabel,
    QTableWidgetItem,
    QErrorMessage,
    QFileDialog,
)
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

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.barcodes = []
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # signals
        self.ui.pushButton_scan.clicked.connect(self.barcode_scan)
        self.ui.toolButton_print.clicked.connect(self.handlePrint)
        self.ui.lineEdit.returnPressed.connect(self.barcode_scan)
        self.ui.pushButton_clear.clicked.connect(self.clear_table)
        self.ui.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.ui.toolButton_deleterow.clicked.connect(self.delete_selected_rows)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.changeRowColor)
        # table config
        self.ui.tableWidget.setColumnWidth(0, 180)
        self.ui.tableWidget.setColumnWidth(1, 450)
        self.ui.tableWidget.setColumnWidth(2, 180)
        self.ui.tableWidget.setColumnWidth(3, 450)
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
        self.handlecombo()

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
        msg.setText ("طراح و توسعه دهنده : <a href='https://www.linkedin.com/in/amir-hossein-nikravan-92877b232/'>امیر حسین نیک روان</a>")
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
            barcode.base.Barcode.default_writer_options["write_text"] = False
            if self.barcode_serial:

                options = {
                    "dpi": 2000,
                    "module_width": 0.3,
                    "module_height": 8,
                    "quiet_zone": 5,
                    "text_distance": 5,
                    "font_size": 12,
                    "font_path":'ARIAL.TTF'
                }
                options2 = {
                    "dpi": 2000,
                    "module_width": 0.02,
                    "module_height": 0.59,
                    "quiet_zone": 1.5,
                    "text_distance": 0.3,
                    "font_size": 0.7,
                    "font_path":'ARIAL.TTF'
                }
                barcode.base.Barcode.default_writer_options["text"] = (
                    f"IMEI: {self.barcode_serial}"
                )
                code = QTableWidgetItem(f"IMEI: {self.barcode_serial}")
                font = QFont()
                font.setFamily("Arial")  # Set the font family
                font.setPointSize(12)
                code.setFont(font)

                try:
                    with open(f"./images/{self.barcode_serial}.png", "wb") as f:
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
                    with open(f"./images/{self.barcode_serial}.svg", "wb") as f:
                        writer = SVGWriter()
                        barcode_class = barcode.get_barcode_class("code128")
                        barcode_instance = barcode_class(
                            f"{self.barcode_serial}", writer
                        )
                        
                        barcode_instance.write(f, options=options)
                        
                         # Print detailed traceback for debuggin
                        self.barcodes.append(self.barcode_serial)

                except Exception as e:
                    self.error_handler(f"Error Creating Barcodes: {e}")
                try:
                    pic = QtGui.QPixmap(f"./images/{self.barcode_serial}.png")
                    label = QtWidgets.QLabel()
                    label.width = 10
                    label.height = 100
                    label.setPixmap(pic)
                except Exception as e:
                    self.error_handler(f"Error Creating table label: {e}")
                try:
                    if self.total % 2 == 0:
                        self.ui.tableWidget.setRowCount(
                            self.ui.tableWidget.rowCount() + 1
                        )

                        self.ui.tableWidget.setItem(
                            self.ui.tableWidget.rowCount() - 1, 0, code
                        )
                        self.ui.tableWidget.setCellWidget(
                            self.ui.tableWidget.rowCount() - 1, 1, label
                        )
                    else:
                        self.ui.tableWidget.setItem(
                            self.ui.tableWidget.rowCount() - 1, 2, code
                        )
                        self.ui.tableWidget.setCellWidget(
                            self.ui.tableWidget.rowCount() - 1, 3, label
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

    def handlecombo(self):
        self.data = {
            "select": {},
            "NOKIA 105 TA-1557 DS": {
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

    def handlePrint(self):
        try:

            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec() == QtWidgets.QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())

        except Exception as e:
            self.error_handler(f"Error Handel Print: {e}")
        self.ui.lineEdit.setFocus()

    def handlePaintRequest(self, printer):

        doc = ss.Document()
        final_layout = ss.VBoxLayout()
        try:
            model = self.ui.comboBox_model.currentText()
            sku = self.ui.comboBox_sku.currentText()
            color = self.ui.comboBox_color.currentText()
        except Exception as e:
            self.error_handler(f"Error Handel print: {e}")
        if model == "select":
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("هشدار")
            msg_box.setText("لطفا مدل را وارد کنید")
            msg_box.exec()
            return
        try:
            bala_layout = ss.VBoxLayout()

            bala_layout.addSVG(f"./svgs/b{sku}.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_layout.addSVG(f"./svgs/{sku}.svg", alignment=ss.AlignTop | ss.AlignLeft)
            bala_layout.addSVG(f"./svgs/blank3.svg", alignment=ss.AlignTop | ss.AlignLeft)

            full_table_layout = ss.HBoxLayout()
            table1_layout = ss.HBoxLayout()
            table2_layout = ss.HBoxLayout()
            l11 = ss.VBoxLayout()
            l12 = ss.VBoxLayout()
            l13 = ss.VBoxLayout()
            l21 = ss.VBoxLayout()
            l22 = ss.VBoxLayout()
            l23 = ss.VBoxLayout()
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
                        l11.addSVG("./svgs/imei1.svg", alignment=ss.AlignTop | ss.AlignLeft)
                        l11.addSVG(
                            "./svgs/blank4.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )
                    if row < 5:
                        l12.addSVG(path1, alignment=ss.AlignTop | ss.AlignLeft)
                    else:
                        # l3.addSVG("blank1.svg", alignment=ss.AlignTop | ss.AlignLeft)
                        l13.addSVG(path1, alignment=ss.AlignTop | ss.AlignLeft)

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
                        l21.addSVG("./svgs/imei2.svg", alignment=ss.AlignTop | ss.AlignLeft)
                        l21.addSVG(
                            "./svgs/blank4.svg", alignment=ss.AlignTop | ss.AlignLeft
                        )

                    if row < 5:
                        l22.addSVG(path2, alignment=ss.AlignTop | ss.AlignLeft)
                    else:
                        # l2.addSVG("blank1.svg", alignment=ss.AlignTop | ss.AlignLeft)
                        l23.addSVG(path2, alignment=ss.AlignTop | ss.AlignLeft)
        except Exception as e:
            self.error_handler(f"Error output tables: {e}")
        try:
            def create_qr_code(data, filename):
                factory = qrcode.image.svg.SvgImage  # Specify SVG image factory
                qr = qrcode.QRCode(
                    version=1,  # Controls the size of the QR Code: 1 is the smallest
                    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
                    box_size=10,  # Size of each box in pixels
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
            full_qr_layout.addSVG("./svgs/blank1.svg", alignment=ss.AlignTop | ss.AlignLeft)
            full_qr_layout.addSVG(
                "./images/qrcode2.svg", alignment=ss.AlignTop | ss.AlignLeft
            )
        except Exception as e:
            self.error_handler(f"Error creating Qr code: {e}")
        try:
            table1_layout.addLayout(l11)
            table1_layout.addLayout(l13)
            table1_layout.addLayout(l12)
            table2_layout.addLayout(l21)
            table2_layout.addLayout(l22)
            table2_layout.addLayout(l23)
            full_table_layout.addLayout(table1_layout)
            full_table_layout.addLayout(vasat)

            full_table_layout.addLayout(table2_layout)
            final_layout.addLayout(bala_layout)
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
                self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options
            )
            return file_path
        except Exception as e:
            self.error_handler(f"Error save file dialog: {e}")
    def convert_svg_to_pdf(self):
        try:
            input_svg = "qt_api_test.svg"  # Your SVG file
            output_pdf = f'{self.save_file_dialog()}.pdf'  # Get save file path from dialog
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
    widget.show()
    sys.exit(app.exec())
