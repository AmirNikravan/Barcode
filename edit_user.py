# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user.ui'
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
    QCheckBox,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(496, 428)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(Dialog)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_usersname = QLineEdit(Dialog)
        self.lineEdit_usersname.setObjectName("lineEdit_usersname")

        self.horizontalLayout.addWidget(self.lineEdit_usersname)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_userslastname = QLineEdit(Dialog)
        self.lineEdit_userslastname.setObjectName("lineEdit_userslastname")

        self.horizontalLayout_2.addWidget(self.lineEdit_userslastname)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_username = QLineEdit(Dialog)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_username.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit_username)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_password = QLineEdit(Dialog)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.horizontalLayout_4.addWidget(self.lineEdit_password)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_db = QCheckBox(Dialog)
        self.checkBox_db.setObjectName("checkBox_db")
        font2 = QFont()
        font2.setPointSize(9)
        self.checkBox_db.setFont(font2)

        self.horizontalLayout_5.addWidget(self.checkBox_db)

        self.checkBox_tolid = QCheckBox(Dialog)
        self.checkBox_tolid.setObjectName("checkBox_tolid")
        self.checkBox_tolid.setFont(font2)

        self.horizontalLayout_5.addWidget(self.checkBox_tolid)

        self.checkBox_gozaresh = QCheckBox(Dialog)
        self.checkBox_gozaresh.setObjectName("checkBox_gozaresh")
        self.checkBox_gozaresh.setFont(font2)

        self.horizontalLayout_5.addWidget(self.checkBox_gozaresh)

        self.checkBox_user = QCheckBox(Dialog)
        self.checkBox_user.setObjectName("checkBox_user")
        self.checkBox_user.setEnabled(False)
        self.checkBox_user.setFont(font2)

        self.horizontalLayout_5.addWidget(self.checkBox_user)

        self.checkBox_model = QCheckBox(Dialog)
        self.checkBox_model.setObjectName("checkBox_model")
        self.checkBox_model.setFont(font2)

        self.horizontalLayout_5.addWidget(self.checkBox_model)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.toolButton_cancel = QToolButton(Dialog)
        self.toolButton_cancel.setObjectName("toolButton_cancel")
        self.toolButton_cancel.setMinimumSize(QSize(28, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.toolButton_cancel.setFont(font3)
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
            "                                                                "
        )

        self.horizontalLayout_6.addWidget(self.toolButton_cancel)

        self.toolButton_confirm = QToolButton(Dialog)
        self.toolButton_confirm.setObjectName("toolButton_confirm")
        self.toolButton_confirm.setMinimumSize(QSize(28, 31))
        self.toolButton_confirm.setFont(font3)
        self.toolButton_confirm.setStyleSheet(
            "QToolButton{border-radius:11px;\n"
            "\n"
            "\n"
            "	background-color: rgb(132, 171, 108);\n"
            "}\n"
            "QToolButton:hover{\n"
            "background-color: rgb(255, 166, 139);\n"
            "}\n"
            "\n"
            "                                                                "
        )

        self.horizontalLayout_6.addWidget(self.toolButton_confirm)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate(
                "Dialog",
                "\u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0631",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0631",
                None,
            )
        )
        # if QT_CONFIG(accessibility)
        self.lineEdit_usersname.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        self.lineEdit_usersname.setText("")
        self.lineEdit_usersname.setPlaceholderText(
            QCoreApplication.translate("Dialog", "\u0646\u0627\u0645", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "\u0646\u0627\u0645 :", None)
        )
        self.lineEdit_userslastname.setPlaceholderText(
            QCoreApplication.translate(
                "Dialog",
                "\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :",
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:",
                None,
            )
        )
        self.lineEdit_password.setPlaceholderText(
            QCoreApplication.translate(
                "Dialog", "\u0631\u0645\u0632\u0639\u0628\u0648\u0631", None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "Dialog", "\u0631\u0645\u0632\u0639\u0628\u0648\u0631:", None
            )
        )
        self.checkBox_db.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u06cc\u062a\u0627\u0628\u06cc\u0633",
                None,
            )
        )
        self.checkBox_tolid.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u062a\u0648\u0644\u06cc\u062f \u062c\u0639\u0628\u0647",
                None,
            )
        )
        self.checkBox_gozaresh.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u06af\u0632\u0627\u0631\u0634 \u06af\u06cc\u0631\u06cc",
                None,
            )
        )
        self.checkBox_user.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646",
                None,
            )
        )
        self.checkBox_model.setText(
            QCoreApplication.translate(
                "Dialog", "\u062a\u063a\u06cc\u06cc\u0631 \u0645\u062f\u0644", None
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Dialog", "\u0645\u062c\u0648\u0632 \u0647\u0627 :", None
            )
        )
        self.toolButton_cancel.setText(
            QCoreApplication.translate("Dialog", "\u0644\u063a\u0648", None)
        )
        self.toolButton_confirm.setText(
            QCoreApplication.translate("Dialog", "\u062a\u0627\u06cc\u06cc\u062f", None)
        )

    # retranslateUi
