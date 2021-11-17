from PyQt5 import QtCore, QtWidgets, uic


import traceback
import sys



class clsNewMember(QtWidgets.QMainWindow):
    def __init__(self):
        super(clsNewMember, self).__init__()
        uic.loadUi('C:/Users/rodri/Desktop/Trabajo Final python/Pantallas qt/Nuevosocio.ui',self)

        self.setupUiComponents()
        
    def setupUiComponents(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    newMs = clsNewMember()
    newMs.show()
    app.exec_()

if __name__ == '__main__':
    main() 