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
        self.file = None  # for excel
        self.df = pd.DataFrame()
        self.table = excel_table
        self.connect = None
        self.cursor = None
        self.database_folder = "./DataBase/"
        self.current_db_path = os.path.join(self.database_folder, "DataBase.db")
        self.current_excel_path = os.path.join(self.database_folder, "Data.xlsx")
        self.load_existing_files()

    def load_existing_files(self):
        # Check if the database file exists and connect to it
        self.status = [True, True]
        if os.path.exists(self.current_db_path):
            self.conn()
        else:
            QMessageBox.critical(
                self, "خطا", "دیتابیس وجود ندارد، لطفا یک دیتابیس معتبر وارد کنید."
            )
            self.status[0] = False
        # Check if the excel file exists and load it
        if os.path.exists(self.current_excel_path):
            self.file = self.current_excel_path
            try:
                self.df = pd.read_excel(self.current_excel_path)
                # Load the data into the table widget
                self.load_excel_data(self.current_excel_path)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load Excel file: {str(e)}"
                )
        else:
            self.status[1] = False
            QMessageBox.critical(
                self, "خطا", "فایل اکسل وجود ندارد،لطفا یک اکسل معتبر وارد کنید."
            )
        self.validation()

    def commit(self):
        self.connect.commit()

    def conn(self):
        self.connect = sqlite3.connect(self.current_db_path)
        self.cursor = self.connect.cursor()

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
        if hasattr(self, "connection"):
            self.connect.close()

    def fetch_user(self, username):
        try:
            self.cursor.execute(
                "SELECT first_name, last_name, username, password, pmodel, puser, pgozaresh, ptoolid, pdb FROM user WHERE username = ?",
                (username,),
            )
            row = self.cursor.fetchone()
            if row:
                return {
                    "first_name": row[0],
                    "last_name": row[1],
                    "username": row[2],
                    "password": row[3],
                    "pmodel": row[4],
                    "puser": row[5],
                    "pgozaresh": row[6],
                    "ptoolid": row[7],
                    "pdb": row[8],
                }
            return None
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    def update_user(self, user_info):
        try:
            self.cursor.execute(
                """
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
            """,
                (
                    user_info["first_name"],
                    user_info["last_name"],
                    user_info["password"],
                    user_info["pmodel"],
                    user_info["puser"],
                    user_info["pgozaresh"],
                    user_info["ptoolid"],
                    user_info["pdb"],
                    user_info["username"],
                ),
            )
            self.connect.commit()
        except Exception as e:
            print(f"Error updating user: {e}")

    def exportdb(self):
        self.close()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "ذخیره دیتابیس برنامه",
            self.database_folder,
            "SQLite Database Files (*.db *.sqlite)",
            options=options,
        )
        if file_path:
            try:
                # Replace 'your_database.db' with your actual SQLite database file name
                database_file = os.path.join(self.database_folder, "DataBase.db")

                # Connect to SQLite database
                conn = sqlite3.connect(database_file)
                if conn:
                    conn.close()
                    shutil.copy(database_file, f"{file_path}.db")
                    QMessageBox.information(self, "ذخیره", "دیتابیس با موقیت ذخیره شد")

                else:
                    QMessageBox.critical(
                        self, "خطا", f"خطا در برقراری ارتباط با پایگاه داده"
                    )
                self.conn()
            except Exception as e:
                QMessageBox.critical(self, "خطا", f"{e}")

    def importdb(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "فایل دیتابیس را انتحاب کنید",
            "",
            "SQLite Database Files (*.db *.sqlite)",
            options=options,
        )
        if file_path:
            try:
                # Check if the chosen file is the same as the current database
                if file_path == self.current_db_path:
                    QMessageBox.critical(
                        self,
                        "خطا",
                        ".این دیتابیس موجود است،لطفا یک دیتابیس جدید وارد کنید",
                    )
                    return

                # Close any open SQLite connection
                if self.connect:
                    self.close()

                # Replace the current database with the chosen one
                if os.path.exists(self.current_db_path):
                    os.remove(
                        self.current_db_path
                    )  # Remove existing file before copying

                shutil.copy(file_path, self.current_db_path)

                QMessageBox.information(
                    self, "Success", f"دیتابیس با موفقیت جایگزین شد"
                )
                if self.connect == None:
                    self.conn()
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to replace database: {str(e)}"
                )

    def importexcel(self):
        self.file, _ = QFileDialog.getOpenFileName(
            self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)"
        )
        if self.file:
            try:
                # Replace the current excel file with the chosen one
                if os.path.exists(self.current_excel_path):
                    os.remove(
                        self.current_excel_path
                    )  # Remove existing file before copying

                shutil.copy(self.file, self.current_excel_path)
                self.file = self.current_excel_path
                QMessageBox.information(
                    self, "Success", f"فایل اکسل با موقیت بارگذاری شد."
                )
                self.load_excel_data(self.file)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to import Excel file: {str(e)}"
                )

    def load_excel_data(self, file_name):
        try:
            if not self.file:
                QMessageBox.critical(self, "خطا", f"دیتابیس اکسل یافت نشد")
            # Read the Excel file
            self.df = pd.read_excel(file_name)

            # Check if the required columns are in the dataframe
            if "IMEI1" in self.df.columns and "IMEI2" in self.df.columns:
                # Set the table widget's row and column count
                self.table.setRowCount(self.df.shape[0])
                self.table.setColumnCount(self.df.shape[1])

                # Set the table headers
                self.table.setHorizontalHeaderLabels(self.df.columns)

                # Populate the table with data
                for row_index, row_data in self.df.iterrows():
                    for col_index, value in enumerate(row_data):
                        self.table.setItem(
                            row_index, col_index, QTableWidgetItem(str(value))
                        )
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    "The selected file does not contain the required columns 'imei1' and 'imei2'.",
                )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def search_imei(self, text):
        imei1_code = text
        # Check if the dataframe is not empty and contains the required columns
        if (
            not self.df.empty
            and "IMEI1" in self.df.columns
            and "IMEI2" in self.df.columns
        ):
            # Convert IMEI1 column to string type for comparison
            self.df["IMEI1"] = self.df["IMEI1"].astype(str)
            result = self.df[self.df["IMEI1"] == imei1_code]

            if not result.empty:
                imei2_value = result.iloc[0]["IMEI2"]
                return imei2_value
            else:
                print("Result: IMEI1 code not found")
        else:
            print("Result: No data loaded or incorrect file format")

    def validation(self):
        try:
            if os.path.exists(self.current_db_path):
                self.status[0] = True
            else:
                self.status[0] = False
            if os.path.exists(self.current_excel_path):
                self.status[1] = True
            else:
                self.status[1] = False
            return self.status
        except Exception as e:
            QMessageBox.warning(
                self, "Database Error", f"Error checking the database: {e}"
            )
            return False

    def count_rows_in_excel(self):
        try:
            # Read the Excel file into a DataFrame
            if self.file:
                df = pd.read_excel(self.file)

                # Get the number of rows
                num_rows = len(df)

                return num_rows
            else:
                return 0
        except Exception as e:
            print(f"Error reading the Excel file: {e}")
            return None

    def login(self, username, password):
        if self.connect:
            cursor = self.connect.cursor()
            cursor.execute(
                "SELECT * FROM user WHERE username=? AND password=?",
                (username, password),
            )
            user = cursor.fetchone()
            return user is not None

    def permission(self, username):
        if self.connect:
            self.cursor.execute(
                "SELECT pmodel,puser,pgozaresh,ptoolid,pdb FROM user WHERE username=?",
                (username,),
            )
            self.perm = self.cursor.fetchone()
            return {
                "model": self.perm[0],
                "user": self.perm[1],
                "report": self.perm[2],
                "toolid": self.perm[3],
                "db": self.perm[4],
            }
