from menu import Menu
from results import Resuslt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from tests import Tests
from history_test import FirstQuest, SecondQuest, ThirdQuest
from nature_test import FirstQuestNature, SecondQuestNature, ThirdQuestNature
from geography_test import FirstQuestGeography, SecondQuestGeography, ThirdQuestGeography
from results_test import GeographyResults, HistoryResults, NatureResults
from DataBaze import DataBase

cnt = 0
db = DataBase()


class GeographyEnd(QMainWindow, GeographyResults):
    def __init__(self, parent=None):
        global cnt
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("GeographyResults")
        self.pushButton.clicked.connect(self.show_again)
        self.pushButton_2.clicked.connect(self.show_tests)
        db.insert(cnt, "Geography")
        ans = db.select("Geography")[0]
        ans = str(ans)
        ans = ans.replace("(", "")
        ans = ans.replace(")", "")
        ans = ans.replace(",", "")
        self.label.setText("Вы сделали\nправильно\n{} из 3 вопросов"
                           "\nЛучший\nрезультат: {}".format(cnt, ans))
        cnt = 0

    def show_tests(self):
        self.w = ThirdWindow()
        self.w.show()
        self.hide()

    def show_again(self):
        self.w1 = GeographyFirst()
        self.w1.show()
        self.hide()


class HistoryEnd(QMainWindow, HistoryResults):
    def __init__(self, parent=None):
        global cnt
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("HistoryResults")
        self.pushButton.clicked.connect(self.show_again)
        self.pushButton_2.clicked.connect(self.show_tests)
        db.insert(cnt, "History")
        ans = db.select("History")[0]
        ans = str(ans)
        ans = ans.replace("(", "")
        ans = ans.replace(")", "")
        ans = ans.replace(",", "")
        self.label.setText("Вы сделали\nправильно\n{} из 3 вопросов"
                           "\nЛучший\nрезультат: {}".format(cnt, ans))
        cnt = 0

    def show_tests(self):
        self.w = ThirdWindow()
        self.w.show()
        self.hide()

    def show_again(self):
        self.w1 = FourthWindow()
        self.w1.show()
        self.hide()


class NatureEnd(QMainWindow, NatureResults):
    def __init__(self, parent=None):
        global cnt
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("NatureResults")
        self.pushButton.clicked.connect(self.show_again)
        self.pushButton_2.clicked.connect(self.show_tests)
        db.insert(cnt, "Nature")
        ans = db.select("Nature")[0]
        ans = str(ans)
        ans = ans.replace("(", "")
        ans = ans.replace(")", "")
        ans = ans.replace(",", "")
        self.label.setText("Вы сделали\nправильно\n{} из 3 вопросов"
                           "\nЛучший\nрезультат: {}".format(cnt, ans))
        cnt = 0

    def show_tests(self):
        self.w = ThirdWindow()
        self.w.show()
        self.hide()

    def show_again(self):
        self.w1 = NatureFirst()
        self.w1.show()
        self.hide()


class GeographyThird(QMainWindow, ThirdQuestGeography):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("GeographyTestThirdQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if not self.checkBox.isChecked() and not self.checkBox_2.isChecked() and \
                self.checkBox_3.isChecked() and self.checkBox_4.isChecked() and \
                self.checkBox_5.isChecked() and not self.checkBox_6.isChecked():
            cnt += 1
        self.w = GeographyEnd()
        self.w.show()
        self.hide()


class GeographySecond(QMainWindow, SecondQuestGeography):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("GeographyTestSecondQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.radioButton_3.isChecked():
            cnt += 1
        self.w = GeographyThird()
        self.w.show()
        self.hide()


class GeographyFirst(QMainWindow, FirstQuestGeography):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("GeographyTestFirstQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.lineEdit.text() == "Байкал":
            cnt += 1
        self.w = GeographySecond()
        self.w.show()
        self.hide()


class NatureThird(QMainWindow, ThirdQuestNature):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("NatureTestThirdQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.lineEdit.text() == "Мустанг":
            cnt += 1
        self.w = NatureEnd()
        self.w.show()
        self.hide()


class NatureSecond(QMainWindow, SecondQuestNature):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("NatureTestSecondQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.checkBox.isChecked() and not self.checkBox_2.isChecked() \
                and not self.checkBox_3.isChecked() and \
                self.checkBox_4.isChecked() and not self.checkBox_5.isChecked():
            cnt += 1
        self.w = NatureThird()
        self.w.show()
        self.hide()


class NatureFirst(QMainWindow, FirstQuestNature):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("NatureTestFirstQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.radioButton_4.isChecked():
            cnt += 1
        self.w = NatureSecond()
        self.w.show()
        self.hide()


class SixWindow(QMainWindow, ThirdQuest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("HistoryTestThirdQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.lineEdit.text() == "Афина":
            cnt += 1
        self.w = HistoryEnd()
        self.w.show()
        self.hide()


class FiveWindow(QMainWindow, SecondQuest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("HistoryTestSecondQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.checkBox.isChecked() and self.checkBox_2.isChecked() \
                and not self.checkBox_3.isChecked() and self.checkBox_4.isChecked() \
                and not self.checkBox_5.isChecked() and not self.checkBox_6.isChecked():
            cnt += 1
        self.w = SixWindow()
        self.w.show()
        self.hide()


class ThirdWindow(QMainWindow, Tests):
    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Tests")
        self.pushButton_4.clicked.connect(self.show_menu)
        self.pushButton_3.clicked.connect(self.show_history)
        self.pushButton_2.clicked.connect(self.show_nature)
        self.pushButton.clicked.connect(self.show_world)

    def show_menu(self):
        self.w4 = MyWidget()
        self.w4.show()
        self.hide()

    def show_history(self):
        self.w5 = FourthWindow()
        self.w5.show()
        self.hide()

    def show_nature(self):
        self.w6 = NatureFirst()
        self.w6.show()
        self.hide()

    def show_world(self):
        self.w7 = GeographyFirst()
        self.w7.show()
        self.hide()


class FourthWindow(QMainWindow, FirstQuest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("HistoryTestFirstQuest")
        self.pushButton.clicked.connect(self.show_next)

    def show_next(self):
        global cnt
        if self.radioButton.isChecked():
            cnt += 1
        self.w = FiveWindow()
        self.w.show()
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
