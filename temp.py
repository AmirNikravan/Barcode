from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLineEdit, QMessageBox, QLabel,
    QDialogButtonBox
)
from PySide6.QtCore import Qt

# Constants for roles and permissions
class Permissions:
    Admin = 0
    User = 1
    Guest = 2

# Mock database class
class Database:
    def __init__(self):
        self.users = {
            'admin': {'password': 'adminpass', 'role': Permissions.Admin},
            'user': {'password': 'userpass', 'role': Permissions.User},
            'guest': {'password': 'guestpass', 'role': Permissions.Guest},
        }

    def authenticate(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return self.users[username]['role']
        return None

# Login dialog class
class LoginDialog(QDialog):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("Login")
        self.setFixedSize(300, 150)
        layout = QVBoxLayout()

        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_edit)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def username(self):
        return self.username_edit.text()

    def password(self):
        return self.password_edit.text()

# Main window class
class MainWindow(QMainWindow):
    def __init__(self, user_role, database):
        super().__init__()
        self.user_role = user_role
        self.database = database
        self.setWindowTitle("Main Application")
        self.setFixedSize(400, 300)
        self.central_widget = QVBoxLayout()

        self.btn_view_reports = QPushButton("View Reports")
        self.btn_view_reports.clicked.connect(self.view_reports)

        self.btn_edit_settings = QPushButton("Edit Settings")
        self.btn_edit_settings.clicked.connect(self.edit_settings)

        self.central_widget.addWidget(self.btn_view_reports)
        self.central_widget.addWidget(self.btn_edit_settings)

        main_widget = QWidget()
        main_widget.setLayout(self.central_widget)
        self.setCentralWidget(main_widget)

    def view_reports(self):
        if self.user_role in [Permissions.Admin, Permissions.User]:
            QMessageBox.information(self, "View Reports", "You can view reports.")
        else:
            QMessageBox.warning(self, "Access Denied", "You do not have permission to view reports.")

    def edit_settings(self):
        if self.user_role == Permissions.Admin:
            QMessageBox.information(self, "Edit Settings", "You can edit settings.")
        else:
            QMessageBox.warning(self, "Access Denied", "You do not have permission to edit settings.")

# Main application
def main():
    app = QApplication([])
    database = Database()
    login_dialog = LoginDialog(database)

    if login_dialog.exec() == QDialog.Accepted:
        username = login_dialog.username()
        user_role = database.authenticate(username, login_dialog.password())
        if user_role is not None:
            main_window = MainWindow(user_role, database)
            main_window.show()
            app.exec()

if __name__ == "__main__":
    main()
