import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal,)
import json
import main_interface
import schedule_interface
import scan_interface
import settings_interface
import confirm_interface
import confirmed_interface
import re
import time, sched, threading
import pygame
from main_interface import *
from schedule_interface import *
from scan_interface import *
from settings_interface import *
from confirm_interface import *
from confirmed_interface import *
from selfinputselect import *
from string import digits
from text2digits import text2digits
import psutil
import schedule
from time import sleep

PI_ACTIVE = True
ALARM = True
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Tick-Tock-961ea96035ea.json"
 
try:
    import picamera
    import picamera.array
    import RPi.GPIO as GPIO
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Desktop/Tick_Tock/Tick-Tock-961ea96035ea.json"
except ModuleNotFoundError as e:
    PI_ACTIVE = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm=GPIO.PWM(13, 50)
pin = 13    
pwm.start(0)

class MainMenu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__()
        self.setupUi(self)
        if PI_ACTIVE:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(12,GPIO.OUT)
            GPIO.setup(16,GPIO.OUT)
        
        self.schedule_menu_button.clicked.connect(self.openScheduleWindow)
        self.scan_menu_button.clicked.connect(self.openScanWindow)
        self.setting_menu_button.clicked.connect(self.openSettingWindow) 

    def openScheduleWindow(self):
        self.schedm = PrescriptionSelectMenu()
        self.schedm.show()
        self.hide()

    def openScanWindow(self):
        self.scanm = ScanMenu()
        self.scanm.show()
        self.hide()

    def openSettingWindow(self):
        self.setm = SettingMenu()
        self.setm.show()
        self.hide()

class ScanMenu(QtWidgets.QDialog, Ui_ScanWindow):
    
    def __init__(self, parent=None):
        super(ScanMenu, self).__init__()
        self.setupUi(self)
        self.scan_button.setVisible(False)
        self.prescriptionNumber = 0
        self.prescription_button_1.clicked.connect(self.onPrescription1Click)
        self.prescription_button_2.clicked.connect(self.onPrescription2Click)
        self.scan_button.clicked.connect(self.onScanButtonClick)
        self.home_button.clicked.connect(self.openMainWindow) 
    
    def openMainWindow(self):
        try:
            self.camFeed.quit()
        except:
            None
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
        
    def onPrescription1Click(self):
        self.prescriptionNumber = 1
        self.startScan()
        
    def onPrescription2Click(self):
        self.prescriptionNumber = 2
        self.startScan()
        
    def startScan(self):
        if PI_ACTIVE:
            self.camFeed = CameraStream(self)
            self.camFeed.start()
        self.scan_button.setVisible(True)
        self.prescription_label.setVisible(False)
        self.prescription_button_1.setVisible(False)
        self.prescription_button_2.setVisible(False)
        
    def onScanButtonClick(self):
        try:
            if PI_ACTIVE:
                if self.camFeed is not None:
                    self.camFeed.getCurrentImage()
            prescriptionInfo = self.getPrescriptionFromImage()
            self.launchConfirmScreen(prescriptionInfo, self.prescriptionNumber)
        except:
            self.camFeed.quit()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Prescription not recognized.\nPlease scan again.")
            msgBox.exec()
            self.startScan() 
           
    def getPrescriptionFromImage(self):
        imageText = self.detect_text("prescription.jpg")
        print (imageText)
        return self.detect_prescription(imageText)
        
    def detect_text(self, path):
        """Detects text in the file."""
        from google.cloud import vision
        import io
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        del response
        return texts[0].description
            
    def detect_prescription(self, text):
        import boto3
        client = boto3.client(service_name='comprehendmedical', region_name='us-east-1')
        result = client.detect_entities(Text = text)
        entities = result['Entities'];
        for entity in entities:
            print('Entity', entity)
        return entities

    def launchConfirmScreen(self, prescriptionInfo, prescriptionNumber):
        self.confm = ConfirmMenu()
        if PI_ACTIVE:
            self.camFeed.quit()
        self.confm.show()
        self.confm.showScheduleInfo(prescriptionInfo, prescriptionNumber)
        self.hide()


