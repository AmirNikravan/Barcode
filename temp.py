import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedWidget Example")
        self.resize(400, 300)

        # Create the QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Add pages to the QStackedWidget
        self.page1 = QLabel("This is Page 1")
        self.page2 = QLabel("This is Page 2")
        self.page3 = QLabel("This is Page 3")
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # Create buttons to change pages
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")
        self.button3 = QPushButton("Page 3")

        # Set object names for styling
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Connect buttons to functions
        self.button1.clicked.connect(lambda: self.change_page(0))
        self.button2.clicked.connect(lambda: self.change_page(1))
        self.button3.clicked.connect(lambda: self.change_page(2))

        # Create a layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

        # Create the main layout and add widgets
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        # Apply initial styles
        self.update_button_styles()

    def change_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        self.update_button_styles()

    def update_button_styles(self):
        # Reset styles for all buttons
        self.button1.setStyleSheet("")
        self.button2.setStyleSheet("")
        self.button3.setStyleSheet("")

        # Apply style to the active button
        current_index = self.stacked_widget.currentIndex()
        if current_index == 0:
            self.button1.setStyleSheet("background-color: rgb(132, 171, 108); color: white;")
        elif current_index == 1:
            self.button2.setStyleSheet("background-color: rgb(132, 171, 108); color: white;")
        elif current_index == 2:
            self.button3.setStyleSheet("background-color: rgb(132, 171, 108); color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
