<<<<<<< HEAD
import jdatetime
from datetime import datetime

# Example Gregorian date as string
gregorian_date_str = "2024/07/16"

# Parse Gregorian date string to datetime object
gregorian_date = datetime.strptime(gregorian_date_str, "%Y/%m/%d").date()

# Convert Gregorian date to Persian date
persian_date = jdatetime.date.fromgregorian(date=gregorian_date)

# Get year, month, day from Persian date
year = persian_date.year
month = persian_date.month
day = persian_date.day

print(f"Persian Date: {year}/{month}/{day}")
=======
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
>>>>>>> ui
