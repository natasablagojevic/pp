import random
import string
import time

import progress_bar
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

__author__ = 'Natasa Blagojevic'
class Hacker(progress_bar.Ui_MainWindow, QtWidgets.QMainWindow):
    def __int__(self):
        super().__init__()

        # setup-ovali smo samog sebe jer je on main window
        self.setupUi(self)

        self.pushButton_start.connect(self.hack)

    def hack(self):
        print('Engine started...')

        for i in range(101):
            self.progressBar.setProperty('value', i)
            if (i % 5 == 0):
                print("..{}..".format(''.random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = random.randint(5, 10))))

            time.sleep(0.1)

        print('Hack successful')





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    hacker = Hacker()
    hacker.show()

    # pozvaces main, ali ces biti blokiran sve dok se moja aplikacija izvrasava
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

