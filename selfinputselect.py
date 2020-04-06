# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tick_tock_self_scanning_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrescriptionSelectWindow(object):
    def setupUi(self, SelfInputSelect):
        SelfInputSelect.setObjectName("SelfInputSelect")
        SelfInputSelect.resize(800, 600)
        font = QtGui.QFont()
        font.setItalic(False)
        SelfInputSelect.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SelfInputSelect)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 150, 600, 51))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        #self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.prescription_one = QtWidgets.QPushButton(self.centralwidget)
        self.prescription_one.setGeometry(QtCore.QRect(320, 230, 151, 50))
        self.prescription_one.setObjectName("prescription_one")
        self.prescription_two = QtWidgets.QPushButton(self.centralwidget)
        self.prescription_two.setGeometry(QtCore.QRect(320, 300, 151, 50))
        self.prescription_two.setObjectName("prescription_two")
        self.label.raise_()
        self.prescription_two.raise_()
        self.prescription_one.raise_()
        #SelfInputSelect.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SelfInputSelect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        #SelfInputSelect.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SelfInputSelect)
        self.statusbar.setObjectName("statusbar")
        #SelfInputSelect.setStatusBar(self.statusbar)     
        
        self.home_button = QtWidgets.QPushButton(SelfInputSelect)
        self.home_button.setGeometry(QtCore.QRect(15, 15, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")
        
        self.retranslateUi(SelfInputSelect)
        QtCore.QMetaObject.connectSlotsByName(SelfInputSelect)

    def retranslateUi(self, SelfInputSelect):
        _translate = QtCore.QCoreApplication.translate
        SelfInputSelect.setWindowTitle(_translate("SelfInputSelect", "SelfInputSelect"))
        self.label.setText(_translate("SelfInputSelect", "Which prescription would you like to input?"))
        self.prescription_one.setText(_translate("SelfInputSelect", "Prescription One"))
        self.prescription_two.setText(_translate("SelfInputSelect", "Prescription Two "))
        self.home_button.setText(_translate("SelfInputSelect", "Home"))


