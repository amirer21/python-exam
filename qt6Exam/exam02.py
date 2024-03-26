import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt6 Example')
        self.setGeometry(300, 300, 300, 200)

        btn = QPushButton('Click me', self)
        btn.clicked.connect(self.showMessageBox)
        btn.move(100, 70)

    def showMessageBox(self):
        QMessageBox.information(self, 'Message', 'Button clicked.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())
