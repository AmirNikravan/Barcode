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
)


class DataBase(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.connect = sqlite3.connect("./DataBase/DataBase.db")
        self.cursor = self.connect.cursor()
        self.database_folder = './DataBase/'
        self.current_db_path = os.path.join(self.database_folder, 'DataBase.db')
    def commit(self):
        self.connect.commit()
    def conn(self):
        self.connect = sqlite3.connect("./DataBase/DataBase.db")
    def close(self):
        self.connect.close()
    def fetch_all(self):
        self.cursor.execute("SELECT * FROM user")
        return self.cursor.fetchall()
    def add_user(self, inform):
        try:
            self.cursor.execute("SELECT * FROM user WHERE username = ?", (inform[2],))
            existing_user = self.cursor.fetchone()

            if existing_user:
                QMessageBox.warning(
                    self, "Error", f"Username '{inform[2]}' already exists."
                )
                return 3
            # print(inform)
            self.cursor.execute(
                """
            insert into user (first_name,last_name,username,password,pmodel,puser,pgozaresh,ptoolid,pdb)
            values(?,?,?,?,?,?,?,?,?)
            """,
                (
                    inform[0],
                    inform[1],
                    inform[2],
                    inform[3],
                    inform[4],
                    inform[5],
                    inform[6],
                    inform[7],
                    inform[8],
                ),
            )
            print("added")
            self.commit()
            return 1
        except Exception as e:
            print(f"error inserting user: {e}")
            return 0
    def delete_user(self, username):
        try:
            # Execute the DELETE SQL statement
            self.cursor.execute("DELETE FROM user WHERE username = ?", (username,))
            self.connect.commit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def __del__(self):
        # Ensure connection is closed when object is deleted
        if hasattr(self, 'connection'):
            self.connect.close()
    def fetch_user(self, username):
        try:
            self.cursor.execute("SELECT first_name, last_name, username, password, pmodel, puser, pgozaresh, ptoolid, pdb FROM user WHERE username = ?", (username,))
            row = self.cursor.fetchone()
            if row:
                return {
                    'first_name': row[0],
                    'last_name': row[1],
                    'username': row[2],
                    'password': row[3],
                    'pmodel': row[4],
                    'puser': row[5],
                    'pgozaresh': row[6],
                    'ptoolid': row[7],
                    'pdb': row[8]
                }
            return None
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
    def update_user(self, user_info):
        try:
            self.cursor.execute("""
                UPDATE user SET
                    first_name = ?,
                    last_name = ?,
                    password = ?,
                    pmodel = ?,
                    puser = ?,
                    pgozaresh = ?,
                    ptoolid = ?,
                    pdb = ?
                WHERE username = ?
            """, (user_info['first_name'], user_info['last_name'], user_info['password'],
                  user_info['pmodel'], user_info['puser'], user_info['pgozaresh'],
                  user_info['ptoolid'], user_info['pdb'], user_info['username']))
            self.connect.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
            
    def exportdb(self):
        self.close()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "ذخیره دیتابیس برنامه", self.database_folder, "SQLite Database Files (*.db *.sqlite)", options=options)
        if file_path:
            try:
                # Replace 'your_database.db' with your actual SQLite database file name
                database_file = os.path.join(self.database_folder, 'DataBase.db')
                
                # Connect to SQLite database
                conn = sqlite3.connect(database_file)
                if conn:
                    conn.close()
                    shutil.copy(database_file, f'{file_path}.db')
                    QMessageBox.information(self, "ذخیره", "دیتابیس با موقیت ذخیره شد")
                    
                else:
                    QMessageBox.critical(
                    self, "خطا", f"خطا در برقراری ارتباط با پایگاه داده"
                )
                self.conn()
            except Exception as e:
                QMessageBox.critical(
                    self, "خطا", f"{e}"
                )
            
    def importdb(self):
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
                    # self.conn = None

                # Replace the current database with the chosen one
                if os.path.exists(self.current_db_path):
                    os.remove(self.current_db_path)  # Remove existing file before copying

                shutil.copy(file_path, self.current_db_path)

                # Rename the chosen database file to 'DataBase.db' if it's not already named that
                if os.path.basename(file_path) != 'DataBase.db':
                    new_file_path = os.path.join(self.database_folder, 'DataBase.db')
                    os.rename(file_path, new_file_path)
                    file_path = new_file_path

                QMessageBox.information(self, "Success", f"Database replaced successfully. New file path: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to replace database: {str(e)}")



        
