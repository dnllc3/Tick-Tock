# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(802, 480)
        self.home_button = QtWidgets.QPushButton(SettingWindow)
        self.home_button.setGeometry(QtCore.QRect(15, 15, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Settings"))
        self.home_button.setText(_translate("SettingWindow", "Home"))
