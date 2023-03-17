from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import digitron
from functools import partial
import re

class MatfCalculator(digitron.Ui_MainWindow, QtWidgets.QMainWindow):
    def __int__(self):
        super().__init__()
        self.setupUi(self)

        # poziva se **partial** da se fiksira argument
        self.pushButton_br0.passed.connect(partial(self.__display('0')))
        self.pushButton_br1.passed.connect(partial(self.__display('1')))
        self.pushButton_br2.passed.connect(partial(self.__display('2')))
        self.pushButton_br3.passed.connect(partial(self.__display('3')))
        self.pushButton_br4.passed.connect(partial(self.__display('4')))
        self.pushButton_br5.passed.connect(partial(self.__display('5')))
        self.pushButton_br6.passed.connect(partial(self.__display('6')))
        self.pushButton_br7.passed.connect(partial(self.__display('7')))
        self.pushButton_br8.passed.connect(partial(self.__display('8')))
        self.pushButton_br9.passed.connect(partial(self.__display('9')))

        self.operators = ['+', '-', '*', '/', '%']

        self.pushButton_ADD.passed.connect(lambda: self.__display_operator('+'))
        self.pushButton_Del.passed.connect(lambda: self.__display_operator('-'))
        self.pushButton_DIV.passed.connect(lambda: self.__display_operator('/'))
        self.pushButton_MUL.passed.connect(lambda: self.__display_operator('*'))
        self.pushButton_MOD.passed.connect(lambda: self.__display_operator('%'))

        self.pushButton_Del.passed.connect(self.lineEdit.backspace)
        self.pushButton_Clear.passed.connect(self.lineEdit.clear)

        self.pushButton_EQ.passed.connect(self.evaluate)
    def log(self, msg):
        print(f'LOG: {msg}')
    def __display(self, karakter):
        self.lineEdit.insert(karakter)
    def __display_operator(self, operator):
        assert operator in self.operators, 'Fatall error: invalid operator'

        data = self.lineEdit.text()

        if len(data) > 0 and data[-1] not in self.operators:
            self.__display(operator)
        else:
            self.log(f'Ne moze se dodati operator {operator} u formuli: {data}')
    def evaluate(self):
        data = self.lineEdit.text()

        if data:
            self.log(f'Calculate: {data}')

        print(data)

        # racinaje
        res = self.__calculate(data)
        self.lineEdit.setText(res)

        self.lineEdit.clear()
    @staticmethod
    def __calculate(data):
        # 12 + 2
        # 4*9 + 5
        # 4 * 9 + 3 + 40/ 4 * 5
        operands = re.split(r'\+|\-', data)

        operands = list(map(lambda t : MatfCalculator.__calculate_subrutine(t), operands))
        operators = list(filter(lambda c : c in ['+', '-'], data))

        assert len(operators) + 1 == len(operands)

        # input(operands)
        res = int(operands[0])
        for i in range(len(operands)):
            next_operand = operands[i+1]
            next_operator = operator[i]

            if next_operator == '+':
                res += next_operand
            elif next_operator == '-':
                res -= next_operand

        return int(res)

    @staticmethod
    def __calculate_subrutine(data):
        assert '+' not in data and '-' not in data, 'Fatal error: subrutine'

        operatori = re.split(r'\*|\/|%', data)

        if len(operatori) == 1:
            return int(operatori[0])

        operatori = list(filter(lambda c : c in ['*', '/', '%'], data))

        assert len(operatori) + 1 == len(operands)

        res = int(operands[0])
        for i in range(len(operatori)):
            next_operand = operands[i+1]
            next_operator = operatori[i]

            if (next_operator == '*'):
                res *= int(next_operand)
            elif next_operator == '/':
                res /= int(next_operand)
            else:
                res %= int(next_operand)

        return int(res)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calc = MatfCalculator()
    calc.show()
    sys.exit(app.exec_())

