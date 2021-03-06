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

class Ui_ScheduleViewWindow(object):
    def setupUi(self, ScheduleViewWindow):
        ScheduleViewWindow.setObjectName("ScheduleViewWindow")
        ScheduleViewWindow.resize(800, 486)
        self.information_label = QtWidgets.QLabel(ScheduleViewWindow)
        self.information_label.setGeometry(QtCore.QRect(180, 20, 440, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.information_label.setFont(font)
        self.information_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_label.setObjectName("information_label")
#         self.medication_label = QtWidgets.QLabel(ScheduleViewWindow)
#         self.medication_label.setGeometry(QtCore.QRect(90, 135, 111, 30))
#         font = QtGui.QFont()
#         font.setFamily("Avenir Heavy")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.medication_label.setFont(font)
#         self.medication_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.medication_label.setObjectName("medication_label")
        self.medication_text = QtWidgets.QLabel(ScheduleViewWindow)
        self.medication_text.setGeometry(QtCore.QRect(90, 150, 420, 60))
        self.medication_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.medication_text.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.medication_text.setFont(font)
        self.medication_text.setText("")
        self.medication_text.setObjectName("medication_text")
        
        self.time_label = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_label.setGeometry(QtCore.QRect(525, 150, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_label.setFont(font)
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        
        
        self.time_spin_1 = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_spin_1.setGeometry(QtCore.QRect(575, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_spin_1.setFont(font)
        self.time_spin_1.setObjectName("time_spin_1")
        
        self.time_spin_2 = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_spin_2.setGeometry(QtCore.QRect(575, 195, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_spin_2.setFont(font)
        self.time_spin_2.setObjectName("time_spin_2")
        
        self.time_spin_3 = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_spin_3.setGeometry(QtCore.QRect(575, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_spin_3.setFont(font)
        self.time_spin_3.setObjectName("time_spin_3")
        
        self.time_spin_4 = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_spin_4.setGeometry(QtCore.QRect(575, 285, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_spin_4.setFont(font)
        self.time_spin_4.setObjectName("time_spin_4")
        
        self.time_spin_5 = QtWidgets.QLabel(ScheduleViewWindow)
        self.time_spin_5.setGeometry(QtCore.QRect(575, 325, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(15)
        self.time_spin_5.setFont(font)
        self.time_spin_5.setObjectName("time_spin_5")
        
#         self.confirm_button = QtWidgets.QPushButton(ScheduleViewWindow)
#         self.confirm_button.setGeometry(QtCore.QRect(170, 320, 135, 60))
#         font = QtGui.QFont()
#         font.setFamily("Avenir Heavy")
#         font.setPointSize(10)
#         self.confirm_button.setFont(font)
#         self.confirm_button.setObjectName("confirm_button")
        self.retake_button = QtWidgets.QPushButton(ScheduleViewWindow)
        self.retake_button.setGeometry(QtCore.QRect(332, 320, 135, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.retake_button.setFont(font)
        self.retake_button.setObjectName("retake_button")
        self.home_button = QtWidgets.QPushButton(ScheduleViewWindow)
        self.home_button.setGeometry(QtCore.QRect(20, 20, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setObjectName("home_button")
        
        self.duration_label = QtWidgets.QLabel(ScheduleViewWindow)
        self.duration_label.setGeometry(QtCore.QRect(380, 225, 31, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(12)
        self.duration_label.setFont(font)
        #self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.duration_spin = QtWidgets.QLabel(ScheduleViewWindow)
        self.duration_spin.setGeometry(QtCore.QRect(410, 225, 42, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(12)
        self.duration_spin.setFont(font)
        self.duration_spin.setObjectName("duration_spin")
        self.duration_combo = QtWidgets.QLabel(ScheduleViewWindow)
        self.duration_combo.setGeometry(QtCore.QRect(470, 225, 69, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Medium")
        font.setPointSize(12)
        self.duration_combo.setFont(font)
        self.duration_combo.setObjectName("duration_combo")
        self.prescription_label = QtWidgets.QLabel(ScheduleViewWindow)
        self.prescription_label.setGeometry(QtCore.QRect(90, 100, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_label.setFont(font)
        self.prescription_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.prescription_label.setObjectName("prescription_label")

        

        self.retranslateUi(ScheduleViewWindow)
        QtCore.QMetaObject.connectSlotsByName(ScheduleViewWindow)
        


    def retranslateUi(self, ScheduleViewWindow):
        _translate = QtCore.QCoreApplication.translate
        ScheduleViewWindow.setWindowTitle(_translate("ScheduleViewWindow", "Dialog"))
        self.information_label.setText(_translate("ScheduleViewWindow", "Current Schedule"))
        self.medication_text.setText(_translate("ScheduleViewWindow", "Advil 20mg, 2 times a day, for 3 weeks"))
#        self.frequency_spin.setText(_translate("ScheduleViewWindow", "1"))
#        self.frequency_label.setText(_translate("ScheduleViewWindow", "times"))
#        self.confirm_button.setText(_translate("ScheduleViewWindow", "Confirm"))
        self.retake_button.setText(_translate("ScheduleViewWindow", "Retake"))
        self.prescription_label.setText(_translate("ScheduleViewWindow", "Prescription 1"))
        self.home_button.setText(_translate("ScheduleViewWindow", "Home"))
#        self.frequency_combo.setText(_translate("ScheduleViewWindow", "a day"))
        self.time_label.setText(_translate("ScheduleViewWindow", "at"))
        #self.time_spin.setTime(_translate("ScheduleViewWindow", QtCore.QTime()))
 #       self.duration_label.setText(_translate("ScheduleViewWindow", "for"))
#        self.duration_combo.setText(_translate("ScheduleViewWindow", "days"))
#        self.time_spin_1.setText(_translate("ScheduleViewWindow", "12:15 AM"))
#        self.time_spin_2.setText(_translate("ScheduleViewWindow", "12:15 PM"))
#        self.time_spin_3.setText(_translate("ScheduleViewWindow", "05:15 AM"))
        

class ScheduleViewWindow(QtWidgets.QMainWindow, Ui_ScheduleViewWindow):
    def __init__(self, parent=None):
        super(ScheduleViewWindow,self).__init__(parent=parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mm = ScheduleViewWindow()
    mm.show()
    sys.exit(app.exec_())



