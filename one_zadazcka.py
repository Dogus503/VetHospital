from menu import Menu
from results import Resuslt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from tests import Tests


class ThirdWindow(QMainWindow, Tests):
    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Tests")
        self.pushButton_4.clicked.connect(self.show_menu)

    def show_menu(self):
        self.w4 = MyWidget()
        self.w4.show()
        self.hide()


class SecondWindow(QMainWindow, Resuslt):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Results")


class MyWidget(QMainWindow, Menu):
    def __init__(self):
        self.w3 = ThirdWindow()
        super(MyWidget, self).__init__()
        self.w2 = SecondWindow()
        self.setupUi(self)
        self.setWindowTitle('Menu')
        self.result.clicked.connect(self.show_window)
        self.test.clicked.connect(self.show_tests)

    def show_window(self):
        self.w2.show()
        self.hide()

    def show_tests(self):
        self.w3.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
