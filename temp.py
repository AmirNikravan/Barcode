import sys
import jdatetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from starcal import StarCalendarWidget

class TableWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTableWidget Demo with Shamsi Date Filter')
        self.setGeometry(100, 100, 800, 600)

        self.data = [
            ['John Doe', '30', '1403/04/24-04:47:53 AM'],
            ['Jane Smith', '25', '1403/04/25-10:22:10 AM'],
            ['Emily Johnson', '35', '1403/04/23-01:14:33 PM'],
            ['Michael Brown', '40', '1403/04/20-11:47:00 AM']
        ]

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create filter layout
        filter_layout = QHBoxLayout()
        self.start_date_edit = StarCalendarWidget(self)
        self.end_date_edit = StarCalendarWidget(self)
        
        filter_button = QPushButton('Apply Filter')
        filter_button.clicked.connect(self.apply_filter)

        filter_layout.addWidget(QLabel('Start Date:'))
        filter_layout.addWidget(self.start_date_edit)
        filter_layout.addWidget(QLabel('End Date:'))
        filter_layout.addWidget(self.end_date_edit)
        filter_layout.addWidget(filter_button)

        layout.addLayout(filter_layout)

        # Create table widget
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_data()

    def load_data(self, start_date=None, end_date=None):
        if start_date and end_date:
            filtered_data = [
                row for row in self.data
                if start_date <= self.parse_jalali_date(row[2]) <= end_date
            ]
        else:
            filtered_data = self.data

        column_names = ['Name', 'Age', 'Date']

        self.table_widget.setRowCount(len(filtered_data))
        self.table_widget.setColumnCount(len(column_names))
        self.table_widget.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(filtered_data):
            for col_idx, cell_data in enumerate(row_data):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

        self.table_widget.resizeColumnsToContents()

    def apply_filter(self):
        start_date = self.start_date_edit.selectedDate().toPyDate()
        end_date = self.end_date_edit.selectedDate().toPyDate()
        self.load_data(start_date, end_date)

    def parse_jalali_date(self, date_str):
        # Parse date from string and convert to jdatetime.date
        date_str = date_str.split('-')[0]
        year, month, day = map(int, date_str.split('/'))
        return jdatetime.date(year, month, day).togregorian()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TableWidgetDemo()
    demo.show()
    sys.exit(app.exec_())
