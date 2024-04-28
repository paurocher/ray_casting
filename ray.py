from PyQt5 import QtCore
import math

class Ray():
    def __init__(self, pos, angle):
        self.sourcePos = pos
        self.rayLength = 2
        self.angle = angle
        self.destPos = self.angleToVect(self.angle)

        self.colPos = None



    def angleToVect(self, angle):
        angleRad = angle * math.pi / 180.
        p = QtCore.QPointF(math.sin (angleRad), math.cos(angleRad)) * self.rayLength + self.sourcePos
        return p

    # def lookAt(self, x, y):
    #     self.destPos.setX(x)
    #     self.destPos.setY(y)
    #
    #     #print (self.destPos)
    #     #print (self.sourcePos)
    #     v = self.destPos - self.sourcePos
    #     #self.destPos = v
    #     a = self.normalize(v.x(), v.y())
    #     self.destPos = (a * self.rayLength + self.sourcePos)


    def normalize(self, x, y):
        #hypot of triangle of the two segments above
        hyp = math.hypot (x, y)
        #print ('hypot = ', hyp)
        return (QtCore.QPointF(x/hyp, y/hyp))


    def col(self, wall):
        pt = self.cast(wall)
        if pt:
            self.colPos = pt

            return pt
        else:
            self.colPos = None

    def cast(self, wall):
        x1 = wall.a.x()
        y1 = wall.a.y()
        x2 = wall.b.x()
        y2 = wall.b.y()

        x3 = self.sourcePos.x()
        y3 = self.sourcePos.y()
        x4 = self.destPos.x()
        y4 = self.destPos.y()

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0 : return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den


        if t > 0 and t < 1 and u > 0:
            xx = x1 + t * (x2 - x1)
            yy = y1 +t * (y2 - y1)
            pt = QtCore.QPointF (xx, yy)
            return pt
        else:
            return False

    def update(self, pos, walls):
        walls = walls
        self.destPos = self.angleToVect(self.angle)
        closest = None
        record = 10000000
        for wall in walls:
            col = self.col (wall)
            if col:
                d = math.sqrt( (col.x()-self.destPos.x())**2 + (col.y()-self.destPos.y())**2 )
                if d < record:
                    record = d
                    closest = col
                    record = min(d, record)
        if closest:
            self.destPos = closest

