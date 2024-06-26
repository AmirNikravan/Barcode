import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtSvgWidgets import QSvgWidget
class SvgViewer(QMainWindow):
    def __init__(self, svg_file):
        super().__init__()

        # Set the window title
        self.setWindowTitle('SVG Viewer')

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create the QSvgWidget
        svg_widget = QSvgWidget(svg_file)

        # Add the SVG widget to the layout
        layout.addWidget(svg_widget)

        # Resize the window to fit the content
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Path to the SVG file
    svg_file = 'qt_api_test.svg'

    # Create and show the main window
    viewer = SvgViewer(svg_file)
    viewer.show()

    # Run the application event loop
    sys.exit(app.exec_())
