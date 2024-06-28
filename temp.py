import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SVG Preview")

        # Create a central widget and set the layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create an SVG widget
        self.svg_widget = QSvgWidget()
        layout.addWidget(self.svg_widget)

        # Load an SVG file
        svg_file_path = "path/to/your/file.svg"  # Replace with your SVG file path
        self.svg_widget.load(svg_file_path)

        self.resize(800, 600)

        # Ensure proper scaling for high DPI displays
        self.svg_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.svg_widget.setScaledContents(True)
        self.svg_widget.setAspectRatioMode(Qt.KeepAspectRatio)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Enable high DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
