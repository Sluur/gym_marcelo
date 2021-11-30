from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys
import data_repositories_clsSociosrepository

import c_loadnewMembership
import c_loadNewMember


class clsSearchDni(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsSearchDni, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Dnisearch.ui',self)

        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        self.setupUiComponents()
    
    
    def setupUiComponents(self):
        self.btnContinue.clicked.connect(self.validateDni)
    
    def validateDni(self):
        dniSearch = self.txtDni.text()
        aux = self.objUser.getDNI(dniSearch)
        print (aux)
        if aux != None:
            self.w = c_loadnewMembership.clsNewMembership(aux[0])
            self.w.show()
            self.close()
        else:
            self.w = c_loadNewMember.clsNewMember()
            self.w.show()
            self.close()
            
        
        
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