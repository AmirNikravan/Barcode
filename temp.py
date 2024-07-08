from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QColor
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Populate example data
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.tableWidget.setItem(row, col, item)

        # Apply stylesheet to QTableWidget
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;
                alternate-background-color: #ffffff;
                selection-background-color: #b3d9ff;
                border: 1px solid #d0d0d0;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #d0d0d0;
            }
            QTableWidget::item:selected {
                background-color: #b3d9ff;
                color: black;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
