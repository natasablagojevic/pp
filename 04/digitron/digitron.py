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
        Digitron.resize(334, 469)
        font = QtGui.QFont()
        font.setPointSize(17)
        Digitron.setFont(font)
        Digitron.setStyleSheet("background-color: rgb(192, 191, 188)")
        self.lineEdit = QtWidgets.QLineEdit(Digitron)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 311, 71))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_br1 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br1.setGeometry(QtCore.QRect(10, 180, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br1.setFont(font)
        self.pushButton_br1.setObjectName("pushButton_br1")
        self.pushButton_br2 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br2.setGeometry(QtCore.QRect(90, 180, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br2.setFont(font)
        self.pushButton_br2.setObjectName("pushButton_br2")
        self.pushButton_br5 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br5.setGeometry(QtCore.QRect(90, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br5.setFont(font)
        self.pushButton_br5.setObjectName("pushButton_br5")
        self.pushButton_br0 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br0.setGeometry(QtCore.QRect(10, 390, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br0.setFont(font)
        self.pushButton_br0.setObjectName("pushButton_br0")
        self.pushButton_plus = QtWidgets.QPushButton(Digitron)
        self.pushButton_plus.setGeometry(QtCore.QRect(170, 110, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_br9 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br9.setGeometry(QtCore.QRect(170, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br9.setFont(font)
        self.pushButton_br9.setObjectName("pushButton_br9")
        self.pushButton_br7 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br7.setGeometry(QtCore.QRect(10, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br7.setFont(font)
        self.pushButton_br7.setObjectName("pushButton_br7")
        self.pushButton_br4 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br4.setGeometry(QtCore.QRect(10, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br4.setFont(font)
        self.pushButton_br4.setObjectName("pushButton_br4")
        self.pushButton_br3 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br3.setGeometry(QtCore.QRect(170, 180, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br3.setFont(font)
        self.pushButton_br3.setObjectName("pushButton_br3")
        self.pushButton_br6 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br6.setGeometry(QtCore.QRect(170, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br6.setFont(font)
        self.pushButton_br6.setObjectName("pushButton_br6")
        self.pushButton_br8 = QtWidgets.QPushButton(Digitron)
        self.pushButton_br8.setGeometry(QtCore.QRect(90, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_br8.setFont(font)
        self.pushButton_br8.setObjectName("pushButton_br8")
        self.pushButton_podeljeno = QtWidgets.QPushButton(Digitron)
        self.pushButton_podeljeno.setGeometry(QtCore.QRect(250, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_podeljeno.setFont(font)
        self.pushButton_podeljeno.setObjectName("pushButton_podeljeno")
        self.pushButton_l = QtWidgets.QPushButton(Digitron)
        self.pushButton_l.setGeometry(QtCore.QRect(90, 110, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_l.setFont(font)
        self.pushButton_l.setObjectName("pushButton_l")
        self.pushButton_mod = QtWidgets.QPushButton(Digitron)
        self.pushButton_mod.setGeometry(QtCore.QRect(250, 320, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.pushButton_puta = QtWidgets.QPushButton(Digitron)
        self.pushButton_puta.setGeometry(QtCore.QRect(250, 180, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_puta.setFont(font)
        self.pushButton_puta.setObjectName("pushButton_puta")
        self.pushButton_minus = QtWidgets.QPushButton(Digitron)
        self.pushButton_minus.setGeometry(QtCore.QRect(250, 110, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_clear = QtWidgets.QPushButton(Digitron)
        self.pushButton_clear.setGeometry(QtCore.QRect(10, 110, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_21 = QtWidgets.QPushButton(Digitron)
        self.pushButton_21.setGeometry(QtCore.QRect(250, 390, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.pushButton_21.setObjectName("pushButton_21")

        self.retranslateUi(Digitron)
        self.pushButton_clear.clicked.connect(self.lineEdit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Digitron)

    def retranslateUi(self, Digitron):
        _translate = QtCore.QCoreApplication.translate
        Digitron.setWindowTitle(_translate("Digitron", "Dialog"))
        self.pushButton_br1.setText(_translate("Digitron", "1"))
        self.pushButton_br2.setText(_translate("Digitron", "2"))
        self.pushButton_br5.setText(_translate("Digitron", "5"))
        self.pushButton_br0.setText(_translate("Digitron", "0"))
        self.pushButton_plus.setText(_translate("Digitron", "+"))
        self.pushButton_br9.setText(_translate("Digitron", "9"))
        self.pushButton_br7.setText(_translate("Digitron", "7"))
        self.pushButton_br4.setText(_translate("Digitron", "4"))
        self.pushButton_br3.setText(_translate("Digitron", "3"))
        self.pushButton_br6.setText(_translate("Digitron", "6"))
        self.pushButton_br8.setText(_translate("Digitron", "8"))
        self.pushButton_podeljeno.setText(_translate("Digitron", "/"))
        self.pushButton_l.setText(_translate("Digitron", "DEL"))
        self.pushButton_mod.setText(_translate("Digitron", "MOD"))
        self.pushButton_puta.setText(_translate("Digitron", "*"))
        self.pushButton_minus.setText(_translate("Digitron", "-"))
        self.pushButton_clear.setText(_translate("Digitron", "C"))
        self.pushButton_21.setText(_translate("Digitron", "="))


# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # Digitron = QtWidgets.QDialog()
    # ui = Ui_Digitron()
    # ui.setupUi(Digitron)
    # Digitron.show()
    # sys.exit(app.exec_())
