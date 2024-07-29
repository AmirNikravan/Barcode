from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
from preview import Ui_Dialog
class Preview(QDialog):
    def __init__(self, path):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        pixmap = QPixmap(path)
        self.ui.label.setPixmap(pixmap)
