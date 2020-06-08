# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.schedule_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.schedule_menu_button.setGeometry(QtCore.QRect(475, 75, 200, 125))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(16)
        self.schedule_menu_button.setFont(font)
        self.schedule_menu_button.setObjectName("schedule_menu_button")
        self.scan_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.scan_menu_button.setGeometry(QtCore.QRect(125, 75, 200, 125))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(16)
        self.scan_menu_button.setFont(font)
        self.scan_menu_button.setObjectName("scan_menu_button")
        # self.setting_menu_button = QtWidgets.QPushButton(self.centralwidget)
        # self.setting_menu_button.setGeometry(QtCore.QRect(300, 275, 200, 125))
        # font = QtGui.QFont()
        # font.setFamily("Avenir Heavy")
        # font.setPointSize(16)
        # self.setting_menu_button.setFont(font)
        # self.setting_menu_button.setObjectName("setting_menu_button")
        self.schedule_view_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.schedule_view_menu_button.setGeometry(QtCore.QRect(300, 275, 200, 125))
        font = QtGui.QFont()
        font.setFamily("Avenir Heavy")
        font.setPointSize(16)
        self.schedule_view_menu_button.setFont(font)
        self.schedule_view_menu_button.setObjectName("schedule_view_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        #self.menubar.setObjectName("menubar")
        #self.menuabc = QtWidgets.QMenu(self.menubar)
        #self.menuabc.setObjectName("menuabc")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.actionScan = QtWidgets.QAction(MainWindow)
        #self.actionScan.setObjectName("actionScan")
        #self.actionExit = QtWidgets.QAction(MainWindow)
        #self.actionExit.setObjectName("actionExit")
        #self.menuabc.addAction(self.actionScan)
        #self.menuabc.addAction(self.actionExit)
        #self.menubar.addAction(self.menuabc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tick Tock"))
        self.schedule_menu_button.setText(_translate("MainWindow", "Schedule"))
        self.scan_menu_button.setText(_translate("MainWindow", "Scan"))
        # self.setting_menu_button.setText(_translate("MainWindow", "Settings"))
        self.schedule_view_menu_button.setText(_translate("MainWindow", "View Schedule"))
        #self.menuabc.setTitle(_translate("MainWindow", "File"))
        #self.actionScan.setText(_translate("MainWindow", "Scan"))
        #self.actionExit.setText(_translate("MainWindow", "Exit"))
