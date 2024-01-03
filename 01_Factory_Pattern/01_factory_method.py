'''
Factory Method is a creational design pattern that provides an interface
for creating objects in a superclass, but allows subclasses to alter the
type of objects that will be created.
'''
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class PointFactory:
    @staticmethod
    def cartesian_system(x, y):
        return Point(x, y)

    @staticmethod
    def polar_system(rho, theta):
        return Point(rho*cos(rho), theta*sin(theta))

class Point:
    factory = PointFactory() 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'
    
    # # we will use this __init__ if we were to pass point system, but if in future we were to add more coordinate system then again we have to add more conditions
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(a)
    #         self.y = b * sin(b)

obj1 = Point.factory.cartesian_system(1,3)
print(obj1)

obj2 = Point.factory.polar_system(1,3)
print(obj2)