import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Dialog")

        # Set up layout and widgets
        layout = QVBoxLayout()
        self.label = QLabel("Do you want to confirm?")
        self.confirm_button = QPushButton("Confirm")

        layout.addWidget(self.label)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

        # Connect the confirm button to the accept method
        self.confirm_button.clicked.connect(self.accept)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        # Set up layout and widgets
        layout = QVBoxLayout()
        self.open_dialog_button = QPushButton("Open Dialog")
        layout.addWidget(self.open_dialog_button)
        self.setLayout(layout)

        # Connect the open dialog button to the method that shows the dialog
        self.open_dialog_button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        dialog = MyDialog()
        if dialog.exec_() == QDialog.Accepted:
            print("Dialog confirmed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
