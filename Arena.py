from PyQt5 import QtGui, QtWidgets, QtCore, Qt
import sys
import ray
import boundary
import particle
import random


class Arena(QtWidgets.QWidget):
    def __init__(self):
        super(Arena, self).__init__()

        self.setGeometry(2500, 400, 500, 500)
        self.pal = QtGui.QPalette()
        self.pal.setColor(QtGui.QPalette.Background, QtGui.QColor(0, 0, 0))
        self.setPalette(self.pal)

        self.wall_brush_circle = QtGui.QBrush()
        self.wall_brush_circle.setStyle(QtCore.Qt.SolidPattern)
        self.wall_brush_circle.setColor(QtGui.QColor(255, 255, 255))

        self.wall_brush_colPoint = QtGui.QBrush()
        self.wall_brush_colPoint.setStyle(QtCore.Qt.SolidPattern)
        self.wall_brush_colPoint.setColor(QtGui.QColor(255, 0, 0, 100))

        self.pen_boundary = QtGui.QPen()
        self.pen_boundary.setColor(QtGui.QColor(255, 255, 255))

        self.pen_colPoint = QtGui.QPen()
        self.pen_colPoint.setColor(QtGui.QColor(200, 0, 0))

        self.mousePos = QtCore.QPointF(0, 0)

        self.walls = []
        self.walls = self.walls + [
            boundary.Boundary(0, 0, self.width(), 0 ),
            boundary.Boundary(self.width(), 0, self.width(), self.height()),
            boundary.Boundary(self.width(), self.height(), 0, self.height()),
            boundary.Boundary(0, self.height(), 0, 0),
            ]
        for w in range(8):
            self.walls.append(boundary.Boundary(random.randint(0, self.width()),
                                                random.randint(0, self.height()),
                                                random.randint(0, self.width()),
                                                random.randint(0, self.height())))


        # self.colPoints = []

        self.particle = particle.Particle(self, 200, 200)

    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing)

        # p.setBrush(self.wall_brush_circle)
        # p.drawEllipse(self.mousePos, 5, 5)

        # boundaries
        p.setPen(self.pen_boundary)
        for b in self.walls:
            p.drawLine(b.a, b.b)

        # rays
        p.setBrush(self.wall_brush_colPoint)
        # for i in self.rays:
        #     p.drawLine(i.sourcePos, i.destPos)
        #     p.setPen(self.pen_colPoint)
        #     #colision circle
        #
        #     if i.colPos :
        #         p.drawEllipse(i.colPos, 5, 5)

        p.drawEllipse(*self.particle.showEllipse())
        # p.drawLines(*self.particle.showLines())
        for part in self.particle.showLines():
            # print (part.rayDir)
            p.drawLine(part.sourcePos, part.destPos)

    def mouseMoveEvent(self, e):
        self.mousePos.setX(e.x())
        self.mousePos.setY(e.y())

        self.particle.setPos(e.x(), e.y())
        self.particle.update(self.walls)

        self.update()
        # self.draw ()
        # for r in self.rays:
        #     r.lookAt(e.x(), e.y())
        #     r.col(self.walls)

    # def draw (self):
    # rays
    # p.setPen(self.pen_boundary)
    # for i in self.rays:
    #     i.setPos(x, y)
    #     i.col(self.walls)
    # collisions
    # p.drawEllipse(self.r.colPos, 5, 5)


app = QtWidgets.QApplication(sys.argv)
Arena = Arena()
Arena.show()
app.exec_()
