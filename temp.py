import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel Data Viewer")

        # Initialize dataframe
        self.df = pd.DataFrame()

        # Set the layout
        self.layout = QVBoxLayout()

        # Create a button to open Excel files
        self.open_button = QPushButton("Open Excel File")
        self.open_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.open_button)

        # Create a line edit for user input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter IMEI1 code")
        self.layout.addWidget(self.search_input)

        # Create a button for searching
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_imei)
        self.layout.addWidget(self.search_button)

        # Label to show the result
        self.result_label = QLabel("Result: ")
        self.layout.addWidget(self.result_label)

        # Create a table widget to display the data
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        # Set the central widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            self.load_excel_data(file_name)

    def load_excel_data(self, file_name):
        try:
            # Read the Excel file
            self.df = pd.read_excel(file_name)

            # Check if the required columns are in the dataframe
            if 'IMEI1' in self.df.columns and 'IMEI2' in self.df.columns:
                # Set the table widget's row and column count
                self.table_widget.setRowCount(self.df.shape[0])
                self.table_widget.setColumnCount(self.df.shape[1])

                # Set the table headers
                self.table_widget.setHorizontalHeaderLabels(self.df.columns)

                # Populate the table with data
                for row_index, row_data in self.df.iterrows():
                    for col_index, value in enumerate(row_data):
                        self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
            else:
                QMessageBox.warning(self, "Error", "The selected file does not contain the required columns 'IMEI1' and 'IMEI2'.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def search_imei(self):
        imei1_code = self.search_input.text().strip()
        # Check if the dataframe is not empty and contains the required columns
        if not self.df.empty and 'IMEI1' in self.df.columns and 'IMEI2' in self.df.columns:
            # Convert IMEI1 column to string type for comparison
            self.df['IMEI1'] = self.df['IMEI1'].astype(str)
            result = self.df[self.df['IMEI1'] == imei1_code]

            if not result.empty:
                imei2_value = result.iloc[0]['IMEI2']
                self.result_label.setText(f"Result: {imei2_value}")
            else:
                self.result_label.setText("Result: IMEI1 code not found")
        else:
            self.result_label.setText("Result: No data loaded or incorrect file format")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
