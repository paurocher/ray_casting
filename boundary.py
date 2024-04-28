from PyQt5 import QtCore

class Boundary():
    def __init__(self, x1, y1, x2, y2):

        self.a = QtCore.QPointF(x1, y1)
        self.b = QtCore.QPointF(x2, y2)

        self.ret()

    def ret(self):
        return (self.a, self.b)