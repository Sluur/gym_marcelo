from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember
import c_loadMain
import c_clsSearchDni

import data_repositories_clsUserrepository

class clsLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsLogin, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/login.ui',self)
        
        self.objUser = data_repositories_clsUserrepository.clsUserRepository()
        print("A")
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnIngresar.clicked.connect(self.validate)
        
    def validate(self):        
        print(self.txtUser.text())
        print(self.txtPass.text())
        IsValid = self.objUser.validate(str(self.txtUser.text()), str(self.txtPass.text()))
        print(IsValid)
        if IsValid:
            print("bienvenido4")
            self.w = c_loadMain.clsMenu()
            self.w.show()
            self.close()
        else:
            print("q te pasa!")
            
       


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    login = clsLogin()
    login.show()
    app.exec_()

if __name__ == '__main__':
    main() 