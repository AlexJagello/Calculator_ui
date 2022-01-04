import operator
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLCDNumber, QMainWindow
from PyQt5.QtGui import QIcon

from mainWindow import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        self.setupUi(self)

        for n in range(1, 10):
            getattr(self, 'pushButton_%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        self.pushButton_0.pressed.connect(lambda v=0: self.input_number(v))
        self.pushButton_delete.pressed.connect(self.delete)
        self.pushButton_delete_all.pressed.connect(self.deleteAll)
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_substraction.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_multiplication.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_devision.pressed.connect(lambda: self.operation(operator.truediv))
        self.pushButton_equals.pressed.connect(self.equals)
        self.reset()
        self.show()

    def display(self):
        self.lcdNumber.display(self.stack[-1])

    def reset(self):
        self.stack = [0]
        self.stack_op = [operator.add]

    def input_number(self, v):
        self.stack[-1] = self.stack[-1] * 10 + v
        self.display()

    def delete(self):
        self.stack[-1] = int(self.stack[-1]/10)
        self.display()

    def deleteAll(self):
        self.stack[-1] = 0
        self.display()

    def operation(self, op):
        self.stack_op.append(op)
        self.stack.append(0)
        self.display()

    def equals(self):
        s = 0
        for i in range(0, self.stack.__len__()):
            s = self.stack_op[i](s, self.stack[i])
        self.stack.clear()
        self.reset()
        self.stack[-1] = s
        self.display()
