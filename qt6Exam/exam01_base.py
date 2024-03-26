from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("PyQt6 Test")
widget.show()

sys.exit(app.exec())
