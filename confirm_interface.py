# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import subprocess
import psutil

class Ui_ConfirmWindow(object):
    def setupUi(self, ConfirmWindow):
        ConfirmWindow.setObjectName("ConfirmWindow")
        ConfirmWindow.resize(800, 486)
        self.information_label = QtWidgets.QLabel(ConfirmWindow)
        self.information_label.setGeometry(QtCore.QRect(180, 20, 440, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.information_label.setFont(font)
        self.information_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_label.setObjectName("information_label")
        self.medication_label = QtWidgets.QLabel(ConfirmWindow)
        self.medication_label.setGeometry(QtCore.QRect(90, 135, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.medication_label.setFont(font)
        self.medication_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.medication_label.setObjectName("medication_label")
        self.medication_text = self.MatchBoxLineEdit(ConfirmWindow)
        self.medication_text.setGeometry(QtCore.QRect(90, 175, 241, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.medication_text.setFont(font)
        self.medication_text.setText("")
        self.medication_text.setObjectName("medication_text")
        self.frequency_spin = QtWidgets.QSpinBox(ConfirmWindow)
        self.frequency_spin.setGeometry(QtCore.QRect(380, 175, 42, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.frequency_spin.setFont(font)
        self.frequency_spin.setObjectName("frequency_spin")
        self.frequency_label = QtWidgets.QLabel(ConfirmWindow)
        self.frequency_label.setGeometry(QtCore.QRect(430, 175, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.frequency_label.setFont(font)
        self.frequency_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frequency_label.setObjectName("frequency_label")
        
        self.time_label = QtWidgets.QLabel(ConfirmWindow)
        self.time_label.setGeometry(QtCore.QRect(595, 175, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        
        self.time_spin_1 = QtWidgets.QTimeEdit(ConfirmWindow)
        self.time_spin_1.setGeometry(QtCore.QRect(635, 175, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(10)
        self.time_spin_1.setFont(font)
        self.time_spin_1.setObjectName("time_spin_1")
        
        self.time_spin_2 = QtWidgets.QTimeEdit(ConfirmWindow)
        self.time_spin_2.setGeometry(QtCore.QRect(635, 220, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(10)
        self.time_spin_2.setFont(font)
        self.time_spin_2.setObjectName("time_spin_2")
        
        self.time_spin_3 = QtWidgets.QTimeEdit(ConfirmWindow)
        self.time_spin_3.setGeometry(QtCore.QRect(635, 265, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(10)
        self.time_spin_3.setFont(font)
        self.time_spin_3.setObjectName("time_spin_3")
        
        self.time_spin_4 = QtWidgets.QTimeEdit(ConfirmWindow)
        self.time_spin_4.setGeometry(QtCore.QRect(635, 310, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(10)
        self.time_spin_4.setFont(font)
        self.time_spin_4.setObjectName("time_spin_4")
        
        self.time_spin_5 = QtWidgets.QTimeEdit(ConfirmWindow)
        self.time_spin_5.setGeometry(QtCore.QRect(635, 355, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(10)
        self.time_spin_5.setFont(font)
        self.time_spin_5.setObjectName("time_spin_5")
        
        self.confirm_button = QtWidgets.QPushButton(ConfirmWindow)
        self.confirm_button.setGeometry(QtCore.QRect(165, 320, 135, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.retake_button = QtWidgets.QPushButton(ConfirmWindow)
        self.retake_button.setGeometry(QtCore.QRect(500, 320, 135, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.retake_button.setFont(font)
        self.retake_button.setObjectName("retake_button")
        self.prescription_label = QtWidgets.QLabel(ConfirmWindow)
        self.prescription_label.setGeometry(QtCore.QRect(90, 85, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_label.setFont(font)
        self.prescription_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.prescription_label.setObjectName("prescription_label")
        self.frequency_combo = QtWidgets.QComboBox(ConfirmWindow)
        self.frequency_combo.setGeometry(QtCore.QRect(480, 175, 115, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.frequency_combo.setFont(font)
        self.frequency_combo.setCurrentText("")
        self.frequency_combo.setObjectName("frequency_combo")
        self.frequency_combo.setEditable(True)
        self.frequency_combo.addItem("")
        self.frequency_combo.addItem("")
        self.home_button = QtWidgets.QPushButton(ConfirmWindow)
        self.home_button.setGeometry(QtCore.QRect(20, 20, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")
        
        self.duration_label = QtWidgets.QLabel(ConfirmWindow)
        self.duration_label.setGeometry(QtCore.QRect(380, 225, 31, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_label.setFont(font)
        #self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.duration_spin = QtWidgets.QSpinBox(ConfirmWindow)
        self.duration_spin.setGeometry(QtCore.QRect(410, 225, 42, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_spin.setFont(font)
        self.duration_spin.setObjectName("duration_spin")
        self.duration_combo = QtWidgets.QComboBox(ConfirmWindow)
        self.duration_combo.setGeometry(QtCore.QRect(470, 225, 69, 30))
        self.duration_combo.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_combo.setFont(font)
        self.duration_combo.setCurrentText("")
        self.duration_combo.setObjectName("duration_combo")
        self.duration_combo.addItem("")
        self.duration_combo.addItem("")
        

        self.retranslateUi(ConfirmWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfirmWindow)
        
    class MatchBoxLineEdit(QtWidgets.QLineEdit):
        def focusInEvent(self, e):
            try:
                subprocess.Popen(["matchbox-keyboard"])
            except FileNotFoundError:
                pass
        
        def focusOutEvent(self, e):
            subprocess.Popen(["matchbox-keyboard"]).kill()

    def retranslateUi(self, ConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfirmWindow.setWindowTitle(_translate("ConfirmWindow", "Dialog"))
        self.information_label.setText(_translate("ConfirmWindow", "Is the following information correct?"))
        self.medication_label.setText(_translate("ConfirmWindow", "Medication"))
        self.frequency_spin.setSpecialValueText(_translate("ConfirmWindow", "1"))
        self.frequency_label.setText(_translate("ConfirmWindow", "times"))
        self.confirm_button.setText(_translate("ConfirmWindow", "Confirm"))
        self.retake_button.setText(_translate("ConfirmWindow", "Retake"))
        self.prescription_label.setText(_translate("ConfirmWindow", "Prescription 1"))
        self.home_button.setText(_translate("ConfrimWindow", "Home"))
        self.frequency_combo.setItemText(0, _translate("ConfirmWindow", "a day"))
        self.frequency_combo.setItemText(1, _translate("ConfirmWindow", "every other day"))
        self.time_label.setText(_translate("ConfirmWindow", "at"))
        #self.time_spin.setTime(_translate("ConfirmWindow", QtCore.QTime()))
        self.duration_label.setText(_translate("ConfirmWindow", "for"))
        self.duration_combo.setItemText(0, _translate("ConfirmWindow", "days"))
        self.duration_combo.setItemText(1, _translate("ConfirmWindow", "weeks"))

class ConfirmWindow(QtWidgets.QMainWindow, Ui_ConfirmWindow):
    def __init__(self, parent=None):
        super(ConfirmWindow,self).__init__(parent=parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mm = ConfirmWindow()
    mm.show()
    sys.exit(app.exec_())



