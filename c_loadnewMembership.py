from PyQt5 import QtCore, QtWidgets, uic
import data_repositories_clsSociosrepository,data_repositories_clsMembresias,data_repositories_clsTarifas
import c_continarPago
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import traceback
import sys
from datetime import datetime
from datetime import timedelta

#https://stackoverflow.com/questions/59960494/pyqt5-recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-o
# como salvar recursion x ventanas que se llaman


class clsNewMembership(QtWidgets.QMainWindow):
    def __init__(self, aux):
        super(clsNewMembership, self).__init__()
        uic.loadUi('C:/Users/nalej/Downloads/gym_marcelo-main (1)/gym_marcelo-main/Pantallas qt/Nuevamembresia.ui',self)
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        self.objMembresia = data_repositories_clsMembresias.clsMembresiasRepository()
        self.objTarifa = data_repositories_clsTarifas.clsMembresiasRepository()
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
        self.dias = 30;
        self.pago = self.tarifa

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
        print (tipo)
        print(tiempo)
        if tipo == 1:
            self.pago = (self.pago)/10;
        elif tipo == 5:
            print("hola")
            if tiempo == 1:
                self.pago = self.pago
            elif tiempo == 2:
                self.pago = self.pago*2
                self.dias = self.dias*2
            elif tiempo == 3:
                self.pago = self.pago*3
                self.dias = self.dias*3
            elif tiempo == 6:
                self.pago = self.pago*6   
                self.dias = self.dias*6
        elif tipo == 3:
            print("hola")
            self.pago == ((self.pago)*75)/100
            if tiempo == 1:
                self.pago = self.pago
            elif tiempo == 2:
                self.pago = self.pago*2
            elif tiempo == 3:
                self.pago = self.pago*3
            elif tiempo == 6:
                self.pago = self.pago*6
        print(self.pago)

        fechaAlta = self.dateEdit.date()
        fechaBaja = fechaAlta.addDays(self.dias)

        print(fechaAlta.toPyDate().strftime("%Y-%m-%d"))
        print(fechaBaja.toPyDate().strftime("%Y-%m-%d"))
        print(self.aux[0])
        
        self.objMembresia.add(str(fechaAlta.toPyDate().strftime("%Y-%m-%d")),str(fechaBaja.toPyDate().strftime("%Y-%m-%d")),int(self.aux[0]))

        self.close()
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newM = clsNewMembership(None)
    newM.show()
    app.exec_()

if __name__ == '__main__':
    main() 