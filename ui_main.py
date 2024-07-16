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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
import rcs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 738)
        MainWindow.setMinimumSize(QSize(450, 450))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/mainicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.user_info = QWidget(self.centralwidget)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.user_info.setFont(font)
        self.horizontalLayout_9 = QHBoxLayout(self.user_info)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_time = QLabel(self.user_info)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_time)

        self.label_date = QLabel(self.user_info)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_date)

        self.label_day = QLabel(self.user_info)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_day)

        self.horizontalSpacer_12 = QSpacerItem(596, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.toolButton_exit = QToolButton(self.user_info)
        self.toolButton_exit.setObjectName(u"toolButton_exit")
        self.toolButton_exit.setMinimumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.toolButton_exit.setFont(font1)
        self.toolButton_exit.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                      ")

        self.horizontalLayout_9.addWidget(self.toolButton_exit)

        self.label_name = QLabel(self.user_info)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(60, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_name.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_name)

        self.label_7 = QLabel(self.user_info)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_7.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.user_info)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(231, 235, 255);")
        self.barcode = QWidget()
        self.barcode.setObjectName(u"barcode")
        self.barcode.setStyleSheet(u"QToolButton{border-radius:11px;\n"
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
"    selection-background-color:red; /* Selected item background color */\n"
"}\n"
"                    ")
        self.verticalLayout = QVBoxLayout(self.barcode)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.barcode)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(59, 41, 48);")

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.barcode)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_clear = QToolButton(self.barcode)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(60, 43))
        self.pushButton_clear.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_clear.setFont(font2)
        self.pushButton_clear.setToolTipDuration(-1)
        self.pushButton_clear.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/deletetable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clear.setIcon(icon1)
        self.pushButton_clear.setIconSize(QSize(27, 32))
        self.pushButton_clear.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.pushButton_clear)

        self.toolButton_deleterow = QToolButton(self.barcode)
        self.toolButton_deleterow.setObjectName(u"toolButton_deleterow")
        self.toolButton_deleterow.setMinimumSize(QSize(61, 36))
        self.toolButton_deleterow.setFont(font2)
        self.toolButton_deleterow.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/deleterow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_deleterow.setIcon(icon2)
        self.toolButton_deleterow.setIconSize(QSize(27, 32))
        self.toolButton_deleterow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.toolButton_deleterow)

        self.horizontalSpacer_2 = QSpacerItem(23, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox = QDoubleSpinBox(self.barcode)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(132, 21))
        font5 = QFont()
        font5.setFamilies([u"Nirmala UI Semilight"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.doubleSpinBox.setFont(font5)
        self.doubleSpinBox.setMaximum(10.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)

        self.label_3 = QLabel(self.barcode)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(42, 16777215))
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.comboBox_color = QComboBox(self.barcode)
        self.comboBox_color.setObjectName(u"comboBox_color")
        self.comboBox_color.setMinimumSize(QSize(104, 27))

        self.horizontalLayout_2.addWidget(self.comboBox_color)

        self.label_5 = QLabel(self.barcode)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.comboBox_sku = QComboBox(self.barcode)
        self.comboBox_sku.setObjectName(u"comboBox_sku")
        self.comboBox_sku.setMinimumSize(QSize(120, 27))

        self.horizontalLayout_2.addWidget(self.comboBox_sku)

        self.label_6 = QLabel(self.barcode)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.comboBox_model = QComboBox(self.barcode)
        self.comboBox_model.setObjectName(u"comboBox_model")
        self.comboBox_model.setMinimumSize(QSize(76, 27))
        self.comboBox_model.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.comboBox_model)

        self.label_4 = QLabel(self.barcode)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_scan = QToolButton(self.barcode)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setMinimumSize(QSize(49, 46))
        self.pushButton_scan.setMaximumSize(QSize(111, 16777215))
        self.pushButton_scan.setFont(font2)
        self.pushButton_scan.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_scan.setIcon(icon3)
        self.pushButton_scan.setIconSize(QSize(31, 36))
        self.pushButton_scan.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.pushButton_scan)

        self.lineEdit = QLineEdit(self.barcode)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"                              ")
        self.lineEdit.setMaxLength(32777)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.barcode)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(18)
        font6.setBold(True)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(67, 86, 92);\n"
