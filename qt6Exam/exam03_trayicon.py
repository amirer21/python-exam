import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class SystemTrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Create a system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), parent=None)
        self.tray_icon.setToolTip("My Tray Icon")

        # Create a menu for the system tray icon
        self.tray_menu = QMenu()
        self.show_action = QAction("Show", self)
        self.quit_action = QAction("Quit", self)
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)

    def run(self):
        self.tray_icon.show()
        return self.app.exec()

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # Handle tray icon click
            print("Tray icon clicked.")

            # Here you can show your application window or perform other actions.

        elif reason == QSystemTrayIcon.ActivationReason.Context:
            # Handle context menu actions
            action = self.tray_menu.exec_(self.tray_icon.geometry().center())
            if action == self.show_action:
                # Implement action for showing the application window
                print("Show action triggered.")

            elif action == self.quit_action:
                self.app.quit()


if __name__ == "__main__":
    app = SystemTrayApp()
    sys.exit(app.run())
