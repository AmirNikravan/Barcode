from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QComboBox
import sys

# شبیه‌سازی کلاس دیتابیس برای خواندن مجوزهای کاربر
class Database:
    def __init__(self):
        # شبیه‌سازی مجوزهای کاربران به صورت دستی
        self.user_permissions = {
            'user1': {'page1': 1, 'page2': 0, 'page3': 1},  # مجوزهای user1 برای صفحه‌ها
            'user2': {'page1': 0, 'page2': 1, 'page3': 1}   # مجوزهای user2 برای صفحه‌ها
        }

    def get_user_permissions(self, username):
        if username in self.user_permissions:
            return self.user_permissions[username]
        else:
            return {}

# کلاس اصلی برنامه
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()

        # صفحه ۱: نمونه اولیه
        page1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QPushButton("Button 1 - Page 1"))
        page1.setLayout(layout1)
        self.stacked_widget.addWidget(page1)

        # صفحه ۲: نمونه دوم
        page2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QComboBox())
        page2.setLayout(layout2)
        self.stacked_widget.addWidget(page2)

        # صفحه ۳: نمونه سوم
        page3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.addWidget(QPushButton("Button 1 - Page 3"))
        layout3.addWidget(QComboBox())
        page3.setLayout(layout3)
        self.stacked_widget.addWidget(page3)

        self.setCentralWidget(self.stacked_widget)

        self.database = Database()
        self.current_user = 'user2'  # فرض کنید کاربر وارد شده

        self.set_permissions()

    def set_permissions(self):
        permissions = self.database.get_user_permissions(self.current_user)

        # تنظیم مجوزها برای هر صفحه
        for index in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(index)
            page_name = f"page{index + 1}"

            if page_name in permissions and permissions[page_name] == 0:
                # غیرفعال کردن دکمه یا ComboBox مربوط به صفحه
                for child in widget.findChildren(QPushButton) + widget.findChildren(QComboBox):
                    child.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
