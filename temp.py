import sys
import jdatetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QTimer

class DateTimeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # تنظیمات اولیه ویجت
        self.setWindowTitle('Current DateTime in Jalali')
        self.setGeometry(100, 100, 300, 200)

        # ایجاد تکست باکس
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # ایجاد دکمه برای به‌روزرسانی زمان
        self.button = QPushButton('Update Time', self)
        self.button.clicked.connect(self.update_time)

        # تنظیم لایه
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # تنظیم تایمر برای به‌روزرسانی زمان هر ثانیه
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # به‌روزرسانی هر 1000 میلی‌ثانیه (1 ثانیه)

        # نمایش زمان اولیه
        self.update_time()

    def update_time(self):
        # گرفتن زمان حال
        now = jdatetime.datetime.now()
        current_time = now.strftime('%H:%M:%S')
        current_date = now.strftime('%Y/%m/%d')
        full_date_time = f'{current_date} - {current_time}'

        # نمایش زمان در تکست باکس
        self.text_edit.setText(full_date_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DateTimeWidget()
    ex.show()
    sys.exit(app.exec_())
