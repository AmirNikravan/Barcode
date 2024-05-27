import sys
import os
import shutil
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
import random
from PyQt6.QtWidgets import QMainWindow
import os
from PyQt6.QtSql import QSqlQueryModel
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtPrintSupport import *
from PyQt6 import QtPrintSupport, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices,QTextImageFormat
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter
from PyQt6 import QtCore, QtGui, QtWidgets
# import qrcode
import sqlite3
import datetime
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 548)
        MainWindow.setMinimumSize(QtCore.QSize(450, 450))
        MainWindow.setStyleSheet("background-color: rgb(255, 234, 237);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(59, 41, 48);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_scan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_scan.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_scan.setFont(font)
        self.pushButton_scan.setStyleSheet("QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.horizontalLayout.addWidget(self.pushButton_scan)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.lineEdit.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit.setMaxLength(32777)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:5px;\n"
"color: rgb(67, 86, 92);\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 209, 171);\n"
"\n"
"\n"
"border-radius:10px\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(122)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(38)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_print = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_print.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setStyleSheet("QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_2.addWidget(self.pushButton_print)
        self.pushButton_preview = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_preview.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_preview.setFont(font)
        self.pushButton_preview.setStyleSheet("QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout_2.addWidget(self.pushButton_preview)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.pushButton_scan.clicked.connect(self.barcode_scan)
        self.pushButton_print.clicked.connect(self.handlePrint)
        self.actionAbout.triggered.connect(self.showAboutMessageBox)
        self.pushButton_preview.clicked.connect(self.handlePreview)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def showAboutMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Developer : Amir Hossein Nikravan")
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "IMEI SCANNER"))
        self.pushButton_scan.setText(_translate("MainWindow", "اضافه"))
        self.label_2.setText(_translate("MainWindow", "بارکد : "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "سریال"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "تصویر"))
        self.pushButton_print.setText(_translate("MainWindow", "چاپ"))
        self.pushButton_preview.setText(_translate("MainWindow", "پیش نمایش"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    def barcode_scan(self):
        # print(self.lineEdit.text())
        try:
            self.barcode_serial = self.lineEdit.text()
            if self.barcode_serial:
                with open(f".\\images\\{self.barcode_serial}.jpeg", "wb") as f:
                    Code128(f"{self.barcode_serial}", writer=ImageWriter()).write(f)

                pic = QtGui.QPixmap(f".\\images\\{self.barcode_serial}.jpeg")

                label = QtWidgets.QLabel()
                label.width = 100
                label.height = 100
                label.setPixmap(pic)

                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                code = QTableWidgetItem(f"{self.barcode_serial}")
                # barcode = QTableWidgetItem(f"{self.number}")
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, code)
                # self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1,  barcode)
                self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 1, label)
                self.tableWidget.setColumnWidth(1, 200)
                self.tableWidget.setRowHeight(self.tableWidget.rowCount() - 1, 220)
        except Exception as e:
            print(f"Error inserting data into table: {e}")
    def handlePrint(self):
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec() == QtWidgets.QDialog.accepted:
                self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()

        # Create QTextCursor
        cursor = QtGui.QTextCursor(document)

        # Calculate total number of barcodes
        total_barcodes = self.tableWidget.rowCount()

        # Display 10 barcodes per page
        barcodes_per_page = 10

        # Calculate total number of pages needed
        total_pages = (total_barcodes + barcodes_per_page - 1) // barcodes_per_page

        # Calculate number of rows and columns for the grid
        num_rows = 5
        num_cols = 2

        # Iterate through each page
        for page_num in range(total_pages):
            # Start a new page
            cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)

            cursor.insertBlock()

            # Calculate the range of barcodes to print on this page
            start_index = page_num * barcodes_per_page
            end_index = min(start_index + barcodes_per_page, total_barcodes)

            # Calculate the number of rows and columns needed for this batch of barcodes
            num_rows_batch = (end_index - start_index + num_cols - 1) // num_cols
            num_cols_batch = min(num_cols, end_index - start_index)

            # Iterate through the rows
            for row_index in range(num_rows_batch):
                # Create a table row
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)

                cursor.insertBlock()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.EndOfBlock)

                cursor.insertText('\n')

                # Iterate through the columns
                for col_index in range(num_cols_batch):
                    barcode_index = start_index + row_index * num_cols_batch + col_index
                    if barcode_index < end_index:
                        # Get the text of the barcode
                        item_text = self.tableWidget.item(barcode_index, 0).text()

                        # Generate barcode image
                        with open(f".\\images\\{item_text}.jpeg", "wb") as f:
                            Code128(item_text, writer=ImageWriter()).write(f)

                        # Load the barcode image as QPixmap
                        pic = QtGui.QPixmap(f".\\images\\{item_text}.jpeg")

                        # Convert QPixmap to QTextImageFormat
                        image_format = QtGui.QTextImageFormat()
                        image_format.setWidth(310)
                        image_format.setHeight(200)
                        image_format.setName(f".\\images\\{item_text}.jpeg")  # Set the image file path

                        # Insert the image into the QTextDocument
                        cursor.insertImage(image_format)

            # Move to the next page
            if page_num < total_pages - 1:
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)

                cursor.insertBlock()

        # Print the document
        printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.NativeFormat)

        document.print(printer)
def delete_folder_on_exit(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder removed successfully: {folder_path}")
    except OSError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    # Create the images folder if it doesn't exist
    if not os.path.exists(".\\images"):
        os.makedirs(".\\images")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Connect the folder deletion function to app.aboutToQuit signal
    folder_path = ".\\images"
    app.aboutToQuit.connect(lambda: delete_folder_on_exit(folder_path))

    sys.exit(app.exec())
