import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCalendarWidget, QPushButton, QTableWidget, QTableWidgetItem, QWidget
from persiantools.jdatetime import JalaliDate

class PersianCalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super(PersianCalendarWidget, self).__init__(parent)
        self.setGridVisible(True)
        self.clicked.connect(self.update_persian_date)

    def update_persian_date(self):
        self.selected_date = self.selectedDate()
        self.persian_date = JalaliDate.to_jalali(self.selected_date.year(), self.selected_date.month(), self.selected_date.day())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Persian Calendar Filter Example')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.calendar_widget = PersianCalendarWidget(self)
        self.layout.addWidget(self.calendar_widget)

        self.filter_button = QPushButton('Filter Data', self)
        self.filter_button.clicked.connect(self.filter_data)
        self.layout.addWidget(self.filter_button)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Username', 'Action', 'Action Date'])
        self.layout.addWidget(self.table_widget)

        # Sample data
        self.data = [
            {'id': 1, 'username': 'user1', 'action': 'scanned barcode', 'action_date': '1402-04-23'},
            {'id': 2, 'username': 'user2', 'action': 'logged in', 'action_date': '1402-04-22'},
            {'id': 3, 'username': 'user3', 'action': 'logged out', 'action_date': '1402-04-24'}
        ]

        # Populate table with initial data
        self.populate_table()

    def populate_table(self):
        self.table_widget.setRowCount(len(self.data))

        for row_index, row_data in enumerate(self.data):
            self.table_widget.setItem(row_index, 0, QTableWidgetItem(str(row_data['id'])))
            self.table_widget.setItem(row_index, 1, QTableWidgetItem(row_data['username']))
            self.table_widget.setItem(row_index, 2, QTableWidgetItem(row_data['action']))
            self.table_widget.setItem(row_index, 3, QTableWidgetItem(row_data['action_date']))

    def filter_data(self):
        selected_date = self.calendar_widget.persian_date
        selected_date_str = selected_date.strftime('%Y-%m-%d')

        filtered_data = [row for row in self.data if row['action_date'] == selected_date_str]

        self.table_widget.setRowCount(len(filtered_data))

        for row_index, row_data in enumerate(filtered_data):
            self.table_widget.setItem(row_index, 0, QTableWidgetItem(str(row_data['id'])))
            self.table_widget.setItem(row_index, 1, QTableWidgetItem(row_data['username']))
            self.table_widget.setItem(row_index, 2, QTableWidgetItem(row_data['action']))
            self.table_widget.setItem(row_index, 3, QTableWidgetItem(row_data['action_date']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