class SettingMenu(QtWidgets.QDialog, Ui_SettingWindow):
    def __init__(self, parent=None):
        super(SettingMenu, self).__init__()
        self.setupUi(self)
        self.home_button.clicked.connect(self.openMainWindow) 
    
    def openMainWindow(self):
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
        
class ConfirmedMenu(QtWidgets.QDialog, Ui_ConfirmedWindow):
    def __init__(self, parent=None):
        super(ConfirmedMenu, self).__init__()
        self.setupUi(self)
        self.medication_text.setText("thing")
        self.retake_button.clicked.connect(self.openScanWindow)
        self.home_button.clicked.connect(self.openMainWindow)
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.alarm = pygame.mixer.Sound("alarm.wav")
        self.alarm.set_volume(0.15)

    def openMainWindow(self):
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
        
    def openScanWindow(self):
        self.scanm = ScanMenu()
        self.scanm.show()
        self.hide()
        
    def importPrescription(self, info, times, times24):
        prescriptionText =  info[1] + ", " + info[2] + " times " + info[3] + ", for " + info[4] + " " + info[5]
        self.medication_text.setText(prescriptionText)
        if info[0] == 1:
            self.prescription_label.setText("Prescription 1")
        if info[0] == 2:
            self.prescription_label.setText("Prescription 2")
        time_spins = {
                    1: self.time_spin_1,
                    2: self.time_spin_2,
                    3: self.time_spin_3,
                    4: self.time_spin_4,
                    5: self.time_spin_5,
                }
        for i, alarm_time in enumerate(times):
            if alarm_time != '':
                time_spins[i + 1].setText(times[i])
                schedule.every().day.at(times24[i]).do(self.alarmOn, info[0])
        t = threading.Timer(1.0, lambda: self.wait())
        t.start()

    def wait(self):
        print("hello")
        while ALARM:
            schedule.run_pending()
            time.sleep(1)

    def alarmOn(self, number):##runs alarm (do whatever open thing here probably)
        ALARM = False
        t = threading.Timer(5.0, lambda: self.alarmOff(number))#prescription number
        if PI_ACTIVE:
            if number == 1:
                GPIO.output(12, GPIO.HIGH)
            if number == 2:
                GPIO.output(16, GPIO.HIGH)
        self.alarm.play(-1)
        duty = 100 / 18 + 2
        GPIO.output(13, True)
        pwm.ChangeDutyCycle(duty)
        sleep(2)
        GPIO.output(13, False)
        pwm.ChangeDutyCycle(0)
        pillonsensor = 1
        while (pillonsensor == 1):
            GPIO.setup(22, GPIO.IN)
            val = GPIO.input(22)
            if val == 1:
                print ("on")
            else:
                print ("off")
                pillonsensor = 0
                self.alarm.stop()
            sleep(0.5)
        
        pillonsensor = 0
        GPIO.setup(22, GPIO.IN)
        GPIO.setup(27, GPIO.IN)
        val = GPIO.input(22)
        val2 = GPIO.input(27)
        while (pillonsensor == 0):
            val = GPIO.input(27)
            val2 = GPIO.input(22)
            if val == 1 and val2 == 1:
                print ("closed")
                pillonsensor = 1
                duty = 0 / 18 + 2
                GPIO.output(13, True)
                pwm.ChangeDutyCycle(duty)
                sleep(2)
                GPIO.output(13, False)
                pwm.ChangeDutyCycle(0)
            else:
                print ("open")
            sleep(0.5)
        t.start()

    def alarmOff(self, number):#turns alarm off(close)
        if PI_ACTIVE:
            if number == 1:
                GPIO.output(12, GPIO.LOW)
            if number == 2:
                GPIO.output(16, GPIO.LOW)
        self.alarm.stop()
        ALARM = True
        
