import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Screenlytics")
        self.resize(1100, 700)

app = QApplication(sys.argv)

window = mainwindow()
window.show()

sys.exit(app.exec())