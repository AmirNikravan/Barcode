# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import rcs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 630)
        MainWindow.setMinimumSize(QSize(450, 450))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/mainicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(188, 188, 188);")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(210, 187, 117);\n"
"    border: 1px solid gray;\n"
"border-radius:5px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: #0078d7; /* Selected item background color */\n"
"}")
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_clear = QToolButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(60, 43))
        self.pushButton_clear.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton_clear.setFont(font1)
        self.pushButton_clear.setToolTipDuration(-1)
        self.pushButton_clear.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/deletetable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clear.setIcon(icon1)
        self.pushButton_clear.setIconSize(QSize(27, 32))
        self.pushButton_clear.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.pushButton_clear)

        self.toolButton_deleterow = QToolButton(self.centralwidget)
        self.toolButton_deleterow.setObjectName(u"toolButton_deleterow")
        self.toolButton_deleterow.setMinimumSize(QSize(61, 36))
        self.toolButton_deleterow.setFont(font1)
        self.toolButton_deleterow.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/deleterow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_deleterow.setIcon(icon2)
        self.toolButton_deleterow.setIconSize(QSize(27, 32))
        self.toolButton_deleterow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.toolButton_deleterow)

        self.horizontalSpacer_2 = QSpacerItem(23, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(132, 21))
        font2 = QFont()
        font2.setFamilies([u"Nirmala UI Semilight"])
        font2.setBold(False)
        self.doubleSpinBox.setFont(font2)
        self.doubleSpinBox.setMaximum(10.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(42, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.comboBox_color = QComboBox(self.centralwidget)
        self.comboBox_color.setObjectName(u"comboBox_color")
        self.comboBox_color.setMinimumSize(QSize(100, 27))

        self.horizontalLayout_2.addWidget(self.comboBox_color)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.comboBox_sku = QComboBox(self.centralwidget)
        self.comboBox_sku.setObjectName(u"comboBox_sku")
        self.comboBox_sku.setMinimumSize(QSize(120, 27))

        self.horizontalLayout_2.addWidget(self.comboBox_sku)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.comboBox_model = QComboBox(self.centralwidget)
        self.comboBox_model.setObjectName(u"comboBox_model")
        self.comboBox_model.setMinimumSize(QSize(69, 27))
        self.comboBox_model.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.comboBox_model)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_scan = QToolButton(self.centralwidget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setMinimumSize(QSize(49, 46))
        self.pushButton_scan.setMaximumSize(QSize(111, 16777215))
        self.pushButton_scan.setFont(font1)
        self.pushButton_scan.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_scan.setIcon(icon3)
        self.pushButton_scan.setIconSize(QSize(31, 36))
        self.pushButton_scan.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.pushButton_scan)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit.setMaxLength(32777)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(67, 86, 92);\n"
"")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 9, -1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet(u"background-color: rgb(215, 226, 255);\n"
"\n"
"border-radius:10px\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_print = QToolButton(self.centralwidget)
        self.toolButton_print.setObjectName(u"toolButton_print")
        self.toolButton_print.setMinimumSize(QSize(80, 0))
        self.toolButton_print.setMaximumSize(QSize(78, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        self.toolButton_print.setFont(font5)
        icon4 = QIcon()
        icon4.addFile(u"Icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_print.setIcon(icon4)
        self.toolButton_print.setIconSize(QSize(35, 54))
        self.toolButton_print.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.toolButton_print)

        self.toolButton_preview = QToolButton(self.centralwidget)
        self.toolButton_preview.setObjectName(u"toolButton_preview")
        self.toolButton_preview.setMinimumSize(QSize(80, 0))
        self.toolButton_preview.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_preview.setIcon(icon5)
        self.toolButton_preview.setIconSize(QSize(35, 54))
        self.toolButton_preview.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.toolButton_preview)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 752, 18))
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
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u062c\u062f\u0648\u0644", None))
        self.toolButton_deleterow.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0633\u0637\u0631", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u"\u062b\u0627\u0646\u06cc\u0647", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u062e\u06cc\u0631:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0646\u06af:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u":SKU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u0644:", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u06a9\u0646", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06a9\u062f: ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u06cc\u0627\u0644", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u06cc\u0627\u0644", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631", None));
        self.toolButton_print.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u06cc\u0646\u062a", None))
        self.toolButton_preview.setText(QCoreApplication.translate("MainWindow", u"\u067e\u06cc\u0634 \u0646\u0645\u0627\u06cc\u0634", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