class PrescriptionSelectMenu(QtWidgets.QDialog, Ui_PrescriptionSelectWindow):
    def __init__(self, parent=None):
        super(PrescriptionSelectMenu, self).__init__()
        self.setupUi(self)
        self.prescription_one.clicked.connect(lambda: self.setPrescriptionNumber(1))
        self.prescription_two.clicked.connect(lambda: self.setPrescriptionNumber(2))
        self.home_button.clicked.connect(self.openMainWindow)
    
    def openMainWindow(self):
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
        
    def setPrescriptionNumber(self, number):
        self.sched = ScheduleMenu()
        self.sched.show()
        self.sched.prescriptionNumber = number
        self.hide()
        
        
class ScheduleMenu(QtWidgets.QDialog, Ui_ScheduleWindow):
    def __init__(self, parent=None):
        super(ScheduleMenu, self).__init__()
        self.setupUi(self)
        self.prescriptionNumber = 0
        #self.uiList = QListWidget()
        #self.uiList.insertItem(1, 'Prescription Select')
        #self.uiList.insertItem(2, 'Prescription Entry')
        #self.stack = QtWidgets.QStackedWidget(self)
        #self.stack.addWidget(PrescriptionSelectMenu(self))
        #self.stack.addWidget(self)
        #self.stackedWidget.setCurrentIndex(0)
        #self.show()
        #self.setCentralWidget(self.stack)
        #self.runPrescriptionSelection()
        if PI_ACTIVE:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(12,GPIO.OUT)
            GPIO.setup(16,GPIO.OUT)
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.alarm = pygame.mixer.Sound("alarm.wav")
        self.alarm.set_volume(0.15)
        currentTime = QtCore.QTime().currentTime()
        self.time_spin_1.setTime(currentTime)
        self.SelfInputComplete.clicked.connect(self.schedule_created)
        self.home_button.clicked.connect(self.openMainWindow)

    def schedule_created(self):
        if self.prescriptionNumber == 1:
            prescription = "Prescription 1"
        elif self.prescriptionNumber == 2:
            prescription = "Prescription 2"
        alarm_time = self.time_spin_1.time().toString("hh:mm")
        schedule.every().day.at(alarm_time).do(self.alarmOn, self.prescriptionNumber)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Schedule created for " + prescription)
        t = threading.Timer(1.0, lambda: self.wait())#prescription number
        t.start()
        msgBox.exec()

    def wait(self):
        print("hello1")
        while 1:
            schedule.run_pending()
            time.sleep(1)

    def openMainWindow(self):
        for proc in psutil.process_iter():
            if proc.name() == "matchbox-keyboard":
                proc.kill()
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
    
        
    def alarmOn(self, number):#open compartment here(alarm)
        ALARM = False
        t = threading.Timer(5.0, lambda: self.alarmOff(self.prescriptionNumber))#prescription number
        if PI_ACTIVE:
            if number == 1:
                GPIO.output(12, GPIO.HIGH)
            if number == 2:
                GPIO.output(16, GPIO.HIGH)
        self.alarm.play(-1)
        duty = 100 / 18 + 2
        GPIO.output(13, True)
        pwm.ChangeDutyCycle(duty)
        sleep(2)
        GPIO.output(13, False)
        pwm.ChangeDutyCycle(0)
        pillonsensor = 1
        while (pillonsensor == 1):
            GPIO.setup(22, GPIO.IN)
            val = GPIO.input(22)
            if val == 1:
                print ("on")
            else:
                print ("off")
                pillonsensor = 0
                self.alarm.stop()
            sleep(0.5)
        
        pillonsensor = 0
        GPIO.setup(22, GPIO.IN)
        GPIO.setup(27, GPIO.IN)
        val = GPIO.input(22)
        val2 = GPIO.input(27)
        while (pillonsensor == 0):
            val = GPIO.input(27)
            val2 = GPIO.input(22)
            if val == 1 and val2 == 1:
                print ("closed")
                pillonsensor = 1
                duty = 0 / 18 + 2
                GPIO.output(13, True)
                pwm.ChangeDutyCycle(duty)
                sleep(2)
                GPIO.output(13, False)
                pwm.ChangeDutyCycle(0)
            else:
                print ("open")
            sleep(0.5)
        t.start()

    def alarmOff(self, number):
        if PI_ACTIVE:
            if number == 1:
                GPIO.output(12, GPIO.LOW)
            if number == 2:
                GPIO.output(16, GPIO.LOW)
        self.alarm.stop()
        ALARM = True

            
