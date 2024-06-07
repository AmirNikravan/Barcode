import sys
import os
from PySide6.QtWidgets import QMessageBox

class Directory():
    def __init__(self):
        self.create_images_directory()

    def closeEvent(self, event):
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
                    error_message = f"Failed to delete {file_path}. Reason: {e}"
                    self.show_error_message(error_message)

            # Delete the directory
            try:
                os.rmdir(directory)
            except OSError as e:
                error_message = f"Failed to delete directory {directory}. Reason: {e}"
                self.show_error_message(error_message)

    def show_error_message(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText("Error")
        error_box.setInformativeText(message)
        error_box.setWindowTitle("Error")
        error_box.exec()
