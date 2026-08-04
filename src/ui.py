import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
import sys
from pathlib import Path



class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Screenlytics")
        self.resize(700, 700)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)

        main_layout.addWidget(self.sidebar, 1)
        main_layout.addWidget(self.content, 12)

        self.sidebar.setStyleSheet("background-color: #16161E;")
        self.content.setStyleSheet("background-color: #1A1B26;")
    
        header = QWidget()
        header_layout = QHBoxLayout(header)

        title = QLabel("Currently Tracking")
        header_layout.addWidget(title, alignment=Qt.AlignCenter)

        self.content_layout.addWidget(header, 1)

        self.currentcard = QWidget()
        self.currentcard_layout = QVBoxLayout(self.currentcard)

        self.content_layout.addWidget(self.currentcard, 3)
        self.currentcard.setStyleSheet("""
            background-color: #24283B;
            border-radius: 12px;
        """)

        self.other_card = QWidget()
        self.othercard_layout = QVBoxLayout(self.other_card)

        self.content_layout.addWidget(self.other_card, 3)
        self.other_card.setStyleSheet("""
            background-color: #24283B;
            border-radius: 12px;
        """)


app = QApplication(sys.argv)

font_path = Path(__file__).parent.parent / "assets" / "fonts" / "Merriweather" /"MRegularSCL.ttf"

font_id = QFontDatabase.addApplicationFont(str(font_path))
family = QFontDatabase.applicationFontFamilies(font_id)

app.setFont(QFont(family, 20))

window = mainwindow()
window.show()

sys.exit(app.exec())