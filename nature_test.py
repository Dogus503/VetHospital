# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nature_firstque.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FirstQuestNature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 620)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 160, 261, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Кто самый близкий родственник\n"
                                                "бизона?"))
        self.radioButton.setText(_translate("Dialog", "Козёл"))
        self.radioButton_2.setText(_translate("Dialog", "Корова"))
        self.radioButton_3.setText(_translate("Dialog", "Баран"))
        self.radioButton_4.setText(_translate("Dialog", "Зубр"))
        self.pushButton.setText(_translate("Dialog", "Ответить"))


class SecondQuestNature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 620)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 170, 281, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Какие из этих пород\n"
                                                "собак ездовые:"))
        self.checkBox.setText(_translate("Dialog", "Самоед"))
        self.checkBox_2.setText(_translate("Dialog", "Пудель"))
        self.checkBox_3.setText(_translate("Dialog", "Сенбернар"))
        self.checkBox_4.setText(_translate("Dialog", "Аляскинский маломут"))
        self.checkBox_5.setText(_translate("Dialog", "Дог"))
        self.pushButton.setText(_translate("Dialog", "Ответить"))


class ThirdQuestNature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 620)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 451, 161))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 220, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 390, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 280, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Как называется дикая\n"
                                                "лошадь:"))
        self.pushButton.setText(_translate("Dialog", "Ответить"))
        self.label_2.setText(_translate("Dialog", "Ответ писать в именительном\n"
                                                  "падеже с большой буквы"))
