import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon


def tray_icon_clicked(reason):
    print("Tray icon clicked:", reason)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon("thumbs-down.png"))  # Use the thumbs-down.png file
    tray_icon.setToolTip("System Tray Example")

    menu = QMenu()
    exit_action = menu.addAction("Exit")
    exit_action.triggered.connect(app.quit)

    tray_icon.setContextMenu(menu)

    tray_icon.activated.connect(tray_icon_clicked)

    tray_icon.show()
    sys.exit(app.exec())
