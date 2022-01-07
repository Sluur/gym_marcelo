from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys

import c_loadSocios
import c_loadNewMember
import c_loadMain
import c_clsSearchDni

import data_repositories_clsMembresias

class clsLoadMembresias(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsLoadMembresias, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Membresias.ui',self)
        
        self.objMembresia = data_repositories_clsMembresias.clsMembresiasRepository()
        
        self.row=-1
        self.column=-1

        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.traerMembresias()
        self.btnTraer.clicked.connect(self.traerMembresiasFiltered)


    @QtCore.pyqtSlot(QtCore.QModelIndex)  
    def cargarForm(self, index):
        aux = self.objUser.getAll()
        column = index.column()
        row = index.row()
        self.w = c_loadNewMember.clsNewMember(aux[row])
        self.w.show()
    def traerMembresiasFiltered(self):
            result = self.objMembresia.getFiltered(str(self.txtBusqueda.text()))
            self.tblData.setRowCount(0)
            self.tblData.setColumnCount(5)
            self.tblData.setHorizontalHeaderLabels(["FechaAlta", "FechaBaja", "Apellido", "Nombre", "DNI"])
            
            for elem in result:
                rows = self.tblData.rowCount()

                self.tblData.setRowCount(rows + 1)
                self.tblData.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
                self.tblData.setItem(rows, 1, QTableWidgetItem(str(elem[1])))
                self.tblData.setItem(rows, 2, QTableWidgetItem(str(elem[2])))
                self.tblData.setItem(rows, 3, QTableWidgetItem(str(elem[3])))
                self.tblData.setItem(rows, 4, QTableWidgetItem(str(elem[4])))
            self.tblData.resizeColumnsToContents()

    def traerMembresias(self):

            result = self.objMembresia.getAll()
            
            self.tblData.setRowCount(0)
            self.tblData.setColumnCount(5)
            self.tblData.setHorizontalHeaderLabels(["FechaAlta", "FechaBaja", "Apellido", "Nombre", "DNI"])
            
            for elem in result:
                rows = self.tblData.rowCount()

                self.tblData.setRowCount(rows + 1)
                self.tblData.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
                self.tblData.setItem(rows, 1, QTableWidgetItem(str(elem[1])))
                self.tblData.setItem(rows, 2, QTableWidgetItem(str(elem[2])))
                self.tblData.setItem(rows, 3, QTableWidgetItem(str(elem[3])))
                self.tblData.setItem(rows, 4, QTableWidgetItem(str(elem[4])))
            self.tblData.resizeColumnsToContents()

            
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    socios = clsLoadMembresias()
    socios.show()
    app.exec_()

if __name__ == '__main__':
    main() 