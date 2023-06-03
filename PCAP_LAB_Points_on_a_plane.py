# %% PCAP LAB ---> Points on a plane my hypot() solution
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__coordinates = {"x": x, "y": y}

    def getx(self):
        return self.__coordinates["x"]

    def gety(self):
        return self.__coordinates["y"]

    def distance_from_xy(self, x, y):
        return math.hypot(self.getx() - x, self.gety() - y)

    def distance_from_point(self, point):
        return math.hypot(self.getx() - point.getx(), self.gety() - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


# %% PCAP LAB ---> Points on a plane my dist() solution
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__coordinates = {"x": x, "y": y}

    def getx(self):
        return self.__coordinates["x"]

    def gety(self):
        return self.__coordinates["y"]

    def distance_from_xy(self, x, y):
        return math.dist((self.getx(), self.gety()), (x, y))

    def distance_from_point(self, point):
        return math.dist((self.getx(), self.gety()), (point.getx(), point.gety()))


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


# %% PCAP LAB ---> Points on a plane sample solution
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
