import sys
from PyQt5.QtWidgets import (
    QLabel, QCheckBox,
    QLineEdit, QSlider, QRadioButton,
    QPushButton, QVBoxLayout,
    QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Which do you like best?')
        self.dog = QRadioButton('Dogs')
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt Radio buttons')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('So it\'s cats for you')
            

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
