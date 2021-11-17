from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import loadNewMember
import loadnewMembership



class clsMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsMain, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/main.ui',self)
        
        self.objUser = clsUserRepository.getAll
        print (str(self.objUser))

        self.setupUiComponents()

    def setupUiComponents(self):
            self.btnNewS.clicked.connect(self.insertMember)
            self.btnNewM.clicked.connect(self.insertMembresia)

    def insertMember(self):
        self.w = loadNewMember.clsNewMember()
        self.w.show()
    def insertMembresia(self):
        self.w = loadnewMembership.clsNewMembership()
        self.w.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    mainW = clsMain()
    mainW.show()
    app.exec_()


main() 