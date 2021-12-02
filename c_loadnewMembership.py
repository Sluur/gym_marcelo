from PyQt5 import QtCore, QtWidgets, uic
import data_repositories_clsSociosrepository,data_repositories_clsTarifas
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import traceback
import sys


#https://stackoverflow.com/questions/59960494/pyqt5-recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-o
# como salvar recursion x ventanas que se llaman


class clsNewMembership(QtWidgets.QMainWindow):
    def __init__(self, aux):
        super(clsNewMembership, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Nuevamembresia.ui',self)
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        self.objTarifa  = data_repositories_clsTarifas.clsMembresiasRepository()
        self.aux = aux
        self.setupUiComponents()
        
        
    def setupUiComponents(self):
        
        self.txtApellido.setText(self.aux[1])
        self.txtNombre.setText(self.aux[2])
        self.txtDni.setText(str(self.aux[3]))
        
        now = QDate.currentDate()
        self.dateEdit.setDate(now)
        self.data = self.getComboList()
        self.data2 = self.getComboType()
        self.comboBox.addItems(self.data2)
        self.comboBox_2.addItems(self.data)
        
        self.btnGuardar.clicked.connect(self.calcularPago)
        
        self.comboBox.currentIndexChanged.connect(self.on_change)
        
        self.tarifa = int((self.objTarifa.getActive())[0][1])
        print (self.tarifa)

    def on_change(self, newIndex):
        if newIndex==2:
            self.comboBox_2.setEnabled(False)
        else:
            self.comboBox_2.setEnabled(True)
    def getComboList(self):     

        comboList=[]
        
        comboList.append("1 Mes")
        comboList.append("2 Meses")   
        comboList.append("3 Meses")
        comboList.append("6 Meses")     
        return comboList
    def getComboType(self):
        comboList=[]
        
        comboList.append("3 dias/Semana")
        comboList.append("5 dias/Semana")
        comboList.append("1 dia")
        return comboList

    def getidDataType(self,elem):

        if (elem!=''):
            return elem
    
    def calcularPago(self):
        tipo = int((self.comboBox.currentText())[0])
        tiempo = int((self.comboBox_2.currentText())[0])
        print(tipo)
        print(tiempo)


        
    
    
    def insterMembership(self):
        self.objUser 
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newM = clsNewMembership(None)
    newM.show()
    app.exec_()

if __name__ == '__main__':
    main() 