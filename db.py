import sqlite3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
)


class DataBase(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.connect = sqlite3.connect("./DataBase/DataBase.db")
        self.cursor = self.connect.cursor()
        self

    def commit(self):
        self.connect.commit()

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