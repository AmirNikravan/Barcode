from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Disable Sorting in Table")

        # Create a table widget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(3)

        # Fill the table with dummy data
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table_widget.setItem(row, col, item)

        # Disable sorting for all columns
        for col in range(self.table_widget.columnCount()):
            self.table_widget.setSortingEnabled(False)

        # Set central widget
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table_widget)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
