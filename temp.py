import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete Table Rows Example")
        self.setGeometry(300, 300, 600, 400)

        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a table
        self.table = QTableWidget(5, 3)  # 5 rows and 3 columns
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Populate the table with some data
        for row in range(5):
            for column in range(3):
                item = QTableWidgetItem(f"Item {row+1}-{column+1}")
                self.table.setItem(row, column, item)

        # Create a delete button
        self.delete_button = QPushButton("Delete Selected Rows")
        self.delete_button.clicked.connect(self.delete_selected_rows)

        # Add the table and button to the layout
        layout.addWidget(self.table)
        layout.addWidget(self.delete_button)

    def delete_selected_rows(self):
        # Get selected items
        selected_items = self.table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "No selection", "Please select one or more cells to delete.")
            return

        # Get unique row indexes from selected items
        rows = {item.row() for item in selected_items}

        # Sort row indexes in reverse order
        for row in sorted(rows, reverse=True):
            self.table.removeRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
