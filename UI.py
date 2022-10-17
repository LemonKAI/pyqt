# -*- coding: utf-8 -*-
import random
import time
from copy import copy

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow

from data import Data
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 910)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 1012, 707))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(100, 60))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.horizontalLayout_7.addWidget(self.label_9)
        self.plr_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.plr_bar.setStyleSheet("")
        self.plr_bar.setProperty("value", 24)
        self.plr_bar.setInvertedAppearance(False)
        self.plr_bar.setObjectName("plr_bar")
        self.horizontalLayout_7.addWidget(self.plr_bar)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(100, 60))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.horizontalLayout_5.addWidget(self.label_13)
        self.acc_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.acc_bar.setProperty("value", 24)
        self.acc_bar.setObjectName("acc_bar")
        self.horizontalLayout_5.addWidget(self.acc_bar)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(100, 60))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.horizontalLayout_6.addWidget(self.label_14)
        self.latency_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.latency_bar.setMaximum(30000)
        self.latency_bar.setProperty("value", 450)
        self.latency_bar.setTextVisible(True)
        self.latency_bar.setObjectName("latency_bar")
        self.horizontalLayout_6.addWidget(self.latency_bar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(100, 60))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.horizontalLayout_8.addWidget(self.label_15)
        self.network_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.network_bar.setProperty("value", 24)
        self.network_bar.setObjectName("network_bar")
        self.horizontalLayout_8.addWidget(self.network_bar)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(100, 60))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.horizontalLayout_9.addWidget(self.label_10)
        self.cpu_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.cpu_bar.setProperty("value", 24)
        self.cpu_bar.setObjectName("cpu_bar")
        self.horizontalLayout_9.addWidget(self.cpu_bar)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_21.setMinimumSize(QtCore.QSize(100, 60))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.horizontalLayout_10.addWidget(self.label_21)
        self.memory_bar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.memory_bar.setMinimumSize(QtCore.QSize(250, 0))
        self.memory_bar.setProperty("value", 24)
        self.memory_bar.setObjectName("memory_bar")
        self.horizontalLayout_10.addWidget(self.memory_bar)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, 50, 30, 50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Idex = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Idex.setFont(font)
        self.Idex.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Idex.setObjectName("Idex")
        self.horizontalLayout_2.addWidget(self.Idex)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(20, 50, 20, 50)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.level = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.level.setText("")
        self.level.setPixmap(QtGui.QPixmap("images/level1.JPG"))
        self.level.setObjectName("level")
        self.verticalLayout_7.addWidget(self.level)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.slider = QtWidgets.QSlider(self.centralwidget)
        # self.slider.setGeometry(QtCore.QRect(310, 800, 160, 16))
        # self.slider.setMaximum(2)
        # self.slider.setOrientation(QtCore.Qt.Horizontal)
        # self.slider.setObjectName("slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.slider.valueChanged.connect(self.valueChange)

        self.thread = WorkThread()
        self.thread.start()
        self.thread.valueUpdated.connect(self.updateProcessBar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Performance:"))
        self.label_9.setText(_translate("MainWindow", "PLR:"))
        self.label_13.setText(_translate("MainWindow", "Data Acc:"))
        self.label_14.setText(_translate("MainWindow", "Latency:"))
        self.label.setText(_translate("MainWindow", "Resource:"))
        self.label_15.setText(_translate("MainWindow", "Network:"))
        self.label_10.setText(_translate("MainWindow", "CPU:"))
        self.label_21.setText(_translate("MainWindow", "Memory:"))
        self.label_3.setText(_translate("MainWindow", "IDEX:"))
        self.Idex.setText(_translate("MainWindow", "-.-"))

    def valueChange(self):
        idx = self.slider.value()
        print("slider value change to " + str(idx))
        global data
        data = data_list[idx]

    def updateProcessBar(self, data):
        self.plr_bar.setValue(data.plr)
        self.acc_bar.setValue(data.acc)
        self.latency_bar.setValue(data.latency)
        if(data.latency > 1000):
            self.latency_bar.setFormat(str(round((data.latency/1000), 2)) + "s")
        else:
            self.latency_bar.setFormat(str(int(data.latency)) + "ms")
        self.network_bar.setValue(data.network)
        self.cpu_bar.setValue(data.cpu)
        self.memory_bar.setValue(data.memory)
        self.updateLevel(data)

    def updateLevel(self, data):
        plr_idex = ((100-data.plr)/20)
        acc_idex = data.acc/20
        lat_idex = ((30000-data.latency)/30000 * 100)/20
        net_idex = (100-data.network)/20
        cpu_idex = (100-data.cpu)/20
        mem_idex = (100-data.memory)/20
        # print(plr_idex,  acc_idex , lat_idex, net_idex, cpu_idex, mem_idex)
        idex = round(float((plr_idex + acc_idex + lat_idex + net_idex + cpu_idex + mem_idex)/6), 2)
        self.Idex.setText(str(idex))
        if(idex > 0 and idex <= 1.5):
            self.level.setPixmap(QtGui.QPixmap("images/level1.JPG"))
        elif(idex > 1.5 and idex <= 2.5):
            self.level.setPixmap(QtGui.QPixmap("images/level2.JPG"))
        elif (idex > 2.5 and idex <= 3.5):
            self.level.setPixmap(QtGui.QPixmap("images/level3.JPG"))
        elif (idex > 3.5 and idex <= 4.5):
            self.level.setPixmap(QtGui.QPixmap("images/level4.JPG"))
        elif (idex > 4.5 and idex <= 5):
            self.level.setPixmap(QtGui.QPixmap("images/level5.JPG"))
        else:
            self.level.setPixmap(QtGui.QPixmap("images/level1.JPG"))
class WorkThread(QThread):
    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
    valueUpdated = pyqtSignal(Data)
    def run(self) :
        global data
        while(True):
            gen_data = copy(data)
            gen_data.plr += random.uniform(-2, 2)
            gen_data.acc += random.uniform(-2, 2)
            gen_data.latency += (random.uniform(-2, 2)*50)
            gen_data.network += random.uniform(-2, 2)
            gen_data.cpu += random.uniform(-2, 2)
            gen_data.memory += random.uniform(-2, 2)
            self.valueUpdated.emit(gen_data)
            time.sleep(1)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent=parent)
    def keyPressEvent(self, keyEvent):

        print("key listen: " + keyEvent.text())
        global data
        if(keyEvent.key() == Qt.Key_1):
            data = data_list[0]
        elif (keyEvent.key() == Qt.Key_2):
            data = data_list[1]
        elif (keyEvent.key() == Qt.Key_3):
            data = data_list[2]
if __name__ == "__main__":
    import sys

    normal = Data(1, 99, 400, 34, 5, 52)
    ddos = Data(83, 41, 14000, 78, 76, 53)
    firewall = Data(2, 99, 500, 37, 5, 53)
    data_list = [normal, ddos, firewall]
    data = data_list[0]

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    work_thread = WorkThread()
    work_thread.start()
    MainWindow.show()
    sys.exit(app.exec_())

