from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys


#https://stackoverflow.com/questions/59960494/pyqt5-recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-o
# como salvar recursion x ventanas que se llaman


class clsNewMembership(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsNewMembership, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/Nuevamembresia.ui',self)

        self.setupUiComponents()
        
    def setupUiComponents(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newM = clsNewMembership()
    newM.show()
    app.exec_()

if __name__ == '__main__':
    main() 