# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scan.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScanWindow(object):
    def setupUi(self, ScanWindow):
        ScanWindow.setObjectName("ScanWindow")
        ScanWindow.resize(800, 480)
        self.scan_button = QtWidgets.QPushButton(ScanWindow)
        self.scan_button.setGeometry(QtCore.QRect(300, 400, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.scan_button.setFont(font)
        self.scan_button.setObjectName("scan_button")
        self.prescription_label = QtWidgets.QLabel(ScanWindow)
        self.prescription_label.setGeometry(QtCore.QRect(180, 50, 440, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_label.setFont(font)
        self.prescription_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prescription_label.setObjectName("prescription_label")
        self.prescription_button_2 = QtWidgets.QPushButton(ScanWindow)
        self.prescription_button_2.setGeometry(QtCore.QRect(500, 180, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_button_2.setFont(font)
        self.prescription_button_2.setObjectName("prescription_button_2")
        self.prescription_button_1 = QtWidgets.QPushButton(ScanWindow)
        self.prescription_button_1.setGeometry(QtCore.QRect(140, 180, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_button_1.setFont(font)
        self.prescription_button_1.setObjectName("prescription_button_1")
        self.home_button = QtWidgets.QPushButton(ScanWindow)
        self.home_button.setGeometry(QtCore.QRect(15, 15, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")
        
        self.retranslateUi(ScanWindow)
        QtCore.QMetaObject.connectSlotsByName(ScanWindow)

    def retranslateUi(self, ScanWindow):
        _translate = QtCore.QCoreApplication.translate
        ScanWindow.setWindowTitle(_translate("ScanWindow", "Scan"))
        self.scan_button.setText(_translate("ScanWindow", "Scan"))
        self.prescription_label.setText(_translate("ScanWindow", "Which prescription would you like to enter?"))
        self.prescription_button_2.setText(_translate("ScanWindow", "Prescription 2"))
        self.prescription_button_1.setText(_translate("ScanWindow", "Prescription 1"))
        self.home_button.setText(_translate("ScanWindow", "Home"))

