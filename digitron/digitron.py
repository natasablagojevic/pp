# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digitron.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Digitron(object):
    def setupUi(self, Digitron):
        Digitron.setObjectName("Digitron")
        Digitron.resize(332, 490)
        Digitron.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.lineEdit_input = QtWidgets.QLineEdit(Digitron)
        self.lineEdit_input.setGeometry(QtCore.QRect(10, 20, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_clear = QtWidgets.QPushButton(Digitron)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 90, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_del = QtWidgets.QPushButton(Digitron)
        self.pushButton_del.setGeometry(QtCore.QRect(90, 90, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_ADD = QtWidgets.QPushButton(Digitron)
        self.pushButton_ADD.setGeometry(QtCore.QRect(170, 90, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ADD.setFont(font)
        self.pushButton_ADD.setObjectName("pushButton_ADD")
        self.pushButton_SUB = QtWidgets.QPushButton(Digitron)
        self.pushButton_SUB.setGeometry(QtCore.QRect(250, 90, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SUB.setFont(font)
        self.pushButton_SUB.setObjectName("pushButton_SUB")
        self.pushButton_br8 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br8.setGeometry(QtCore.QRect(90, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br8.setFont(font)
        self.pushButton_br8.setObjectName("pushButton_br8")
        self.pushButton_br7 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br7.setGeometry(QtCore.QRect(10, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br7.setFont(font)
        self.pushButton_br7.setObjectName("pushButton_br7")
        self.pushButton_MUL = QtWidgets.QPushButton(Digitron)
        self.pushButton_MUL.setGeometry(QtCore.QRect(250, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_MUL.setFont(font)
        self.pushButton_MUL.setObjectName("pushButton_MUL")
        self.pushButton_br9 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br9.setGeometry(QtCore.QRect(170, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br9.setFont(font)
        self.pushButton_br9.setObjectName("pushButton_br9")
        self.pushButton_br3 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br3.setGeometry(QtCore.QRect(170, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br3.setFont(font)
        self.pushButton_br3.setObjectName("pushButton_br3")
        self.pushButton_DIV = QtWidgets.QPushButton(Digitron)
        self.pushButton_DIV.setGeometry(QtCore.QRect(250, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_DIV.setFont(font)
        self.pushButton_DIV.setObjectName("pushButton_DIV")
        self.pushButton_br2 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br2.setGeometry(QtCore.QRect(90, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br2.setFont(font)
        self.pushButton_br2.setObjectName("pushButton_br2")
        self.pushButton_br1 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br1.setGeometry(QtCore.QRect(10, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br1.setFont(font)
        self.pushButton_br1.setObjectName("pushButton_br1")
        self.pushButton_EQ = QtWidgets.QPushButton(Digitron)
        self.pushButton_EQ.setGeometry(QtCore.QRect(250, 410, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EQ.setFont(font)
        self.pushButton_EQ.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.pushButton_EQ.setObjectName("pushButton_EQ")
        self.pushButton_MOD = QtWidgets.QPushButton(Digitron)
        self.pushButton_MOD.setGeometry(QtCore.QRect(250, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_MOD.setFont(font)
        self.pushButton_MOD.setObjectName("pushButton_MOD")
        self.pushButton_br0 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br0.setGeometry(QtCore.QRect(10, 410, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br0.setFont(font)
        self.pushButton_br0.setObjectName("pushButton_br0")
        self.pushButton_br4 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br4.setGeometry(QtCore.QRect(10, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br4.setFont(font)
        self.pushButton_br4.setObjectName("pushButton_br4")
        self.pushButton_br5 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br5.setGeometry(QtCore.QRect(90, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br5.setFont(font)
        self.pushButton_br5.setObjectName("pushButton_br5")
        self.pushButton_br6 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br6.setGeometry(QtCore.QRect(170, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br6.setFont(font)
        self.pushButton_br6.setObjectName("pushButton_br6")

        self.retranslateUi(Digitron)
        QtCore.QMetaObject.connectSlotsByName(Digitron)

    def retranslateUi(self, Digitron):
        _translate = QtCore.QCoreApplication.translate
        Digitron.setWindowTitle(_translate("Digitron", "Dialog"))
        self.pushButton_clear.setText(_translate("Digitron", "C"))
        self.pushButton_del.setText(_translate("Digitron", "DEL"))
        self.pushButton_ADD.setText(_translate("Digitron", "+"))
        self.pushButton_SUB.setText(_translate("Digitron", "-"))
        self.pushButton_br8.setText(_translate("Digitron", "8"))
        self.pushButton_br7.setText(_translate("Digitron", "7"))
        self.pushButton_MUL.setText(_translate("Digitron", "*"))
        self.pushButton_br9.setText(_translate("Digitron", "9"))
        self.pushButton_br3.setText(_translate("Digitron", "3"))
        self.pushButton_DIV.setText(_translate("Digitron", "/"))
        self.pushButton_br2.setText(_translate("Digitron", "2"))
        self.pushButton_br1.setText(_translate("Digitron", "1"))
        self.pushButton_EQ.setText(_translate("Digitron", "="))
        self.pushButton_MOD.setText(_translate("Digitron", "MOD"))
        self.pushButton_br0.setText(_translate("Digitron", "0"))
        self.pushButton_br4.setText(_translate("Digitron", "4"))
        self.pushButton_br5.setText(_translate("Digitron", "5"))
        self.pushButton_br6.setText(_translate("Digitron", "6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Digitron = QtWidgets.QDialog()
    ui = Ui_Digitron()
    ui.setupUi(Digitron)
    Digitron.show()
    sys.exit(app.exec_())