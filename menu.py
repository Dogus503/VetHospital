# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Menu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(890, 605)
        self.test = QtWidgets.QPushButton(Dialog)
        self.test.setGeometry(QtCore.QRect(230, 120, 381, 141))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.test.setFont(font)
        self.test.setObjectName("test")
        self.result = QtWidgets.QPushButton(Dialog)
        self.result.setGeometry(QtCore.QRect(230, 320, 381, 141))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.result.setFont(font)
        self.result.setObjectName("result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.test.setText(_translate("Dialog", "Тесты"))
        self.result.setText(_translate("Dialog", "Результаты"))