class ConfirmMenu(QtWidgets.QDialog, Ui_ConfirmWindow):
    def __init__(self, parent=None):
        super(ConfirmMenu, self).__init__()
        self.setupUi(self)
        self.prescriptionNumber = 0
        self.confirm_button.clicked.connect(self.schedule_created) #clean this up later
        self.retake_button.clicked.connect(self.openScanWindow)
        #clean this up
        if PI_ACTIVE:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(12,GPIO.OUT)
            GPIO.setup(16,GPIO.OUT)
        self.home_button.clicked.connect(self.openMainWindow) 
    
    def openMainWindow(self):
        for proc in psutil.process_iter():
            if proc.name() == "matchbox-keyboard":
                proc.kill()
        self.mm = MainMenu()
        self.mm.show()
        self.hide()
    
        

    def showScheduleInfo(self, info, prescriptionNumber):
        self.prescriptionNumber = prescriptionNumber
        self.prescription_label.setText("Prescription " + str(prescriptionNumber))
        
        medication = ''
        strength = ''
        scheduleFrequency1 = ''
        scheduleFrequency2 = ''
        scheduleDuration1 = ''
        scheduleDuration2 = ''
        scheduleFrequency = ''
        scheduleDuration = ''
        
        t2d = text2digits.Text2Digits()
        currentTime = QtCore.QTime().currentTime()
        self.time_spins = {
                    1: self.time_spin_1,
                    2: self.time_spin_2,
                    3: self.time_spin_3,
                    4: self.time_spin_4,
                    5: self.time_spin_5,
                }
        for time_spin in self.time_spins.values():
            time_spin.setVisible(False)
        self.time_spin_1.setVisible(True)

        try:
            for entity in info:
                if entity['Category'] == 'MEDICATION':
                    for attribute in entity['Attributes']:
                        if attribute['Type'] == 'STRENGTH':
                            strength = attribute['Text']
                        if attribute['Type'] == 'FREQUENCY':
                            scheduleFrequency = attribute['Text']
                        if attribute['Type'] =='DURATION': 
                            scheduleDuration = attribute['Text']
                    medication = entity['Text'] + ' ' + strength
            
            scheduleFrequency = t2d.convert(scheduleFrequency)
            scheduleFrequencyNumbers = re.findall("\d+", scheduleFrequency)
            if len(scheduleFrequencyNumbers) != 0:
                scheduleFrequency1 = scheduleFrequencyNumbers[0]
                remove_digits = scheduleFrequency.maketrans('', '', digits)
                scheduleFrequency2 = (scheduleFrequency.translate(remove_digits)).replace('times ', '')
                #detect 'a day, week, month' or 'every other __' instead
            elif('once' in scheduleFrequency):
                    scheduleFrequency1 = str(1)
                    scheduleFrequency2 = scheduleFrequency.replace('once ','')
            elif('twice' in scheduleFrequency):
                    scheduleFrequency1 = str(2)
                    scheduleFrequency2 = scheduleFrequency.replace('twice ','')
            else:
                scheduleFrequency2 = scheduleFrequency
                scheduleFrequency1 = str(1)
            
            scheduleDuration = t2d.convert(scheduleDuration)
            scheduleDurationNumbers = re.findall("\d+", scheduleDuration)
            if len(scheduleDurationNumbers) != 0:
                scheduleDuration1 = scheduleDurationNumbers[0]
                remove_digits = scheduleDuration.maketrans('', '', digits)
                scheduleDuration2 = scheduleDuration.translate(remove_digits)
            if scheduleDuration1 == '':
               None
               #handling code if no number   
        except:
            scheduleFrequency1 = str(1)
            scheduleFrequency2 = 'a day'
            scheduleDuration1 = str(1)
            scheduleDuration2 = 'weeks'
        time1 = currentTime
        
        self.scheduleFrequency1_int = int(scheduleFrequency1)
        if self.scheduleFrequency1_int > 1:
            for i in range(2, self.scheduleFrequency1_int + 1):
                print(i)
                time1 = time1.addSecs(86400/self.scheduleFrequency1_int)
                self.time_spins[i].setVisible(True)
                self.time_spins[i].setTime(time1)
                #time_spin_new = QtWidgets.QTimeEdit(time1, self)
                #time_spin_new.setGeometry(QtCore.QRect(635, (175 + 45 * (scheduleFrequency1_int - 1)), 85, 30))
                #time_spin_new.move(635, (175 + 45 * (scheduleFrequency1_int - 1)))
                #font = QtGui.QFont()
                #font.setFamily("Avenir Medium")
                #font.setPointSize(10)
                #time_spin_new.setFont(font)
                #time_spin_new.setObjectName("time_spin_new_" + str(scheduleFrequency1_int - 1))
                #time1 = time1.addSecs(86400/scheduleFrequency1_int)
                #time_spin_new.setTime(time1) 
                
        self.time_spin_1.setTime(currentTime)
        self.medication_text.setText(medication)    
        self.frequency_spin.setSpecialValueText(scheduleFrequency1)
        self.frequency_combo.setCurrentText(scheduleFrequency2)
        self.duration_spin.setSpecialValueText(scheduleDuration1)
        self.duration_combo.setCurrentText(scheduleDuration2)
    
    def schedule_created(self):
        #t = threading.Timer(10.0, lambda: self.alarmOn(self.prescriptionNumber))#prescription number
        #t.start()
        times = ['','','','','']
        times24 = ['','','','','']
        medicationInfo =  [self.prescriptionNumber,
                           self.medication_text.text(),
                           self.frequency_spin.text(),
                           str(self.frequency_combo.currentText()),
                           self.duration_spin.text(),
                           str(self.duration_combo.currentText())]
        for i in range (0, self.scheduleFrequency1_int):
            times[i] = self.time_spins[i + 1].time().toString("hh:mm AP")
            times24[i] = self.time_spins[i + 1].time().toString("hh:mm")
        for proc in psutil.process_iter():
            if proc.name() == "matchbox-keyboard":
                proc.kill()
        self.confdm = ConfirmedMenu()
        self.confdm.show()
        self.hide()
        self.confdm.importPrescription(medicationInfo, times, times24)
       

    
    def openScheduleWindow(self):
        for proc in psutil.process_iter():
            if proc.name() == "matchbox-keyboard":
                proc.kill()
        self.schedm = ScheduleMenu()
        self.schedm.show()
        self.hide()

    def openScanWindow(self):
        for proc in psutil.process_iter():
            if proc.name() == "matchbox-keyboard":
                proc.kill()
        self.scanm = ScanMenu()
        self.scanm.show()
        self.hide()
        
class CameraStream(QThread):

    def __init__(self, parent):
        super(self.__class__, self).__init__()

    def getCurrentImage(self):
        self.camera.capture('prescription.jpg')

    def quit(self):
        super(self.__class__, self).quit()
        self.camera.close()

    def run(self):
        self.camera = picamera.PiCamera()
        self.camera.rotation = 180
        self.camera.start_preview(fullscreen=False, window=(25, 45,
                                  750, 375))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mm = MainMenu()
    mm.show()
    sys.exit(app.exec_())