"                              ")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.barcode)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(87, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.tableWidget = QTableWidget(self.barcode)
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
"                              ")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(275)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.horizontalSpacer_7 = QSpacerItem(135, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_print = QToolButton(self.barcode)
        self.toolButton_print.setObjectName(u"toolButton_print")
        self.toolButton_print.setMinimumSize(QSize(80, 0))
        self.toolButton_print.setMaximumSize(QSize(78, 16777215))
        self.toolButton_print.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u"Icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_print.setIcon(icon4)
        self.toolButton_print.setIconSize(QSize(35, 54))
        self.toolButton_print.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.toolButton_print)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.barcode)
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.users.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.users)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.users)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_8)

        self.line_3 = QFrame(self.users)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 15))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_9 = QLabel(self.users)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_9)

        self.tableWidget_list_users = QTableWidget(self.users)
        if (self.tableWidget_list_users.columnCount() < 5):
            self.tableWidget_list_users.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_list_users.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_list_users.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_list_users.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_list_users.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_list_users.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget_list_users.setObjectName(u"tableWidget_list_users")
        self.tableWidget_list_users.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_list_users.setStyleSheet(u"background-color: rgb(195, 188, 219);")
        self.tableWidget_list_users.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_list_users.horizontalHeader().setDefaultSectionSize(192)

        self.verticalLayout_5.addWidget(self.tableWidget_list_users)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.toolButton_deleteuser = QToolButton(self.users)
        self.toolButton_deleteuser.setObjectName(u"toolButton_deleteuser")
        self.toolButton_deleteuser.setMinimumSize(QSize(0, 34))
        self.toolButton_deleteuser.setFont(font3)
        self.toolButton_deleteuser.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"background-color: rgb(195, 152, 255);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")

        self.horizontalLayout_5.addWidget(self.toolButton_deleteuser)

        self.toolButton_newuser = QToolButton(self.users)
        self.toolButton_newuser.setObjectName(u"toolButton_newuser")
        self.toolButton_newuser.setMinimumSize(QSize(0, 34))
        self.toolButton_newuser.setFont(font3)
        self.toolButton_newuser.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"background-color: rgb(195, 152, 255);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")

        self.horizontalLayout_5.addWidget(self.toolButton_newuser)

        self.toolButton_edituser = QToolButton(self.users)
        self.toolButton_edituser.setObjectName(u"toolButton_edituser")
        self.toolButton_edituser.setMinimumSize(QSize(0, 36))
        self.toolButton_edituser.setFont(font3)
        self.toolButton_edituser.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"background-color: rgb(195, 152, 255);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")

        self.horizontalLayout_5.addWidget(self.toolButton_edituser)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.label_10 = QLabel(self.users)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.tableWidget_3 = QTableWidget(self.users)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.tableWidget_3)

        self.toolButton_clearstatus = QToolButton(self.users)
        self.toolButton_clearstatus.setObjectName(u"toolButton_clearstatus")

        self.verticalLayout_5.addWidget(self.toolButton_clearstatus)

        self.stackedWidget.addWidget(self.users)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.verticalLayout_7 = QVBoxLayout(self.database)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.toolButton_dbcheck = QToolButton(self.database)
        self.toolButton_dbcheck.setObjectName(u"toolButton_dbcheck")
        self.toolButton_dbcheck.setMinimumSize(QSize(23, 29))
        self.toolButton_dbcheck.setFont(font2)
        self.toolButton_dbcheck.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")

        self.horizontalLayout_14.addWidget(self.toolButton_dbcheck)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.label_11 = QLabel(self.database)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.horizontalLayout_14.addWidget(self.label_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.line_4 = QFrame(self.database)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.label_12 = QLabel(self.database)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.tableWidget_excel = QTableWidget(self.database)
        if (self.tableWidget_excel.columnCount() < 2):
            self.tableWidget_excel.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_excel.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_excel.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.tableWidget_excel.setObjectName(u"tableWidget_excel")
        self.tableWidget_excel.setMinimumSize(QSize(0, 0))
        self.tableWidget_excel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget_excel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_excel.horizontalHeader().setDefaultSectionSize(127)

        self.horizontalLayout_8.addWidget(self.tableWidget_excel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_excel_status = QLabel(self.database)
        self.label_excel_status.setObjectName(u"label_excel_status")
        self.label_excel_status.setMinimumSize(QSize(50, 0))
        self.label_excel_status.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_excel_status)

        self.label_14 = QLabel(self.database)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_count = QLabel(self.database)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setFont(font2)
        self.label_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_count)

        self.label_15 = QLabel(self.database)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.toolButton_inputexcel = QToolButton(self.database)
        self.toolButton_inputexcel.setObjectName(u"toolButton_inputexcel")
        self.toolButton_inputexcel.setMinimumSize(QSize(49, 36))
        self.toolButton_inputexcel.setFont(font2)
        self.toolButton_inputexcel.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/icons8-input-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_inputexcel.setIcon(icon5)
        self.toolButton_inputexcel.setIconSize(QSize(27, 31))
        self.toolButton_inputexcel.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_7.addWidget(self.toolButton_inputexcel)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.label_13 = QLabel(self.database)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.label_db_status = QLabel(self.database)
        self.label_db_status.setObjectName(u"label_db_status")
        self.label_db_status.setMinimumSize(QSize(71, 0))
        self.label_db_status.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_db_status)

        self.label_16 = QLabel(self.database)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_16)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.toolButton_exportdb = QToolButton(self.database)
        self.toolButton_exportdb.setObjectName(u"toolButton_exportdb")
        self.toolButton_exportdb.setMinimumSize(QSize(49, 36))
        self.toolButton_exportdb.setFont(font2)
        self.toolButton_exportdb.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")
        icon6 = QIcon()
        icon6.addFile(u"Icons/icons8-export-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_exportdb.setIcon(icon6)
        self.toolButton_exportdb.setIconSize(QSize(27, 31))
        self.toolButton_exportdb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_6.addWidget(self.toolButton_exportdb)

        self.toolButton_inputdb = QToolButton(self.database)
        self.toolButton_inputdb.setObjectName(u"toolButton_inputdb")
        self.toolButton_inputdb.setEnabled(True)
        self.toolButton_inputdb.setMinimumSize(QSize(49, 36))
        self.toolButton_inputdb.setFont(font2)
        self.toolButton_inputdb.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                              ")
        self.toolButton_inputdb.setIcon(icon5)
        self.toolButton_inputdb.setIconSize(QSize(27, 31))
        self.toolButton_inputdb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_6.addWidget(self.toolButton_inputdb)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.database)
        self.account = QWidget()
        self.account.setObjectName(u"account")
        self.verticalLayout_9 = QVBoxLayout(self.account)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.account)
        self.label_17.setObjectName(u"label_17")
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(20)
        self.label_17.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_17)

        self.line_5 = QFrame(self.account)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.groupBox = QGroupBox(self.account)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 232))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(455, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.label_accname = QLabel(self.groupBox)
        self.label_accname.setObjectName(u"label_accname")

        self.horizontalLayout_15.addWidget(self.label_accname)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(19, 16777215))

        self.horizontalLayout_15.addWidget(self.label_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_16 = QSpacerItem(406, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)

        self.label_acclastname = QLabel(self.groupBox)
        self.label_acclastname.setObjectName(u"label_acclastname")

        self.horizontalLayout_16.addWidget(self.label_acclastname)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_16.addWidget(self.label_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_17 = QSpacerItem(359, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.label_accusername = QLabel(self.groupBox)
        self.label_accusername.setObjectName(u"label_accusername")
        self.label_accusername.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_accusername)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(62, 16777215))

        self.horizontalLayout_17.addWidget(self.label_22)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(324, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.label_acctotal = QLabel(self.groupBox)
        self.label_acctotal.setObjectName(u"label_acctotal")
        self.label_acctotal.setCursor(QCursor(Qt.ArrowCursor))
        self.label_acctotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_acctotal)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(6, 0))
        self.label_26.setMaximumSize(QSize(128, 16777215))

        self.horizontalLayout_19.addWidget(self.label_26)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_20 = QSpacerItem(75, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.label_accperm = QLabel(self.groupBox)
        self.label_accperm.setObjectName(u"label_accperm")

        self.horizontalLayout_20.addWidget(self.label_accperm)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))
        self.label_28.setMaximumSize(QSize(49, 16777215))

        self.horizontalLayout_20.addWidget(self.label_28)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.label_30 = QLabel(self.account)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_9.addWidget(self.label_30)

        self.tableWidget_history = QTableWidget(self.account)
        if (self.tableWidget_history.columnCount() < 3):
            self.tableWidget_history.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_history.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.tableWidget_history.setObjectName(u"tableWidget_history")
        self.tableWidget_history.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget_history.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget_history.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_history.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_history.setTextElideMode(Qt.ElideRight)
        self.tableWidget_history.horizontalHeader().setVisible(False)
        self.tableWidget_history.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_history.horizontalHeader().setMinimumSectionSize(43)
        self.tableWidget_history.horizontalHeader().setDefaultSectionSize(207)
        self.tableWidget_history.verticalHeader().setVisible(False)
        self.tableWidget_history.verticalHeader().setDefaultSectionSize(76)

        self.verticalLayout_9.addWidget(self.tableWidget_history)

        self.stackedWidget.addWidget(self.account)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_10 = QVBoxLayout(self.report)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_19 = QLabel(self.report)
        self.label_19.setObjectName(u"label_19")
        font8 = QFont()
        font8.setPointSize(14)
        self.label_19.setFont(font8)

        self.verticalLayout_10.addWidget(self.label_19)

        self.line_6 = QFrame(self.report)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_6)

        self.tabWidget = QTabWidget(self.report)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.barcode_report = QWidget()
        self.barcode_report.setObjectName(u"barcode_report")
        self.verticalLayout_12 = QVBoxLayout(self.barcode_report)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_21 = QLabel(self.barcode_report)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_23.addWidget(self.label_21)

        self.lineEdit_barrep = QLineEdit(self.barcode_report)
        self.lineEdit_barrep.setObjectName(u"lineEdit_barrep")
        self.lineEdit_barrep.setMaxLength(15)

        self.horizontalLayout_23.addWidget(self.lineEdit_barrep)

        self.label_23 = QLabel(self.barcode_report)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_23.addWidget(self.label_23)

        self.comboBox_barrep_user = QComboBox(self.barcode_report)
        self.comboBox_barrep_user.setObjectName(u"comboBox_barrep_user")
        self.comboBox_barrep_user.setMinimumSize(QSize(118, 0))

        self.horizontalLayout_23.addWidget(self.comboBox_barrep_user)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_24 = QLabel(self.barcode_report)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(55, 0))

        self.horizontalLayout_21.addWidget(self.label_24)

        self.comboBox_barrep_start_day = QComboBox(self.barcode_report)
        self.comboBox_barrep_start_day.setObjectName(u"comboBox_barrep_start_day")

        self.horizontalLayout_21.addWidget(self.comboBox_barrep_start_day)

        self.comboBox_barrep_start_month = QComboBox(self.barcode_report)
        self.comboBox_barrep_start_month.setObjectName(u"comboBox_barrep_start_month")

        self.horizontalLayout_21.addWidget(self.comboBox_barrep_start_month)

        self.comboBox_barrep_start_year = QComboBox(self.barcode_report)
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.addItem("")
        self.comboBox_barrep_start_year.setObjectName(u"comboBox_barrep_start_year")

        self.horizontalLayout_21.addWidget(self.comboBox_barrep_start_year)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_27 = QLabel(self.barcode_report)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(55, 0))

        self.horizontalLayout_22.addWidget(self.label_27)

        self.comboBox_barrep_end_day = QComboBox(self.barcode_report)
        self.comboBox_barrep_end_day.setObjectName(u"comboBox_barrep_end_day")

        self.horizontalLayout_22.addWidget(self.comboBox_barrep_end_day)

        self.comboBox_barrep_end_month = QComboBox(self.barcode_report)
        self.comboBox_barrep_end_month.setObjectName(u"comboBox_barrep_end_month")

        self.horizontalLayout_22.addWidget(self.comboBox_barrep_end_month)

        self.comboBox_barrep_end_year = QComboBox(self.barcode_report)
        self.comboBox_barrep_end_year.setObjectName(u"comboBox_barrep_end_year")

        self.horizontalLayout_22.addWidget(self.comboBox_barrep_end_year)


        self.verticalLayout_11.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_24.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_21)

        self.toolButton_barrep_search = QToolButton(self.barcode_report)
        self.toolButton_barrep_search.setObjectName(u"toolButton_barrep_search")

        self.horizontalLayout_25.addWidget(self.toolButton_barrep_search)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_18)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.tableWidget_report_barcode = QTableWidget(self.barcode_report)
        self.tableWidget_report_barcode.setObjectName(u"tableWidget_report_barcode")
        self.tableWidget_report_barcode.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget_report_barcode.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_12.addWidget(self.tableWidget_report_barcode)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.toolButton_barrep_print = QToolButton(self.barcode_report)
        self.toolButton_barrep_print.setObjectName(u"toolButton_barrep_print")
        self.toolButton_barrep_print.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")

        self.horizontalLayout_18.addWidget(self.toolButton_barrep_print)

        self.toolButton_barrep_excel = QToolButton(self.barcode_report)
        self.toolButton_barrep_excel.setObjectName(u"toolButton_barrep_excel")
        self.toolButton_barrep_excel.setMinimumSize(QSize(0, 0))
        self.toolButton_barrep_excel.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")

        self.horizontalLayout_18.addWidget(self.toolButton_barrep_excel)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)

        self.tabWidget.addTab(self.barcode_report, "")
        self.users_report = QWidget()
        self.users_report.setObjectName(u"users_report")
        self.tabWidget.addTab(self.users_report, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.report)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.navigation = QWidget(self.centralwidget)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setMinimumSize(QSize(72, 0))
        self.navigation.setStyleSheet(u"background-color: rgb(252, 224, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.navigation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolButton_navigscan = QToolButton(self.navigation)
        self.toolButton_navigscan.setObjectName(u"toolButton_navigscan")
        self.toolButton_navigscan.setMinimumSize(QSize(54, 47))
        self.toolButton_navigscan.setFont(font3)
        self.toolButton_navigscan.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/icons8-barcode-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_navigscan.setIcon(icon7)
        self.toolButton_navigscan.setIconSize(QSize(34, 33))
        self.toolButton_navigscan.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_navigscan)

        self.toolButton_navigbox = QToolButton(self.navigation)
        self.toolButton_navigbox.setObjectName(u"toolButton_navigbox")
        self.toolButton_navigbox.setEnabled(False)
        self.toolButton_navigbox.setMinimumSize(QSize(54, 59))
        self.toolButton_navigbox.setFont(font3)
        self.toolButton_navigbox.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/icons8-box-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_navigbox.setIcon(icon8)
        self.toolButton_navigbox.setIconSize(QSize(31, 34))
        self.toolButton_navigbox.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_navigbox)

        self.toolButton_navigdatabase = QToolButton(self.navigation)
        self.toolButton_navigdatabase.setObjectName(u"toolButton_navigdatabase")
        self.toolButton_navigdatabase.setMinimumSize(QSize(54, 59))
        self.toolButton_navigdatabase.setFont(font3)
        self.toolButton_navigdatabase.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/icons8-database-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_navigdatabase.setIcon(icon9)
        self.toolButton_navigdatabase.setIconSize(QSize(34, 37))
        self.toolButton_navigdatabase.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_navigdatabase)

        self.toolButton_naviguser = QToolButton(self.navigation)
        self.toolButton_naviguser.setObjectName(u"toolButton_naviguser")
        self.toolButton_naviguser.setMinimumSize(QSize(54, 59))
        self.toolButton_naviguser.setFont(font3)
        self.toolButton_naviguser.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/icons8-user-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_naviguser.setIcon(icon10)
        self.toolButton_naviguser.setIconSize(QSize(31, 34))
        self.toolButton_naviguser.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_naviguser)

        self.toolButton_navigreport = QToolButton(self.navigation)
        self.toolButton_navigreport.setObjectName(u"toolButton_navigreport")
        self.toolButton_navigreport.setEnabled(True)
        self.toolButton_navigreport.setMinimumSize(QSize(54, 59))
        self.toolButton_navigreport.setFont(font3)
        self.toolButton_navigreport.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/icons8-report-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_navigreport.setIcon(icon11)
        self.toolButton_navigreport.setIconSize(QSize(31, 34))
        self.toolButton_navigreport.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_navigreport)

        self.toolButton_navigaccount = QToolButton(self.navigation)
        self.toolButton_navigaccount.setObjectName(u"toolButton_navigaccount")
        self.toolButton_navigaccount.setEnabled(True)
        self.toolButton_navigaccount.setMinimumSize(QSize(54, 59))
        self.toolButton_navigaccount.setFont(font3)
        self.toolButton_navigaccount.setStyleSheet(u"QToolButton{border-radius:11px;\n"
"\n"
"\n"
"	background-color: rgb(132, 171, 108);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"\n"
"                        ")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/icons8-account-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_navigaccount.setIcon(icon12)
        self.toolButton_navigaccount.setIconSize(QSize(31, 34))
        self.toolButton_navigaccount.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_navigaccount)


        self.horizontalLayout_4.addWidget(self.navigation)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 756, 18))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628\u0627\u0631\u0647", None))
        self.label_time.setText("")
        self.label_date.setText("")
        self.label_day.setText("")
        self.toolButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c", None))
        self.label_name.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631 :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u06a9\u0646 \u0628\u0627\u0631\u06a9\u062f", None))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0633\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        ___qtablewidgetitem4 = self.tableWidget_list_users.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645", None));
        ___qtablewidgetitem5 = self.tableWidget_list_users.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None));
        ___qtablewidgetitem6 = self.tableWidget_list_users.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem7 = self.tableWidget_list_users.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem8 = self.tableWidget_list_users.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0648\u0632 \u0647\u0627", None));
        self.toolButton_deleteuser.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u06a9\u0627\u0631\u0628\u0631", None))
        self.toolButton_newuser.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f", None))
        self.toolButton_edituser.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0631", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.toolButton_clearstatus.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646 \u062c\u062f\u0648\u0644", None))
        self.toolButton_dbcheck.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0631\u0631\u0633\u06cc \u062f\u06cc\u062a\u0627\u0628\u06cc\u0633 \u0647\u0627", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u062a\u0627\u0628\u06cc\u0633", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u062a\u0627\u0628\u06cc\u0633 IMEI", None))
        ___qtablewidgetitem9 = self.tableWidget_excel.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"IMEI1", None));
        ___qtablewidgetitem10 = self.tableWidget_excel.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"IMEI2", None));
        self.label_excel_status.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a :", None))
        self.label_count.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f IMEI :", None))
        self.toolButton_inputexcel.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u062a\u0627\u0628\u06cc\u0633 \u0628\u0631\u0646\u0627\u0645\u0647", None))
        self.label_db_status.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a :", None))
        self.toolButton_exportdb.setText(QCoreApplication.translate("MainWindow", u"export", None))
        self.toolButton_inputdb.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0627\u06a9\u0627\u0646\u062a \u0645\u0646", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0634\u062e\u0635\u06cc", None))
        self.label_accname.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_acclastname.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc:", None))
        self.label_accusername.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.label_acctotal.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06a9\u062f \u0647\u0627\u06cc \u0627\u0633\u06a9\u0646 \u0634\u062f\u0647:", None))
        self.label_accperm.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0648\u0632 \u0647\u0627:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e\u0686\u0647 \u0639\u0645\u0644\u06a9\u0631\u062f", None))
        ___qtablewidgetitem11 = self.tableWidget_history.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e", None));
        ___qtablewidgetitem12 = self.tableWidget_history.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0632\u0645\u0627\u0646", None));
        ___qtablewidgetitem13 = self.tableWidget_history.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0639\u0627\u0644\u06cc\u062a", None));
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u06af\u06cc\u0631\u06cc", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0631\u06cc\u0627\u0644 \u0628\u0627\u0631\u06a9\u062f :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e :     \u0627\u0632", None))
        self.comboBox_barrep_start_year.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644", None))
        self.comboBox_barrep_start_year.setItemText(1, QCoreApplication.translate("MainWindow", u"1403", None))
        self.comboBox_barrep_start_year.setItemText(2, QCoreApplication.translate("MainWindow", u"1404", None))
        self.comboBox_barrep_start_year.setItemText(3, QCoreApplication.translate("MainWindow", u"1405", None))
        self.comboBox_barrep_start_year.setItemText(4, QCoreApplication.translate("MainWindow", u"1406", None))
        self.comboBox_barrep_start_year.setItemText(5, QCoreApplication.translate("MainWindow", u"1407", None))
        self.comboBox_barrep_start_year.setItemText(6, QCoreApplication.translate("MainWindow", u"1408", None))
        self.comboBox_barrep_start_year.setItemText(7, QCoreApplication.translate("MainWindow", u"1409", None))
        self.comboBox_barrep_start_year.setItemText(8, QCoreApplication.translate("MainWindow", u"1410", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e :     \u062a\u0627", None))
        self.toolButton_barrep_search.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a \u0648 \u062c\u0648", None))
        self.toolButton_barrep_print.setText(QCoreApplication.translate("MainWindow", u"print", None))
        self.toolButton_barrep_excel.setText(QCoreApplication.translate("MainWindow", u"excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.barcode_report), QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06a9\u062f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.users_report), QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.toolButton_navigscan.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u06a9\u0646", None))
        self.toolButton_navigbox.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0639\u0628\u0647", None))
        self.toolButton_navigdatabase.setText(QCoreApplication.translate("MainWindow", u"\u062f\u06cc\u062a\u0627\u0628\u06cc\u0633", None))
        self.toolButton_naviguser.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.toolButton_navigreport.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634", None))
        self.toolButton_navigaccount.setText(QCoreApplication.translate("MainWindow", u"\u0627\u06a9\u0627\u0646\u062a", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u06a9\u0645\u06a9", None))
    # retranslateUi

