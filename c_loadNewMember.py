from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys

import data_repositories_clsSociosrepository


class clsNewMember(QtWidgets.QMainWindow):
    def __init__(self,aux):
        super(clsNewMember, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Nuevosocio.ui',self)
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        self.aux = aux
        self.setupUiComponents()
        
    def setupUiComponents(self):
        if self.aux != None:
            self.txtTopSocio.setText("EDITAR SOCIO")
            self.txtApellido.setText(self.aux[1])
            self.txtNombre.setText(self.aux[2])
            self.txtDni.setText(str(self.aux[3]))
            self.txtTelefono.setText(str(self.aux[4]))
            self.pushButton.clicked.connect(self.updateMember)
            self.label.setText(str(self.aux[0]))
            
 
        else:
            self.txtTopSocio.setText("NUEVO SOCIO")    
            self.pushButton.clicked.connect(self.insertMember)
           
            
        self.data = self.getComboList()
        self.comboBox.addItems(self.data)
        self.btnCancelar.clicked.connect(self.close)
        

    def getComboList(self):     

        comboList=[]
        
        comboList.append("Masculino")
        comboList.append("Femenino")        
        return comboList


    def getidDataType(self,elem):

        if (elem!=''):
            return elem[0] 
        
    def insertMember(self):
        
        revdate = self.dateEdit.date().toPyDate().strftime("%Y-%m-%d")
        self.objUser.insert(str(self.txtApellido.text()),str(self.txtNombre.text()),int(self.txtDni.text()),int(self.txtTelefono.text()),revdate,str(self.getidDataType(self.comboBox.currentText())),str(self.txtObs.text()),0,1)
        self.close() 
    def updateMember(self):
        revdate = self.dateEdit.date().toPyDate().strftime("%Y-%m-%d")
        self.objUser.update(str(self.txtApellido.text()),str(self.txtNombre.text()),int(self.txtDni.text()),int(self.txtTelefono.text()),revdate,str(self.getidDataType(self.comboBox.currentText())),str(self.txtObs.text()),0,1,int(self.label.text()))
        self.close() 
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newMs = clsNewMember(None)
    newMs.show()
    app.exec_()

if __name__ == '__main__':
    main() 