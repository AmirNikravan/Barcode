from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtCore import Qt, QRectF

class RoundedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        button = QPushButton("Close", self)
        button.clicked.connect(self.close)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setFixedSize(300, 200)
        self.setRoundedCorners()

    def setRoundedCorners(self):
        path = QPainterPath()
        rect = QRectF(self.rect())
        radius = 20.0
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = RoundedDialog()
    dialog.show()
    sys.exit(app.exec_())
