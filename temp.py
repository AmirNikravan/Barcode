from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
import sys
import shutil
import os
import sqlite3
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SQLite Database Operations')
        self.setGeometry(100, 100, 400, 200)

        # Button to save database
        self.button_save_db = QPushButton('Save Database', self)
        self.button_save_db.setGeometry(50, 50, 300, 50)
        self.button_save_db.clicked.connect(self.save_database)

        # Button to replace database
        self.button_replace_db = QPushButton('Replace Database', self)
        self.button_replace_db.setGeometry(50, 120, 300, 50)
        self.button_replace_db.clicked.connect(self.replace_database)

        # Specify the folder where your SQLite database is located
        self.database_folder = '/path/to/your/database/folder'
        self.current_db_path = os.path.join(self.database_folder, 'your_current_database.db')  # Replace with your current database file name

    def save_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Database File", self.database_folder, "SQLite Database Files (*.db *.sqlite)", options=options)
        if file_path:
            try:
                conn = sqlite3.connect(self.current_db_path)  # Connect to your SQLite database
                if conn:
                    conn.close()
                    shutil.copy(self.current_db_path, file_path)  # Copy the current database to the chosen location
                    QMessageBox.information(self, "Success", f"Database saved to {file_path}")
                else:
                    QMessageBox.critical(self, "Error", "Failed to connect to database.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save database: {str(e)}")

    def replace_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File to Replace", "", "SQLite Database Files (*.db *.sqlite)", options=options)
        if file_path:
            try:
                # Check if the chosen file is the same as the current database
                if file_path == self.current_db_path:
                    QMessageBox.critical(self, "Error", "Cannot replace with the same database file.")
                    return

                # Close any connections to the current database
                # Example: conn.close() for closing SQLite connection

                # Replace the current database with the chosen one
                shutil.copy(file_path, self.current_db_path)
                
                QMessageBox.information(self, "Success", "Database replaced successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to replace database: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
