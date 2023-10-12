import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(600, 400))
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout) 


app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("pswrd gen")
window.show()

app.exec()
