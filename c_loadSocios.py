from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember
import c_loadMain
import c_clsSearchDni

import data_repositories_clsSociosrepository

class clsloadSocios(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsloadSocios, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Socios.ui',self)
        
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        print("A")
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.traerSocios()
        self.btnTraer.clicked.connect(self.traerSocios)
        
    def traerSocios(self):
        # try:            
            result = self.objUser.getFiltered(str(self.txtBusqueda.text()))
            
            self.tblData.setRowCount(0)
            self.tblData.setColumnCount(9)
            self.tblData.setHorizontalHeaderLabels(["ID", "Apellido", "Nombre", "Dni", "Telefono", "Fecha N", "Sexo", "Observaciones", "Rutina"])
            
            for elem in result:
                rows = self.tblData.rowCount()

                self.tblData.setRowCount(rows + 1)
                self.tblData.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
                self.tblData.setItem(rows, 1, QTableWidgetItem(str(elem[1])))
                self.tblData.setItem(rows, 2, QTableWidgetItem(str(elem[2])))
                self.tblData.setItem(rows, 3, QTableWidgetItem(str(elem[3])))
                self.tblData.setItem(rows, 4, QTableWidgetItem(str(elem[4])))                 
                self.tblData.setItem(rows, 5, QTableWidgetItem(str(elem[5])))
                self.tblData.setItem(rows, 6, QTableWidgetItem(str(elem[6])))
                self.tblData.setItem(rows, 7, QTableWidgetItem(str(elem[7])))  
                self.tblData.setItem(rows, 8, QTableWidgetItem(str(elem[8])))  
            self.tblData.resizeColumnsToContents()

        # except:
        #     print('Error al cargar datos en grilla')
            
       


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    socios = clsloadSocios()
    socios.show()
    app.exec_()

if __name__ == '__main__':
    main() 