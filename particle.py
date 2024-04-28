from PyQt5 import QtCore
from PyQt5 import QtGui
import ray

class Particle():
    def __init__(self, parent, posX, posY):
        self.parent = parent
        self.pos = QtCore.QPoint (posX, posY)
        self.rays = []

        for i in range(0, 360, 1):
            self.rays.append (ray.Ray(self.pos, i))

    def setPos(self, x, y):
        self.pos.setX(x)
        self.pos.setY(y)

    def showEllipse(self):
        return (self.pos,10,10)

    def showLines(self):
        return self.rays

    def update(self, walls):
        for i in self.rays:
            i.update(self.pos, walls)
            #i.col(wall)
