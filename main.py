import sys 
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(300, 200))

        # WIDGET CENTRAL
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # MAIN LAYOUT
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # GRID LAYOUT FOR OPTIONS
        option_layout = QGridLayout()

        # PASSWORD GENERATED
        self.password_generated = QLineEdit()

        # BTN LAYOUT
        button_layout = QHBoxLayout()

        main_layout.addLayout(option_layout)
        main_layout.addWidget(self.password_generated)
        main_layout.addLayout(button_layout)

        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copier", self)
        btn_genrate = QPushButton("Générer", self)

        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_genrate)

        # SLIDER LAYOUT
        self.txt_size = QLabel("Taille : 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.options_size = QSlider(Qt.Horizontal)
        self.options_size.setMinimum(8)
        self.options_size.setMaximum(30)
        self.options_size.setValue(10)
        option_layout.addWidget(self.options_size, 1, 0)

        self.option_lowercase = QCheckBox("Minuscules")
        self.option_uppercase = QCheckBox("Majuscules")
        self.option_numbers = QCheckBox("Chiffres")
        self.option_symboles = QCheckBox("Symboles")

        option_layout.addWidget(self.option_lowercase, 1, 1)
        option_layout.addWidget(self.option_uppercase, 0, 1)
        option_layout.addWidget(self.option_numbers, 0, 2)
        option_layout.addWidget(self.option_symboles, 1, 2)

        self.option_lowercase.setChecked(True)
        self.option_numbers.setChecked(True)


        btn_quit.clicked.connect(self.quit)
        btn_copy.clicked.connect(self.copy)
        btn_genrate.clicked.connect(self.generate)

        self.options_size.valueChanged.connect(self.change_size)

        self.generate()

        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()

    def quit(self):
        QApplication.quit()

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())
        self.status.showMessage("Mot de passe copié", 1000)

    def generate(self):
        size = self.options_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_number = self.option_numbers.isChecked()
        has_symbol = self.option_symboles.isChecked()
        
        letters = ''
        if has_lower:
            letters += "azertyuiopqsdfghjklmwxcvbn"
        if has_upper:
            letters += "AZERTYUIOPQSDFGHJKLMWXCVBN"
        if has_number:
            letters += "0123456789"
        if has_symbol:
            letters += "$*&%"

        password = ''
        for i in range(size):
            password += choice(letters) 
        self.password_generated.setText(password)

    def change_size(self):
        # récuperer la valeur => actualiser texte
        value = self.options_size.value()
        self.txt_size.setText("taille : " + str(value))

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Password generator")
window.show()
app.exec()