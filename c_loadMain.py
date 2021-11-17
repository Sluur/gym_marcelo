from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember
import c_loadnewMembership

import data_repositories_clsUserrepository

class clsMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsMain, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/main.ui',self)
        
        self.objUser = data_repositories_clsUserrepository.clsUserRepository()
        
        
        self.setupUiComponents()

    def setupUiComponents(self):
            self.btnNewS.clicked.connect(self.insertMember)
            self.btnNewM.clicked.connect(self.insertMembresia)

    def insertMember(self):
        self.w = c_loadNewMember.clsNewMember()
        self.w.show()
        result = self.objUser.getAll()
        print(result)
    def insertMembresia(self):
        self.w = c_loadnewMembership.clsNewMembership()
        self.w.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    mainW = clsMain()
    mainW.show()
    app.exec_()


main() 