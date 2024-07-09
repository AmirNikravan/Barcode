from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

class Database:
    def __init__(self):
        # Simulating user data with a dictionary (username: password)
        self.users = {
            'user1': 'password1',
            'user2': 'password2'
        }

    def login(self, username, password):
        # Check if username exists and password matches
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

class Login(QDialog):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.setWindowTitle("Login")
        
        # Username and password input fields
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("نام کاربری")
        self.lineEdit_pass = QLineEdit()
        self.lineEdit_pass.setPlaceholderText("رمز عبور")
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)
        
        # Buttons
        self.toolButton_enter = QPushButton("ورود")
        self.toolButton_cancel = QPushButton("لغو")
        self.toolButton_enter.clicked.connect(self.validation)
        self.toolButton_cancel.clicked.connect(self.reject)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit_username)
        layout.addWidget(self.lineEdit_pass)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.toolButton_enter)
        button_layout.addWidget(self.toolButton_cancel)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def validation(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_pass.text()
        if self.database.login(username, password):
            self.accept()  # Accept the dialog if login is successful
        else:
            QMessageBox.critical(self, 'خطا', 'نام کاربری یا رمز عبور اشتباه است.')
            self.lineEdit_username.clear()
            self.lineEdit_pass.clear()
            self.lineEdit_username.setFocus()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.current_user = None  # Track current logged-in user

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        # Create actions for menus or toolbar
        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.logout_action = QAction('Logout', self)
        self.logout_action.triggered.connect(self.logout)

    def create_menus(self):
        self.menuBar().addAction(self.logout_action)

    def handle_login(self):
        dialog = Login(self.database)
        if dialog.exec() == QDialog.Accepted:
            self.current_user = dialog.lineEdit_username.text()  # Store logged-in user
            self.show()
        else:
            sys.exit(0)  # Exit application if login is cancelled or failed

    def logout(self):
        self.current_user = None  # Clear current user session
        # Additional actions to reset UI or return to login state if necessary
        # For example, hide user-specific UI elements, disable certain actions

        # Optionally, show the login dialog again after logout
        self.handle_login()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.handle_login()
    sys.exit(app.exec())
