import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox

class LoginDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace with your authentication logic
        if username == "admin" and password == "admin123":
            QMessageBox.information(self, "Login Successful", "Welcome Admin!")
            self.close()
            # You can add code here to open another window or perform other actions after successful login
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    login_dialog.show()
    sys.exit(app.exec())
