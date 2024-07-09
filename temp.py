import sys
import sqlite3
import shutil
import os
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFileDialog,
    QTableWidgetItem,
)
import pandas as pd

class DataBase(QWidget):
    def __init__(self, excel_table) -> None:
        super().__init__()
        self.file = None
        self.df = pd.DataFrame()
        self.table = excel_table
        self.database_folder = './DataBase/'
        self.current_db_path = os.path.join(self.database_folder, 'DataBase.db')
        self.current_excel_path = os.path.join(self.database_folder, 'Data.xlsx')
        self.connect = None
        self.cursor = None
        self.init_ui()
        self.load_existing_files()

    def init_ui(self):
        layout = QVBoxLayout()
        self.excel_button = QPushButton("Import Excel File")
        self.db_button = QPushButton("Import Database File")
        self.excel_button.clicked.connect(self.import_excel)
        self.db_button.clicked.connect(self.import_db)
        layout.addWidget(self.excel_button)
        layout.addWidget(self.db_button)
        self.setLayout(layout)

    def commit(self):
        if self.connect:
            self.connect.commit()

    def conn(self):
        self.connect = sqlite3.connect(self.current_db_path)
        self.cursor = self.connect.cursor()

    def close(self):
        if self.connect:
            self.connect.close()

    def import_db(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File to Replace", "", "SQLite Database Files (*.db *.sqlite)", options=options)
        if file_path:
            try:
                # Check if the chosen file is the same as the current database
                if file_path == self.current_db_path:
                    QMessageBox.critical(self, "Error", "Cannot replace with the same database file.")
                    return

                # Close any open SQLite connection
                if self.connect:
                    self.close()

                # Replace the current database with the chosen one
                if os.path.exists(self.current_db_path):
                    os.remove(self.current_db_path)  # Remove existing file before copying

                shutil.copy(file_path, self.current_db_path)

                QMessageBox.information(self, "Success", f"Database replaced successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to replace database: {str(e)}")

    def import_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                # Replace the current excel file with the chosen one
                if os.path.exists(self.current_excel_path):
                    os.remove(self.current_excel_path)  # Remove existing file before copying

                shutil.copy(file_path, self.current_excel_path)
                self.file = self.current_excel_path
                QMessageBox.information(self, "Success", f"Excel file imported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to import Excel file: {str(e)}")

    def load_existing_files(self):
        # Check if the database file exists and connect to it
        if os.path.exists(self.current_db_path):
            self.conn()
        else:
            QMessageBox.critical(self, "Error", "Database file not found. Please import a database file.")

        # Check if the excel file exists and load it
        if os.path.exists(self.current_excel_path):
            self.file = self.current_excel_path
            try:
                self.df = pd.read_excel(self.current_excel_path)
                # Load the data into the table widget
                self.load_data_into_table()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load Excel file: {str(e)}")
        else:
            QMessageBox.critical(self, "Error", "Excel file not found. Please import an Excel file.")

    def load_data_into_table(self):
        if not self.df.empty:
            self.table.setRowCount(self.df.shape[0])
            self.table.setColumnCount(self.df.shape[1])
            self.table.setHorizontalHeaderLabels(self.df.columns)

            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.table.setItem(i, j, QTableWidgetItem(str(self.df.iat[i, j])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    excel_table = None  # Replace this with your actual table widget
    validator_app = DataBase(excel_table)
    validator_app.show()
    sys.exit(app.exec())
