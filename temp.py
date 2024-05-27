# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrTVInu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        super.__init__(self)

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 548)
        MainWindow.setMinimumSize(QSize(450, 450))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 234, 237);")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(59, 41, 48);")

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_scan = QPushButton(self.centralwidget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setMinimumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.pushButton_scan.setFont(font1)
        self.pushButton_scan.setStyleSheet(u"QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_scan)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit.setMaxLength(32777)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(67, 86, 92);\n"
"")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 209, 171);\n"
"\n"
"\n"
"border-radius:10px\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(38)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(122)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_print = QPushButton(self.centralwidget)
        self.pushButton_print.setObjectName(u"pushButton_print")
        self.pushButton_print.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        self.pushButton_print.setFont(font3)
        self.pushButton_print.setStyleSheet(u"QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_print)

        self.pushButton_preview = QPushButton(self.centralwidget)
        self.pushButton_preview.setObjectName(u"pushButton_preview")
        self.pushButton_preview.setMinimumSize(QSize(0, 25))
        self.pushButton_preview.setFont(font3)
        self.pushButton_preview.setStyleSheet(u"QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_preview)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 604, 19))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMEI SCANNER", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0647", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06a9\u062f : ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u06cc\u0627\u0644", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631", None));
        self.pushButton_print.setText(QCoreApplication.translate("MainWindow", u"\u0686\u0627\u067e", None))
        self.pushButton_preview.setText(QCoreApplication.translate("MainWindow", u"\u067e\u06cc\u0634 \u0646\u0645\u0627\u06cc\u0634", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
import sys
app = QApplication(sys.argv)
window = Ui_MainWindow(
)
window.show()
sys.exit(app.exec())