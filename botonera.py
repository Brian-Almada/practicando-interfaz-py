from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class CustomButton(QPushButton):
    def __init__(self, text, icon_path, parent=None):
        super().__init__(text, parent)

        self.setFixedHeight(60)
        self.setStyleSheet("""
            QPushButton {
                background-color: #555;
                border: none;
                border-radius: 20px;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #777;
            }
            QPushButton:pressed {
                background-color: #888;
            }
        """)

        pixmap = QPixmap(icon_path).scaledToHeight(40, mode=Qt.SmoothTransformation)
        icon = QIcon(pixmap)
        self.setIcon(icon)
        self.setIconSize(pixmap.size())
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button1 = CustomButton("Play", "play.png", parent=self)
        button1.move(50, 50)

        button2 = CustomButton("Stop", "stop.png", parent=self)
        button2.move(150, 50)

        self.setGeometry(100, 100, 300, 150)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
