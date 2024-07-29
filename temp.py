import sys
import cairosvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap

class ImagePreviewWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        self.setWindowTitle('Image Preview')
        self.setGeometry(400, 400, 800, 600)

        # Create a QLabel to display the image
        self.label = QLabel()
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Specify the SVG file path here
    svg_file = '1.svg'  # Replace with your actual SVG file path
    png_file = 'converted_image.png'        # Path for the converted PNG file

    # Convert SVG to PNG using CairoSVG
    cairosvg.svg2png(url=svg_file, write_to=png_file)

    # Create and show the window to preview the PNG image
    window = ImagePreviewWindow(png_file)
    window.show()

    sys.exit(app.exec_())
