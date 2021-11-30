from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember

import c_clsSearchDni

import data_repositories_clsUserrepository

class clsMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsMenu, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/main.ui',self)
        
        self.objUser = data_repositories_clsUserrepository.clsUserRepository()
        print("A")
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnNew.clicked.connect(self.searchDni)

    
    
    def searchDni(self):
        self.w = c_clsSearchDni.clsSearchDni()
        self.w.show()
        
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    mainW = clsMenu()
    mainW.show()
    app.exec_()


if __name__ == '__main__':
    main() 