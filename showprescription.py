# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import psutil

class Ui_ConfirmWindow(object):
    def setupUi(self, ConfirmWindow):
        ConfirmWindow.setObjectName("ConfirmWindow")
        ConfirmWindow.resize(800, 486)
        self.medication_text = self.MatchBoxLineEdit(ConfirmWindow)
        self.medication_text.setGeometry(QtCore.QRect(90, 175, 241, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.medication_text.setFont(font)
        self.medication_text.setText("")
        self.medication_text.setObjectName("medication_text")
        self.schedule_label = QtWidgets.QLabel(ConfirmWindow)
        self.schedule_label.setGeometry(QtCore.QRect(380, 135, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label.setFont(font)
        self.schedule_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.schedule_label.setObjectName("schedule_label")
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
        self.confirm_button = QtWidgets.QPushButton(ConfirmWindow)
        self.confirm_button.setGeometry(QtCore.QRect(170, 320, 135, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.frequency_combo = QtWidgets.QComboBox(ConfirmWindow)
        self.frequency_combo.setGeometry(QtCore.QRect(480, 175, 69, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.frequency_combo.setFont(font)
        self.frequency_combo.setCurrentText("")
        self.frequency_combo.setObjectName("frequency_combo")
        self.frequency_combo.setEditable(True)
        self.frequency_combo.addItem("")
        self.frequency_combo.addItem("")
        self.duration_label = QtWidgets.QLabel(ConfirmWindow)
        self.duration_label.setGeometry(QtCore.QRect(550, 175, 31, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_label.setFont(font)
        self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.duration_spin = QtWidgets.QSpinBox(ConfirmWindow)
        self.duration_spin.setGeometry(QtCore.QRect(580, 175, 42, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_spin.setFont(font)
        self.duration_spin.setObjectName("duration_spin")
        self.duration_combo = QtWidgets.QComboBox(ConfirmWindow)
        self.duration_combo.setGeometry(QtCore.QRect(630, 175, 69, 30))
        self.duration_combo.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(9)
        self.duration_combo.setFont(font)
        self.duration_combo.setCurrentText("")
        self.duration_combo.setObjectName("duration_combo")
        self.duration_combo.addItem("")
        self.duration_combo.addItem("")
        self.home_button = QtWidgets.QPushButton(ConfirmWindow)
        self.home_button.setGeometry(QtCore.QRect(20, 20, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")

        self.retranslateUi(ConfirmWindow)
        self.frequency_combo.setCurrentIndex(-1)
        self.duration_combo.setCurrentIndex(-1)
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
        
        self.schedule_label.setText(_translate("ConfirmWindow", "Schedule"))
        self.frequency_spin.setSpecialValueText(_translate("ConfirmWindow", "1"))
        self.frequency_label.setText(_translate("ConfirmWindow", "times"))
        #self.prescription_label.setText(_translate("ConfirmWindow", "Prescription 1"))
        self.duration_label.setText(_translate("ConfirmWindow", "for"))
        self.home_button.setText(_translate("ConfrimWindow", "Home"))
        self.frequency_combo.setItemText(0, _translate("ConfirmWindow", "a day"))
        self.frequency_combo.setItemText(1, _translate("ConfirmWindow", "every other day"))
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


