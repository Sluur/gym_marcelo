from PyQt5 import QtCore, QtWidgets, uic
import data_repositories_clsSociosrepository

import traceback
import sys


#https://stackoverflow.com/questions/59960494/pyqt5-recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-o
# como salvar recursion x ventanas que se llaman


class clsNewMembership(QtWidgets.QMainWindow):
    def __init__(self, aux):
        super(clsNewMembership, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Nuevamembresia.ui',self)
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        self.aux = aux
        self.setupUiComponents()
        
    def setupUiComponents(self):
        
        self.txtApellido.setText(self.aux[1])
        self.txtNombre.setText(self.aux[2])
        self.txtDni.setText(str(self.aux[3]))
        
    def getComboList(self):     

        comboList=[]
        
        comboList.append("Masculino")
        comboList.append("Femenino")        
        return comboList


    def getidDataType(self,elem):

        if (elem!=''):
            return elem[0]
    def insterMembership(self):
        self.objUser 
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newM = clsNewMembership(None)
    newM.show()
    app.exec_()

if __name__ == '__main__':
    main() 