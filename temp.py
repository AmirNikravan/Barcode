from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys
import sqlite3
import shutil
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Save SQLite Database')
        self.setGeometry(100, 100, 400, 200)

        self.button_save_db = QPushButton('Save Database', self)
        self.button_save_db.setGeometry(50, 50, 300, 50)
        self.button_save_db.clicked.connect(self.save_database)

        # Specify the folder where your SQLite database is located
        self.database_folder = './DataBase/'

    def save_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Database File", self.database_folder, "SQLite Database Files (*.db *.sqlite)", options=options)
        if file_path:
            try:
                # Replace 'your_database.db' with your actual SQLite database file name
                database_file = os.path.join(self.database_folder, 'DataBase.db')
                
                # Connect to SQLite database
                conn = sqlite3.connect(database_file)
                if conn:
                    conn.close()
                    shutil.copy(database_file, f'{file_path}.db')
                    self.statusBar().showMessage(f"Database saved to {file_path}", 5000)
                else:
                    self.statusBar().showMessage("Failed to connect to database", 5000)
            except Exception as e:
                self.statusBar().showMessage(f"Error: {str(e)}", 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
