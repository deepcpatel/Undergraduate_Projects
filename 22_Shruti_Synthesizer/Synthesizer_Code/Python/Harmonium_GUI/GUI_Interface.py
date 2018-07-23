# pyQt5 installation Instruction :
#
# 1). Install pyQt5 by running - "sudo apt-get install python-pyqt5" for Python 2.7 and,
#                                "sudo apt-get install python-pyqt5" for Python 3

import os
import sys
import signal
import Handler as handle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from multiprocessing import Process
import Envelope_Generation_Sampling as env
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QMessageBox, QTextEdit, QDesktopWidget, QLabel

class CustomizedWindow(QWidget):
    
    def __init__(self, opt_str, hand, envelope):
        super(QWidget, self).__init__()
        self.title = 'Select the Shrutis'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 210
        self.opt_string = opt_str
        self.e = envelope
        self.h = hand
        self.initUI()        
        
    def initUI(self):   

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)   

        # Selection of Komal Re
        lbl1 = QLabel('Komal Re:', self)
        lbl1.move(10, 15)
        self.combo_komal_re = QComboBox(self)
        self.combo_komal_re.addItem("Ati Komal")
        self.combo_komal_re.addItem("Komal")
        self.combo_komal_re.move(80, 10)
        self.combo_komal_re.setCurrentIndex(self.opt_string[1]-2)
        self.combo_komal_re.activated[str].connect(self.onActivatedKomalRe)
        # Selection of Shuddh Re
        lbl2 = QLabel('Shuddh Re:', self)
        lbl2.move(190, 15)
        self.combo_shuddh_re = QComboBox(self)
        self.combo_shuddh_re.addItem("Shuddh")
        self.combo_shuddh_re.addItem("Teevra")
        self.combo_shuddh_re.move(270, 10)
        self.combo_shuddh_re.setCurrentIndex(self.opt_string[2]-4)
        self.combo_shuddh_re.activated[str].connect(self.onActivatedShuddhRe)
        # Selection of Komal Ga
        lbl3 = QLabel('Komal Ga:', self)
        lbl3.move(10, 50)
        self.combo_komal_ga = QComboBox(self)
        self.combo_komal_ga.addItem("Ati Komal")
        self.combo_komal_ga.addItem("Komal")
        self.combo_komal_ga.move(80, 45)
        self.combo_komal_ga.setCurrentIndex(self.opt_string[3]-6)
        self.combo_komal_ga.activated[str].connect(self.onActivatedKomalGa)
        # Selection of Shuddh Ga
        lbl4 = QLabel('Shuddh Ga:', self)
        lbl4.move(190, 50)
        self.combo_shuddh_ga = QComboBox(self)
        self.combo_shuddh_ga.addItem("Shuddh")
        self.combo_shuddh_ga.addItem("Teevra")
        self.combo_shuddh_ga.move(270, 45)
        self.combo_shuddh_ga.setCurrentIndex(self.opt_string[4]-8)
        self.combo_shuddh_ga.activated[str].connect(self.onActivatedShuddhGa)
        # Selection of Shuddh Ma
        lbl5 = QLabel('Shuddh Ma:', self)
        lbl5.move(10, 85)
        self.combo_shuddh_ma = QComboBox(self)
        self.combo_shuddh_ma.addItem("Shuddh Madhyam")
        self.combo_shuddh_ma.addItem("Ek Shruti Madhyam")
        self.combo_shuddh_ma.move(91, 80)
        self.combo_shuddh_ma.setCurrentIndex(self.opt_string[5]-10)
        self.combo_shuddh_ma.activated[str].connect(self.onActivatedShuddhMa)
        # Selection of Taar Ma
        lbl6 = QLabel('Taar Ma:', self)
        lbl6.move(260, 85)
        self.combo_taar_ma = QComboBox(self)
        self.combo_taar_ma.addItem("Teevra Madhyam")
        self.combo_taar_ma.addItem("Teevratama Madhyam")
        self.combo_taar_ma.move(320, 80)
        self.combo_taar_ma.setCurrentIndex(self.opt_string[6]-12)
        self.combo_taar_ma.activated[str].connect(self.onActivatedTaarMa)
        # Selection of Komal Dh
        lbl7 = QLabel('Komal Dh:', self)
        lbl7.move(10, 120)
        self.combo_komal_dh = QComboBox(self)
        self.combo_komal_dh.addItem("Ati Komal")
        self.combo_komal_dh.addItem("Komal")
        self.combo_komal_dh.move(80, 115)
        self.combo_komal_dh.setCurrentIndex(self.opt_string[8]-15)
        self.combo_komal_dh.activated[str].connect(self.onActivatedKomalDh)
        # Selection of Shuddh Dh
        lbl8 = QLabel('Shuddh Dh:', self)
        lbl8.move(190, 120)
        self.combo_shuddh_dh = QComboBox(self)
        self.combo_shuddh_dh.addItem("Shuddh")
        self.combo_shuddh_dh.addItem("Teevra")
        self.combo_shuddh_dh.move(270, 115)
        self.combo_shuddh_dh.setCurrentIndex(self.opt_string[9]-17)
        self.combo_shuddh_dh.activated[str].connect(self.onActivatedShuddhDh)
        # Selection of Komal Ni
        lbl9 = QLabel('Komal Ni:', self)
        lbl9.move(10, 155)
        self.combo_komal_ni = QComboBox(self)
        self.combo_komal_ni.addItem("Ati Komal")
        self.combo_komal_ni.addItem("Komal")
        self.combo_komal_ni.move(80, 150)
        self.combo_komal_ni.setCurrentIndex(self.opt_string[10]-19)
        self.combo_komal_ni.activated[str].connect(self.onActivatedKomalNi)
        # Selection of Shuddh Ni
        lbl10 = QLabel('Shuddh Ni:', self)
        lbl10.move(190, 155)
        self.combo_shuddh_ni = QComboBox(self)
        self.combo_shuddh_ni.addItem("Shuddh")
        self.combo_shuddh_ni.addItem("Teevra")
        self.combo_shuddh_ni.move(270, 150)
        self.combo_shuddh_ni.setCurrentIndex(self.opt_string[11]-21)
        self.combo_shuddh_ni.activated[str].connect(self.onActivatedShuddhNi)

        # Set notes and start playing
        button1 = QPushButton('Play!', self)
        button1.setToolTip('Start Playing')
        button1.move(390,115) 
        button1.resize(100,30)
        button1.clicked.connect(self.onActivatedSet)

        # Reset
        button2 = QPushButton('Reset', self)
        button2.setToolTip('Reset The Values')
        button2.move(390,145) 
        button2.resize(100,30)
        button2.clicked.connect(self.onActivatedReset)

        # Back
        button3 = QPushButton('Back', self)
        button3.setToolTip('Go to the previous menu')
        button3.move(390,175) 
        button3.resize(100,30)
        button3.clicked.connect(self.on_click_exit)

    def onActivatedSet(self):
        self.h.dynamicNoteGeneration(env = self.e, opt_str = self.opt_string)
        p = Process(target=self.h.handling, args=())
        p.start()
        buttonReply = QMessageBox.question(self, 'Start Playing!', "Stop Playing?", QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            os.remove("temp.txt")
            os.kill(p.pid, signal.SIGKILL)
        self.show()  

    def onActivatedReset(self):
        
        selection = 1
        self.opt_string[0] = 1
        self.opt_string[1] = 1+selection
        self.opt_string[2] = 3+selection
        self.opt_string[3] = 5+selection
        self.opt_string[4] = 7+selection
        self.opt_string[5] = 9+selection
        self.opt_string[6] = 11+selection
        self.opt_string[7] = 14
        self.opt_string[8] = 14+selection
        self.opt_string[9] = 16+selection
        self.opt_string[10] = 18+selection
        self.opt_string[11] = 20+selection

        self.combo_komal_re.setCurrentIndex(self.opt_string[1]-2)
        self.combo_shuddh_re.setCurrentIndex(self.opt_string[2]-4)
        self.combo_komal_ga.setCurrentIndex(self.opt_string[3]-6)
        self.combo_shuddh_ga.setCurrentIndex(self.opt_string[4]-8)
        self.combo_shuddh_ma.setCurrentIndex(self.opt_string[5]-10)
        self.combo_taar_ma.setCurrentIndex(self.opt_string[6]-12)
        self.combo_komal_dh.setCurrentIndex(self.opt_string[8]-15)
        self.combo_shuddh_dh.setCurrentIndex(self.opt_string[9]-17)
        self.combo_komal_ni.setCurrentIndex(self.opt_string[10]-19)
        self.combo_shuddh_ni.setCurrentIndex(self.opt_string[11]-21)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivatedKomalRe(self, text):
        komalRe = self.combo_komal_re.currentText()
        if komalRe=="Ati Komal":
            self.opt_string[1] = 2
        else:
            self.opt_string[1] = 3

    def onActivatedShuddhRe(self, text):
        shuddhRe = self.combo_shuddh_re.currentText()
        if shuddhRe=="Shuddh":
            self.opt_string[2] = 4
        else:
            self.opt_string[2] = 5

    def onActivatedKomalGa(self, text):
        komalGa = self.combo_komal_ga.currentText()
        if komalGa=="Ati Komal":
            self.opt_string[3] = 6
        else:
            self.opt_string[3] = 7

    def onActivatedShuddhGa(self, text):
        shuddhGa = self.combo_shuddh_ga.currentText()
        if shuddhGa=="Shuddh":
            self.opt_string[4] = 8
        else:
            self.opt_string[4] = 9

    def onActivatedShuddhMa(self, text):
        shuddhMa = self.combo_shuddh_ma.currentText()
        if shuddhMa=="Shuddh Madhyam":
            self.opt_string[5] = 10
        else:
            self.opt_string[5] = 11

    def onActivatedTaarMa(self, text):
        taarMa = self.combo_taar_ma.currentText()
        if taarMa=="Teevra Madhyam":
            self.opt_string[6] = 12
        else:
            self.opt_string[6] = 13

    def onActivatedKomalDh(self, text):
        komalDh = self.combo_komal_dh.currentText()
        if komalDh=="Ati Komal":
            self.opt_string[8] = 15
        else:
            self.opt_string[8] = 16

    def onActivatedShuddhDh(self, text):
        shuddhDh = self.combo_shuddh_dh.currentText()
        if shuddhDh=="Shuddh":
            self.opt_string[9] = 17
        else:
            self.opt_string[9] = 18

    def onActivatedKomalNi(self, text):
        komalNi = self.combo_komal_ni.currentText()
        if komalNi=="Ati Komal":
            self.opt_string[10] = 19
        else:
            self.opt_string[10] = 20

    def onActivatedShuddhNi(self, text):
        shuddhNi = self.combo_shuddh_ni.currentText()
        if shuddhNi=="Shuddh":
            self.opt_string[11] = 21
        else:
            self.opt_string[11] = 22

    def on_click_exit(self):
        ex.opt_string = self.opt_string
        self.close()

class Scale_Selection(QWidget):
    
    def __init__(self, hand):

        super(QWidget, self).__init__()
        self.title = 'Select the Scale'
        self.left = 10
        self.top = 10
        self.width = 210
        self.height = 120
        self.h = hand
        self.initUI()        
        
    def initUI(self):      
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)

        # Scale Selection
        lbl1 = QLabel('Select Scale :', self)
        lbl1.move(10, 15)
        self.scale_select = QComboBox(self)
        self.scale_select.addItem("C (Safed1)")
        self.scale_select.addItem("C# (Kali1)")
        self.scale_select.addItem("D (Safed2)")
        self.scale_select.addItem("D# (Kali2)")
        self.scale_select.addItem("E (Safed3)")
        self.scale_select.addItem("F (Safed4)")
        self.scale_select.addItem("F# (Kali3)")
        self.scale_select.addItem("G (Safed5)")
        self.scale_select.addItem("G# (Kali4)")
        self.scale_select.addItem("A (Safed6)")
        self.scale_select.addItem("A# (Kali5)")
        self.scale_select.addItem("B (Safed7)")
        self.scale_select.move(100, 10)
        self.scale_select.setCurrentIndex(self.h.scale-1)
        self.scale_select.activated[str].connect(self.onScaleSelection)

        # Set notes and start playing
        button_exit = QPushButton('Submit', self)
        button_exit.setToolTip('Submit Selection')
        button_exit.move(60,50) 
        button_exit.resize(100,30)
        button_exit.clicked.connect(self.onActivatedSet)

        # Back
        button_exit = QPushButton('Back', self)
        button_exit.setToolTip('Go to the previous menu')
        button_exit.move(60,80) 
        button_exit.resize(100,30)
        button_exit.clicked.connect(self.on_click_exit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivatedSet(self):

        self.h.frequency_selection()
        self.on_click_exit()

    def onScaleSelection(self, text):

        scaleSelect = self.scale_select.currentText()

        if scaleSelect=="C (Safed1)":
            self.h.scale = 1
        elif scaleSelect=="C# (Kali1)":
            self.h.scale = 2
        elif scaleSelect=="D (Safed2)":
            self.h.scale = 3
        elif scaleSelect=="D# (Kali2)":
            self.h.scale = 4
        elif scaleSelect=="E (Safed3)":
            self.h.scale = 5
        elif scaleSelect=="F (Safed4)":
            self.h.scale = 6
        elif scaleSelect=="F# (Kali3)":
            self.h.scale = 7
        elif scaleSelect=="G (Safed5)":
            self.h.scale = 8
        elif scaleSelect=="G# (Kali4)":
            self.h.scale = 9
        elif scaleSelect=="A (Safed6)":
            self.h.scale = 10
        elif scaleSelect=="A# (Kali5)":
            self.h.scale = 11
        elif scaleSelect=="B (Safed7)":
            self.h.scale = 12

    def on_click_exit(self):
        self.close()

class App(QWidget):
 
    def __init__(self):

        super(QWidget, self).__init__()
        self.title = '22 Shrutis Synthesizer'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 280

        self.tone_filename = os.getcwd()+"/C4_Sa_Harmonium_VST.wav"
        self.e = env.Envelope_Generation_Sampling(filename = self.tone_filename)
        self.h = handle.Handler()
        self.opt_string = {}
        selection  = 1
        self.opt_string[0] = 1
        self.opt_string[1] = 1+selection
        self.opt_string[2] = 3+selection
        self.opt_string[3] = 5+selection
        self.opt_string[4] = 7+selection
        self.opt_string[5] = 9+selection
        self.opt_string[6] = 11+selection
        self.opt_string[7] = 14
        self.opt_string[8] = 14+selection
        self.opt_string[9] = 16+selection
        self.opt_string[10] = 18+selection
        self.opt_string[11] = 20+selection

        self.initUI()
 
    def initUI(self):

        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)

        lbl1 = QLabel('Select the Synthesizer mode', self)
        lbl1.move(152, 25)
 
        button_western = QPushButton('Western Scale', self)
        button_western.setToolTip('Western Scale')
        button_western.move(150,70)
        button_western.resize(200,30)
        button_western.clicked.connect(self.on_click_western)

        button_custom = QPushButton('22 Shrutis Selection', self)
        button_custom.setToolTip('22 Shrutis Selection')
        button_custom.move(150,120) 
        button_custom.resize(200,30)
        button_custom.clicked.connect(self.on_click_custom)    

        button_custom = QPushButton('Select Your Scale', self)
        button_custom.setToolTip('Choose your base scale')
        button_custom.move(150,170) 
        button_custom.resize(200,30)
        button_custom.clicked.connect(self.on_click_select_scale)    
 
        button_exit = QPushButton('Quit', self)
        button_exit.setToolTip('Quit')
        button_exit.move(200,220) 
        button_exit.resize(100,30)
        button_exit.clicked.connect(QApplication.instance().quit)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
 
    @pyqtSlot()
    def on_click_western(self):

        self.h.defaultNoteGeneration(env = self.e)
        p = Process(target=self.h.handling, args=())
        p.start()
        buttonReply = QMessageBox.question(self, 'Start Playing!', "Stop Playing?", QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            os.remove("temp.txt")
            os.kill(p.pid, signal.SIGKILL)
        self.show()  

    @pyqtSlot()
    def on_click_select_scale(self):

        self.ex = Scale_Selection(self.h)
        self.ex.show()

    @pyqtSlot()
    def on_click_custom(self):
        self.ex = CustomizedWindow(self.opt_string, self.h, self.e)
        self.ex.show()

    @pyqtSlot()
    def on_click_exit(self):
    	sys.exit(app.exec_())

if __name__ == "__main__":
    os.system('clear')
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())