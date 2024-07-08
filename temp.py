import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import QTimer, QDate, QTime, QLocale

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Date, Time, and Day in Farsi")

        # Create layout and central widget
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create labels for date, time, and day
        self.date_label = QLabel()
        self.time_label = QLabel()
        self.day_label = QLabel()

        # Add labels to the layout
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.day_label)

        # Set up a timer to update the labels every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)  # Update every second

        # Initial update
        self.update_labels()

    def update_labels(self):
        # Get current date and time
        current_date = QDate.currentDate()
        current_time = QTime.currentTime()
        
        # Get Farsi locale
        locale = QLocale(QLocale.Persian, QLocale.Iran)

        # Format date and time in Farsi
        date_text = locale.toString(current_date, QLocale.LongFormat)
        time_text = locale.toString(current_time, 'hh:mm:ss')
        day_text = locale.dayName(current_date.dayOfWeek())

        # Set text to labels
        self.date_label.setText(f"تاریخ: {date_text}")
        self.time_label.setText(f"زمان: {time_text}")
        self.day_label.setText(f"روز: {day_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
