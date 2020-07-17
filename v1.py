# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QFileDialog, QTableView
import pyqtgraph as pg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.simButton = QtWidgets.QPushButton(self.centralwidget)
        self.simButton.setGeometry(QtCore.QRect(30, 10, 221, 61))
        self.simButton.setObjectName("simButton")
        self.expButton = QtWidgets.QPushButton(self.centralwidget)
        self.expButton.setGeometry(QtCore.QRect(30, 70, 221, 61))
        self.expButton.setObjectName("expButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(270, 14, 1150, 650))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAT 395 Final Project"))
        self.simButton.setText(_translate("MainWindow", "Choose Simulation Data File"))
        self.expButton.setText(_translate("MainWindow", "Choose Experimental Data File"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.simButton.clicked.connect(self.simButton_handler)
        self.expButton.clicked.connect(self.expButton_handler)

    
    def simButton_handler(self):
        print("Sim Button Pressed")
        self.open_dialog_box_sim()
        
    
    def expButton_handler(self):
        print("Exp Button Pressed")
        self.open_dialog_box_exp()
        
        
    def open_dialog_box_sim(self):
        filename_sim = QFileDialog.getOpenFileName()
        path_sim = filename_sim[0]
        def GenSplineData(x, y): # Plots the stuff
            plt.scatter(x, y, label = "Simulation Data") # plot the raw data
            xp = np.linspace(400, 2800, 1201)
            spl = UnivariateSpline(x, y) # fit the data to a spline
            sply = spl(xp)
            db_entry = { # puts the x's and y's together in one matrix
                        "Energy (eV)": xp,
                        "Intensity (a.u)": sply
                        }
            df_spline = pd.DataFrame(db_entry) # out the values in a pandas dataframe
            df_spline.to_csv('/Users/raivat/Desktop/Spline_Fit_Values.csv', index=False) # save a CSV file
        
        s = pd.read_excel(path_sim)
        # reads the .csv file can be found in dropbox > shared manuscripts >
        # Ravi Ben MoOx Nucleation and LEIS > Figures
        GenSplineData(s.energy, s.Simulation) # run the function
    
    def open_dialog_box_exp(self):
        filename_exp = QFileDialog.getOpenFileName()
        path_exp = filename_exp[0]


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        self.show()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

