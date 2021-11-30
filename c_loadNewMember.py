from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys

import data_repositories_clsSociosrepository


class clsNewMember(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsNewMember, self).__init__()
        uic.loadUi('C:/Users/rodri/Documents/gym_marcelo/Pantallas qt/Nuevosocio.ui',self)
        self.objUser = data_repositories_clsSociosrepository.clsSocioRepository()
        
        self.setupUiComponents()
        
    def setupUiComponents(self):
        self.pushButton.clicked.connect(self.insertMember)
        self.data = self.getComboList()
        self.comboBox.addItems(self.data)
        
        
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
        self.objUser.insert(str(self.lineEdit.text()),str(self.lineEdit_2.text()),int(self.lineEdit_3.text()),int(self.lineEdit_4.text()),revdate,str(self.getidDataType(self.comboBox.currentText())),str(self.lineEdit_5.text()),0,1)

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newMs = clsNewMember()
    newMs.show()
    app.exec_()

if __name__ == '__main__':
    main() 