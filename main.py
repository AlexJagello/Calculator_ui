import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Calculator import Calculator

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())