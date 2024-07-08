import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Dialog")

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create an OK button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.on_ok_clicked)

        # Add the button to the layout
        layout.addWidget(self.ok_button)

        # Set the dialog layout
        self.setLayout(layout)

    def on_ok_clicked(self):
        self.close()  # Closes the dialog with an accept signal

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = MyDialog()
    dialog.exec()  # Show the dialog as a modal dialog

    sys.exit(app.exec())
