from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Barcode Scanner Example")

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(15)  # Set maximum length to 15 digits
        self.line_edit.setAlignment(Qt.AlignCenter)  # Align text to center

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_digits)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Connect the returnPressed signal to the save_digits slot for manual input
        self.line_edit.returnPressed.connect(self.save_digits)

    def save_digits(self):
        digits = self.line_edit.text()
        if len(digits) == 15:
            # Save the digits to your database or perform other operations
            print("Digits:", digits)
            self.line_edit.clear()  # Clear the line edit after scanning
        else:
            print("Invalid input. Please enter 15 digits.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
