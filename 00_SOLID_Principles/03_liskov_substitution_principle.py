''' 
LSP -> Liskov Substitution Principle => The Liskov Substitution Principle states that subclasses should be substitutable for their base
classes. This means that, given that class B is a subclass of class A, we should be able to pass an object of class B to any method that 
expects an object of class A and the method should not give any weird output in that case.

This is the expected behavior, because when we use inheritance we assume that the child class inherits everything that the superclass has. 
The child class extends the behavior but never narrows it down. 
'''

class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

sc = Square(5)
use_it(sc)

'''
if we look at the output for sc we got -> Expected an area of 50, got 100
This happend bcz of (rc.height = 10) changed width of the Square. Hence the function use_it() works only on 
Rectangle and not on any derived classes and this is a direct violation of LSP, which states that whenever you have
an interface taking some sort of base class, you should be able to stick in any of its inheritors. So if we take
Rectangle, we should be able to stick in a Square in there and everything should work correctly
'''