import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

class FileValidatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Validator')

        # Layout and widgets
        layout = QVBoxLayout()

        self.excel_label = QLabel('No Excel file selected')
        self.db_label = QLabel('No DB file selected')
        self.validation_label = QLabel('Validation Status: Not Validated')

        self.excel_button = QPushButton('Select Excel File')
        self.db_button = QPushButton('Select DB File')
        self.execute_button = QPushButton('Execute')

        # Initially disable execute button
        self.execute_button.setEnabled(False)

        # Connect buttons to functions
        self.excel_button.clicked.connect(self.select_excel_file)
        self.db_button.clicked.connect(self.select_db_file)
        self.execute_button.clicked.connect(self.execute_action)

        # Add widgets to layout
        layout.addWidget(self.excel_label)
        layout.addWidget(self.excel_button)
        layout.addWidget(self.db_label)
        layout.addWidget(self.db_button)
        layout.addWidget(self.validation_label)
        layout.addWidget(self.execute_button)

        self.setLayout(layout)

        # File paths
        self.excel_file_path = None
        self.db_file_path = None

    def select_excel_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            self.excel_file_path = file_path
            self.excel_label.setText(f'Excel File: {file_path}')
            self.validate_files()

    def select_db_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select DB File", "", "Database Files (*.db)")
        if file_path:
            self.db_file_path = file_path
            self.db_label.setText(f'DB File: {file_path}')
            self.validate_files()

    def validate_files(self):
        if self.excel_file_path and self.db_file_path:
            if self.excel_file_path.endswith(('.xls', '.xlsx')) and self.db_file_path.endswith('.db'):
                self.validation_label.setText('Validation Status: Valid')
                self.execute_button.setEnabled(True)
            else:
                self.validation_label.setText('Validation Status: Invalid File Types')
                self.execute_button.setEnabled(False)
        else:
            self.validation_label.setText('Validation Status: Not Validated')
            self.execute_button.setEnabled(False)

    def execute_action(self):
        if self.excel_file_path and self.db_file_path:
            QMessageBox.information(self, "Execution", "Files are valid. Executing the action.")
            # Add your execution logic here
        else:
            QMessageBox.warning(self, "Execution", "Files are not valid. Cannot execute the action.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    validator_app = FileValidatorApp()
    validator_app.show()
    sys.exit(app.exec())
