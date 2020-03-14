 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Transport.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication
import numpy as np
from pyqtgraph import PlotWidget,mkPen,setConfigOptions



class Ui_Dialog(object):
    def __init__(self) :
        self.c = 1
        self.dx = 0.1
        self.n = 1
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Equation de transport")
        Dialog.resize(996, 388)
        Dialog.setWindowIcon(QtGui.QIcon(r'D:\Cours\Aero2\GP\Transport\Numerix.jpg'))
        Dialog.setFixedSize(996,388)
        font = QtGui.QFont()
        font.setFamily("CMU Bright")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 361, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 161, 16))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setMouseTracking(False)
        self.label_2.setObjectName("label_2")
        self.L = QtWidgets.QLineEdit(self.frame)
        self.L.setGeometry(QtCore.QRect(10, 40, 113, 22))
        self.L.setObjectName("L")
        self.tmax = QtWidgets.QLineEdit(self.frame)
        self.tmax.setGeometry(QtCore.QRect(200, 40, 113, 22))
        self.tmax.setObjectName("tmax")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 110, 361, 221))
        font = QtGui.QFont()
        font.setFamily("CMU Serif")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_3.setObjectName("label_3")
        self.CI = QtWidgets.QComboBox(self.frame_2)
        self.CI.setGeometry(QtCore.QRect(10, 50, 91, 22))
        font = QtGui.QFont()
        font.setFamily("CMU Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CI.setFont(font)
        self.CI.setStyleSheet("")
        self.CI.setObjectName("CI")
        self.CI.addItem("sin(x)")
        self.CI.addItem("exp(-x^2)")
        self.CI.addItem("0")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 201, 16))
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(170, 0, 191, 181))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_5.setObjectName("label_5")
        self.Cl_0 = QtWidgets.QComboBox(self.frame_3)
        self.Cl_0.setGeometry(QtCore.QRect(20, 70, 90, 22))
        self.Cl_0.setObjectName("Cl_0")
        self.Cl_0.addItem("0")
        self.Cl_0.addItem("sin(t)")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label_6.setObjectName("label_6")
        self.Cl_L = QtWidgets.QComboBox(self.frame_3)
        self.Cl_L.setGeometry(QtCore.QRect(20, 140, 90, 22))
        self.Cl_L.setObjectName("Cl_L")
        self.Cl_L.addItem("0")
        self.Cl_L.addItem("sin(t)")
        self.Cl_L.addItem("Aucune")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_7.setObjectName("label_7")
        self.Vitesse = QtWidgets.QLineEdit(self.frame_2)
        self.Vitesse.setGeometry(QtCore.QRect(10, 140, 113, 22))
        self.Vitesse.setObjectName("Vitesse")
        self.Animation = QtWidgets.QCheckBox(Dialog)
        self.Animation.setGeometry(QtCore.QRect(30, 340, 101, 20))
        self.Animation.setObjectName("Animation")
        self.Plot_btn = QtWidgets.QPushButton(Dialog)
        self.Plot_btn.setGeometry(QtCore.QRect(220, 340, 93, 28))
        self.Plot_btn.setObjectName("Plot_btn")
        self.Graph = PlotWidget(Dialog)
        self.Graph.setGeometry(QtCore.QRect(389, 9, 591, 361))
        self.Graph.setObjectName("Graph")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.CI, self.Vitesse)
        Dialog.setTabOrder(self.Vitesse,self.Cl_0)
        Dialog.setTabOrder(self.Cl_0, self.Cl_L)
        Dialog.setTabOrder(self.Cl_L, self.Animation)
        Dialog.setTabOrder(self.Animation, self.Plot_btn)
        
        setConfigOptions(antialias=True)
        
        self.Plot_btn.clicked.connect(self.plotter)
        self.Graph.setBackground('w')
        self.Graph.setLabel('left','y(x,tmax)')
        self.Graph.setLabel('bottom','x')
        
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animplotter)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Equation de transport"))
        self.label.setText(_translate("Dialog", "Longueur de l\'espace :"))
        self.label_2.setText(_translate("Dialog", "Temps maximum :"))
        self.label_3.setText(_translate("Dialog", "Conditions initiales :"))
        self.CI.setItemText(0, _translate("Dialog", "sin(x)"))
        self.CI.setItemText(1, _translate("Dialog", "exp(-x^2)"))
        self.CI.setItemText(2, _translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "Conditions aux limites :"))
        self.label_5.setText(_translate("Dialog", "En x = 0 :"))
        self.Cl_0.setItemText(0, _translate("Dialog", "0"))
        self.Cl_0.setItemText(1, _translate("Dialog", "sin(t)"))
        self.label_6.setText(_translate("Dialog", "En x = L :"))
        self.Cl_L.setItemText(0, _translate("Dialog", "0"))
        self.Cl_L.setItemText(1, _translate("Dialog", "sin(t)"))
        self.Animation.setText(_translate("Dialog", "Animation"))
        self.Plot_btn.setText(_translate("Dialog", "Plot !"))
        self.label_6.setText(_translate("Dialog", "En x = L :"))
        self.Cl_L.setItemText(0, _translate("Dialog", "0"))
        self.Cl_L.setItemText(1, _translate("Dialog", "sin(t)"))
        self.Cl_L.setItemText(2, _translate("Dialog", "Aucune"))
        self.Animation.setText(_translate("Dialog", "Animation"))
        self.Plot_btn.setText(_translate("Dialog", "Plot !"))
        self.label_7.setText(_translate("Dialog", "Vitesse de l\'onde :"))
    
    def solve(self) :
        
        self.C = self.c*self.dt/self.dx
        self.Fi = init = self.Finit()
        self.sol = []
        self.solutions = [0 for t in self.T]
        
        for t in range(len(self.T)) :
            for x in range(len(self.Fi)) :
                self.sol.append(
                    init[x] - self.C*(init[x] - init[x-1])
                    )
            
            if self.Cl_0.currentText() == 'sin(t)' :
                self.sol[0] = np.sin(self.T[t]*self.c)
            elif self.Cl_0.currentText() == '0' :
                self.sol[0] = 0
            
            if self.Cl_L.currentText() == 'sin(t)' :
                self.sol[-1] = np.sin(self.T[t])
            elif self.Cl_L.currentText() == '0' :
                self.sol[-1] = 0
            
            init = self.sol
            self.sol = []
            self.solutions[t] = init
            
        self.sol = init
        return self.sol
    
    def plotter(self) :
        
        self.c = float(self.Vitesse.text())
        self.tmaxv = float(self.tmax.text())
        self.dt = self.dx/self.c
        
        self.Graph.clear()
        
        self.X = np.arange(0,float(self.L.text()),self.dx).tolist()
        self.T = np.arange(0,self.tmaxv,self.dt).tolist()
        
        Solution = self.solve()
        self.Graph.setXRange(0,float(self.L.text()))
        self.Graph.setYRange(min(Solution)-self.dx,1.1)
        
        self.timer.setInterval(self.tmaxv/len(self.T)*10**3)
        #self.timer.setInterval(50)
        
        if self.Animation.isChecked() :
            self.n = 1
            self.my_line = self.Graph.plot(self.X,self.Finit(),name ='t=0', pen = mkPen(color = 'k') )
            self.timer.start()
        else :
            self.Graph.plot(self.X,self.Finit(),name ='t=0', pen = mkPen(color = 'b') )
            self.Graph.plot(self.X,Solution,name ='t=tmax', pen = mkPen(color = 'k') )
        
    def Finit(self) :
        X = np.arange(0,float(self.L.text()),self.dx)
        if self.CI.currentText() == 'exp(-x^2)' :
            return np.exp(-(X-float(self.L.text())/2)**2)
        elif self.CI.currentText() == 'sin(x)' :
            return np.sin(X)
        elif self.CI.currentText() == '0' :
            return [0 for x in X]
    
    def animplotter(self) :
        try :
            self.my_line.setData(self.X,self.solutions[self.n])
            self.n += 1
        except :
            self.timer.stop()



class AppWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())