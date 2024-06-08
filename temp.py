from PyQt5 import QtWidgets, QtPrintSupport, QtGui
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # تنظیمات UI
        self.setWindowTitle('Print Example')
        self.setGeometry(100, 100, 800, 600)

        self.printButton = QtWidgets.QPushButton('Print', self)
        self.printButton.setGeometry(250, 250, 100, 50)
        self.printButton.clicked.connect(self.handlePrint)

        self.previewButton = QtWidgets.QPushButton('Preview', self)
        self.previewButton.setGeometry(450, 250, 100, 50)
        self.previewButton.clicked.connect(self.handlePreview)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(300, 350, 200, 30)

    def error_handler(self, message):
        QtWidgets.QMessageBox.critical(self, "Error", message)

    def handlePaintRequest(self, printer):
        try:
            document = QtGui.QTextDocument()
            document.setHtml("<h1>Test Print</h1>")
            document.print_(printer)
        except Exception as e:
            self.error_handler(f"Error Handle Paint Request: {e}")

    def handlePrint(self):
        try:
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec() == QtWidgets.QDialog.Accepted:  # استفاده از Accepted به جای accepted
                self.handlePaintRequest(dialog.printer())
        except Exception as e:
            self.error_handler(f"Error Handle Print: {e}")
        self.lineEdit.setFocus()

    def handlePreview(self):
        try:
            dialog = QtPrintSupport.QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec()
        except Exception as e:
            self.error_handler(f"Error Handle Preview: {e}")
        self.lineEdit.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
