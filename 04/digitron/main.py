import digitron
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Digitron = QtWidgets.QDialog()
    ui = Ui_Digitron()
    ui.setupUi(Digitron)
    Digitron.show()
    sys.exit(app.exec_())
