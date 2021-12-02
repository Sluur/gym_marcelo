from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember

import c_clsSearchDni, c_loadSocios, c_loadNewPrice,c_loadMain
import data_repositories_clsUserrepository,data_repositories_clsTarifas


class clsMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsMenu, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/main.ui',self)
        
        self.objUser = data_repositories_clsUserrepository.clsUserRepository()
        self.objTarifa  = data_repositories_clsTarifas.clsMembresiasRepository()
        print("A")
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.cuota = str((self.objTarifa.getActive())[0][1])
        self.btnNew.clicked.connect(self.searchDni)
        self.btnSocios.clicked.connect(self.Socios)
        self.btnTarifa.clicked.connect(self.nuevaTarifa)
        self.txtCuota.setText("Cuota: $"+self.cuota)
        
    def Socios(self):
        self.w = c_loadSocios.clsloadSocios()
        self.w.show()
    
    
    def searchDni(self):
        self.w = c_clsSearchDni.clsSearchDni()
        self.w.show()
    
    def nuevaTarifa(self):
        self.w = c_loadNewPrice.clsLoadNewPrice()
        self.w.show()
        self.close()

        
        
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    mainW = clsMenu()
    mainW.show()
    app.exec_()


if __name__ == '__main__':
    main() 