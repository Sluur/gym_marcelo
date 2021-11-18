from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys

import c_loadnewMembership



class clsSearchDni(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsSearchDni, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/Dnisearch.ui',self)

        self.setupUiComponents()
    
    
    def setupUiComponents(self):
        self.btnContinue.clicked.connect(self.insertMembresia)
        
    def insertMembresia(self):
        self.w = c_loadnewMembership.clsNewMembership()
        self.w.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    dnis = clsSearchDni()
    dnis.show()
    app.exec_()

if __name__ == '__main__':
    main() 