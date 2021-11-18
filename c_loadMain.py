from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember

import c_clsSearchDni

import data_repositories_clsUserrepository

class clsMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsMain, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/main.ui',self)
        
        self.objUser = data_repositories_clsUserrepository.clsUserRepository()
        print("A")
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnNewS.clicked.connect(self.insertMember)
        self.btnNewM.clicked.connect(self.searchDni)

    
    
    def searchDni(self):
        self.w = c_clsSearchDni.clsSearchDni()
        self.w.show()
        
    def insertMember(self):
        self.w = c_loadNewMember.clsNewMember()
        self.w.show()
        result = self.objUser.getAll()
        print(result)


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    mainW = clsMain()
    mainW.show()
    app.exec_()


main() 