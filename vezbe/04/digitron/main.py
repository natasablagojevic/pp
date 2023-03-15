import digitron
from PyQt5 import QtCore, QtGui, QtWidgets
import functools

class MatfCalculator:
    def __init__(self):
         super(MatfCalculator, self).__init__()
         self.stupUI(self)

        lista_brojeva = [ 
            (self.pushButton_br0, '0'),
            (self.pushButton_br1, '1'), 
            (self.pushButton_br2, '2'), 
            (self.pushButton_br3, '3'), 
            (self.pushButton_br4, '4'), 
            (self.pushButton_br5, '5'), 
            (self.pushButton_br6, '6'), 
            (self.pushButton_br7, '7'), 
            (self.pushButton_br8, '8'), 
            (self.pushButton_br9, '9')
        ]
    
        self.valid_ops = '+-*/%'

        for btn, br in lista_brojeva:
            button.clicked.connect(functools(self.__display_digit, br))

        lista_operatora = [
            (self.pushButton_plus, '+'),
            (self.pushButton_minus, '-'),
            (self.pushButton_puta, '*'),
            (self.pushButton_mod, '%'),
            (self.pushButton_podeljeno, '/')
        ]

        for btn, op in lista_operatora:
            button.clicked.connect(functools(self.__display_op, op))

        # button jednakosti = pushButton_21
        button.clicked.connect(self.__evaluate)

    def __display_util(self, data):
        display = self.lineEdit
        display.insert(data)
            
    def __display_digit(self, digit):
        self.__display_util(digit)

    def __display_op(self, op):
        assert op in self.valid_ops
        self.__display_util(op)

    def __evaluate(self):
        display = self.lineEdit
        data = display.text()
        res = MatfCalculator.__evaluate_util(data)
        display.clear()
        display.insert(res)

    @staticmethod
    def __evaluate_util(self):
        return '442'       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Digitron = QtWidgets.QDialog()
    ui = MatfCalculator()
    ui.show()
    Digitron.show()
    sys.exit(app.exec_())


""" 
    za domaci:
    
    primer:
    23*9 - 4%3 + 6/3/2

    splitujemo po + i -
    i izracunamo 
"""
