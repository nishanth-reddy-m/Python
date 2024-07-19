from math import hypot

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return hypot(abs(self.__x - x), abs(self.__y - y))
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(),point.gety())

class Triangle:
    def __init__(self, t1, t2, t3):
        self.__t = [t1, t2, t3]
    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__t[i].distance_from_point(self.__t[(i+1) % 3])
        return per

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())