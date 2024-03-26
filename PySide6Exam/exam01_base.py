import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PySide6 Example')
        self.setGeometry(100, 100, 400, 200)

        label = QLabel('Hello, PySide6!', self)
        label.move(150, 80)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())
