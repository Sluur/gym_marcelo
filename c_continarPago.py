from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem



import traceback

import sys


import c_loadNewMember
import c_loadMain
import c_clsSearchDni

import data_repositories_clsMembresias,data_repositories_clsSociosrepository

class clsPago(QtWidgets.QMainWindow):
    def __init__(self, aux, pago, dias):
        super(clsPago, self).__init__()
        uic.loadUi('C:/Users/nalej/Downloads/gym_marcelo-main (1)/gym_marcelo-main/Pantallas qt/Continuarmembresia.ui',self)


        self.dias = dias
        self.pago = pago 
        self.aux = aux
        
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btnContinuar.clicked.connect(self.addMembresia)
        self.btnCancelar.clicked.connect(self.close)
        self.txtPago.setText("$" + str(self.pago))   

    def addMembresia(self):
        self.objMembresia
        
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    login = clsPago(None,None,None)
    login.show()
    app.exec_()

if __name__ == '__main__':
    main() 