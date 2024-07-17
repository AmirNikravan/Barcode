# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import loginres_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(446, 382)
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"IRANSansXFaNum"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit_username = QLineEdit(Dialog)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(0, 40))
        self.lineEdit_username.setStyleSheet(u"background-color:rgb(233, 234, 234);\n"
"font: 87 10pt \"IRANSansXFaNum Black\";\n"
"color: rgb(31, 68, 142);\n"
"border-radius: 10px;")
        self.lineEdit_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_username.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_username)

        self.lineEdit_pass = QLineEdit(Dialog)
        self.lineEdit_pass.setObjectName(u"lineEdit_pass")
        self.lineEdit_pass.setMinimumSize(QSize(0, 40))
        self.lineEdit_pass.setStyleSheet(u"background-color:rgb(233, 234, 234);\n"
"font: 87 10pt \"IRANSansXFaNum Black\";\n"
"color: rgb(31, 68, 142);\n"
"border-radius: 10px;")
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)
        self.lineEdit_pass.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_pass.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_pass)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(8, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.toolButton_cancel = QToolButton(Dialog)
        self.toolButton_cancel.setObjectName(u"toolButton_cancel")
        self.toolButton_cancel.setMinimumSize(QSize(137, 45))
        font2 = QFont()
        font2.setFamilies([u"IRANSansXFaNum Black"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.toolButton_cancel.setFont(font2)
        self.toolButton_cancel.setStyleSheet(u"\n"
"QToolButton{border-radius:11px;\n"
"color: rgb(233, 234, 234);\n"
"font: 87 10pt \"IRANSansXFaNum Black\";\n"
"background-color:rgb(31, 68, 142);\n"
"}\n"
"QToolButton:hover{\n"
"color: rgb(233, 234, 234);\n"
"\n"
"background-color:rgb(7, 21, 52);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.toolButton_cancel)

        self.horizontalSpacer_5 = QSpacerItem(53, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.toolButton_enter = QToolButton(Dialog)
        self.toolButton_enter.setObjectName(u"toolButton_enter")
        self.toolButton_enter.setMinimumSize(QSize(137, 45))
        self.toolButton_enter.setFont(font2)
        self.toolButton_enter.setStyleSheet(u"\n"
"QToolButton{border-radius:11px;\n"
"color: rgb(233, 234, 234);\n"
"font: 87 10pt \"IRANSansXFaNum Black\";\n"
"background-color:rgb(31, 68, 142);\n"
"}\n"
"QToolButton:hover{\n"
"color: rgb(233, 234, 234);\n"
"\n"
"background-color:rgb(7, 21, 52);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.toolButton_enter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0648\u0631\u0648\u062f \u0628\u0647 \u0633\u06cc\u0633\u062a\u0645", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.lineEdit_pass.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.toolButton_cancel.setText(QCoreApplication.translate("Dialog", u"\u0644\u063a\u0648", None))
        self.toolButton_enter.setText(QCoreApplication.translate("Dialog", u"\u0648\u0631\u0648\u062f", None))
    # retranslateUi

