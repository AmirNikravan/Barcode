from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QSizePolicy
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fill Space Example")

        # Create a QHBoxLayout
        layout = QHBoxLayout()

        # Create a QStackedWidget
        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(QLabel("Stacked Widget Page 1"))
        stacked_widget.addWidget(QLabel("Stacked Widget Page 2"))

        # Create another QWidget
        other_widget = QWidget()
        other_widget.setStyleSheet("background-color: lightgray;")  # Just for visualization

        # Set size policy for other_widget to expand
        other_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add widgets to the layout
        layout.addWidget(stacked_widget)
        layout.addWidget(other_widget)

        # Set the layout for the main window
        self.setLayout(layout)

        # Stretch factor to fill the space between the widgets
        layout.setStretch(0, 1)  # Set stretch factor for stacked_widget
        layout.setStretch(1, 2)  # Set stretch factor for other_widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
