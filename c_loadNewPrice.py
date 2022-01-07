from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

import traceback
import sys
import data_repositories_clsTarifas, c_loadMain

import c_loadnewMembership
import c_loadNewMember


class clsLoadNewPrice(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsLoadNewPrice, self).__init__()
        uic.loadUi('C:/Users/nalej/Downloads/gym_marcelo-main (1)/gym_marcelo-main/Pantallas qt/NuevaTarifa.ui',self)

        self.objTarifa = data_repositories_clsTarifas.clsMembresiasRepository()
        self.setupUiComponents()
    
    
    def setupUiComponents(self):
        self.btnGuardar.clicked.connect(self.cambiarTarifa)
        self.btnCancelar.clicked.connect(self.close)

    def cambiarTarifa(self):
        nuevoPrecio = int(self.lineEdit.text())
        FechaAlta = QDate.currentDate().toPyDate()
        FechaBaja = QDate.currentDate().toPyDate()
        Id = str((self.objTarifa.getActive())[0][0])
        
        
        self.objTarifa.update(FechaBaja, Id)
        
        self.objTarifa.insert(nuevoPrecio, FechaAlta)
        
        self.close()
        self.w= c_loadMain.clsMenu()
        self.w.show()

    
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    dnis = clsLoadNewPrice()
    dnis.show()
    app.exec_()

if __name__ == '__main__':
    main() 