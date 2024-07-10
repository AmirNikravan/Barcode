# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(431, 350)
        Dialog.setStyleSheet("background-color: rgb(135, 183, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_username = QLineEdit(Dialog)
        self.lineEdit_username.setObjectName("lineEdit_username")

        self.horizontalLayout.addWidget(self.lineEdit_username)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        font1 = QFont()
        font1.setFamilies(["Arial"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_pass = QLineEdit(Dialog)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_pass)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_cancel = QToolButton(Dialog)
        self.toolButton_cancel.setObjectName("toolButton_cancel")
        self.toolButton_cancel.setMinimumSize(QSize(45, 45))
        self.toolButton_cancel.setFont(font1)
        self.toolButton_cancel.setStyleSheet(
            "QToolButton{border-radius:11px;\n"
            "\n"
            "\n"
            "	background-color: rgb(132, 171, 108);\n"
            "}\n"
            "QToolButton:hover{\n"
            "background-color: rgb(255, 166, 139);\n"
            "}\n"
            "\n"
            ""
        )

        self.horizontalLayout_3.addWidget(self.toolButton_cancel)

        self.toolButton_enter = QToolButton(Dialog)
        self.toolButton_enter.setObjectName("toolButton_enter")
        self.toolButton_enter.setMinimumSize(QSize(45, 45))
        self.toolButton_enter.setFont(font1)
        self.toolButton_enter.setStyleSheet(
            "QToolButton{border-radius:11px;\n"
            "\n"
            "\n"
            "	background-color: rgb(132, 171, 108);\n"
            "}\n"
            "QToolButton:hover{\n"
            "background-color: rgb(255, 166, 139);\n"
            "}\n"
            "\n"
            ""
        )

        self.horizontalLayout_3.addWidget(self.toolButton_enter)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0648\u0631\u0648\u062f \u0628\u0647 \u0633\u06cc\u0633\u062a\u0645",
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog", "\u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None
            )
        )
        self.toolButton_cancel.setText(
            QCoreApplication.translate("Dialog", "\u0644\u063a\u0648", None)
        )
        self.toolButton_enter.setText(
            QCoreApplication.translate("Dialog", "\u0648\u0631\u0648\u062f", None)
        )

    # retranslateUi
