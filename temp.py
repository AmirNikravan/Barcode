import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the directory when the program starts
        self.create_images_directory()

        # Your GUI setup code here

    def closeEvent(self, event):
        # Delete the directory when the program ends
        self.delete_images_directory()
        event.accept()

    def create_images_directory(self):
        directory = "images"
        if not os.path.exists(directory):
            os.makedirs(directory)

    def delete_images_directory(self):
        directory = "images"
        if os.path.exists(directory):
            # Remove all files inside the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")

            # Delete the directory
            try:
                os.rmdir(directory)
            except OSError as e:
                print(f"Failed to delete directory {directory}. Reason: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
