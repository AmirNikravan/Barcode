from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, user_role):
        super().__init__()
        
        self.user_role = user_role
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Permission Based App')
        
        layout = QVBoxLayout()
        
        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')
        
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.apply_permissions()

    def apply_permissions(self):
        permissions = self.get_permissions(self.user_role)
        
        self.button1.setEnabled('button1' in permissions)
        self.button2.setEnabled('button2' in permissions)
        self.button3.setEnabled('button3' in permissions)

    def get_permissions(self, role):
        roles_permissions = {
            'admin': ['button1', 'button2', 'button3'],
            'editor': ['button1', 'button2'],
            'viewer': []
        }
        return roles_permissions.get(role, [])

if __name__ == '__main__':
    app = QApplication([])
    
    # Simulate logging in as different user roles
    user_role = 'viewer'  # Change this to 'admin', 'editor', or 'viewer'
    
    window = MainWindow(user_role)
    window.show()
    
    app.exec()
