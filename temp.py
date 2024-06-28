import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clickable Link in QMessageBox")
        self.setGeometry(100, 100, 400, 200)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Button to show QMessageBox
        self.show_message_button = QPushButton("Show Message Box")
        self.show_message_button.clicked.connect(self.show_message_box)
        self.layout.addWidget(self.show_message_button)

    def show_message_box(self):
        # Create a QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Message Box with Link")
        msg_box.setIcon(QMessageBox.Information)

        # Set the message text with HTML to create a link
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        msg_box.setText("This is a <a href='https://www.example.com'>link</a> in a QMessageBox.")

        # Set other buttons and execute
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
