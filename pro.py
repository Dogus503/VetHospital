import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
from calc import Ui_Form
from math import factorial


class Example(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.group = ""
        self.now = ""
        self.setupUi(self)
        self.btn0.clicked.connect(self.add0)
        self.btn1.clicked.connect(self.add1)
        self.btn2.clicked.connect(self.add2)
        self.btn3.clicked.connect(self.add3)
        self.btn4.clicked.connect(self.add4)
        self.btn5.clicked.connect(self.add5)
        self.btn6.clicked.connect(self.add6)
        self.btn7.clicked.connect(self.add7)
        self.btn8.clicked.connect(self.add8)
        self.btn9.clicked.connect(self.add9)
        self.btn_eq.clicked.connect(self.equals)
        self.btn_sqrt.clicked.connect(self.cor)
        self.btn_pow.clicked.connect(self.step)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.times)
        self.btn_div.clicked.connect(self.nothing)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_dot.clicked.connect(self.addnote)
        self.btn_fact.clicked.connect(self.fact)

    def addnote(self):
        self.group += "."
        self.now += "."
        self.table.display(self.now)

    def add0(self):
        self.group += "0"
        self.now += "0"
        self.table.display(self.now)

    def add1(self):
        self.group += "1"
        self.now += "1"
        self.table.display(self.now)

    def add2(self):
        self.group += "2"
        self.now += "2"
        self.table.display(self.now)

    def add3(self):
        self.group += "3"
        self.now += "3"
        self.table.display(self.now)

    def add4(self):
        self.group += "4"
        self.now += "4"
        self.table.display(self.now)

    def add5(self):
        self.group += "5"
        self.now += "5"
        self.table.display(self.now)

    def add6(self):
        self.group += "6"
        self.now += "6"
        self.table.display(self.now)

    def add7(self):
        self.group += "7"
        self.now += "7"
        self.table.display(self.now)

    def add8(self):
        self.group += "8"
        self.now += "8"
        self.table.display(self.now)

    def add9(self):
        self.group += "9"
        self.now += "9"
        self.table.display(self.now)

    def plus(self):
        self.group += "+"
        self.table.display("")
        self.now = ""

    def minus(self):
        self.group += "-"
        self.table.display("")
        self.now = ""

    def times(self):
        self.group += "*"
        self.table.display("")
        self.now = ""

    def nothing(self):
        self.group += "/"
        self.table.display("")
        self.now = ""

    def clear(self):
        self.table.display("")
        self.group = ""
        self.now = ""

    def equals(self):
        try:
            self.table.display(str(eval(self.group)))
            self.group = str(eval(self.group))
            self.now = self.group
        except:
            self.table.display("Error")
            self.group = ""
            self.now = ""

    def cor(self):
        if self.group[0] != "-1":
            self.table.display(str(eval(self.group + "**0.5")))
        else:
            self.table.display("Error")
        self.group = str(eval(self.group + "**0.5"))
        self.now = self.group

    def step(self):
        self.group += "**"
        self.table.display("")
        self.now = ""

    def fact(self):
        self.group = factorial(int(self.group))
        self.now = self.group
        self.table.display(self.now)

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
