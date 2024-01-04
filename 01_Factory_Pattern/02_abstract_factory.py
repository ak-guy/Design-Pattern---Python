'''
Abstract Factory pattern provides an interface for creating families of
related or dependent objects without specifying their concrete classes

Note : difference bw FP(Factory Pattern) and AFP(Abstract Factory Pattern)
       is FP helps in constructing single object whereas AFP helps in
       constructing multiple objects.

Reference ->
1. https://www.youtube.com/watch?v=v-GiuMmsXj4&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5
2. https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/AbstractFactory/Conceptual/main.py
'''

from abc import ABC, abstractmethod

''' class structure abstract factory which will be responsible for creating Product A and Product B '''
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteAbstractFactory1(AbstractFactory):
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class ConcreteAbstractFactory2(AbstractFactory):
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

''' class structure for Product A '''
class AbstractProductA(ABC):
    @abstractmethod
    def some_useful_function(self):
        pass

class ConcreteAbstractProductA1(AbstractProductA):
    def some_useful_function(self):
        pass

class ConcreteAbstractProductA2(AbstractProductA):
    def some_useful_function(self):
        pass

class ConcreteAbstractProductA3(AbstractProductA):
    def some_useful_function(self):
        pass


''' class structure for Product B '''
class AbstractProductB(ABC):
    @abstractmethod
    def some_useful_function(self):
        pass

class ConcreteAbstractProductB1(AbstractProductB):
    def some_useful_function(self):
        pass

class ConcreteAbstractProductB2(AbstractProductB):
    def some_useful_function(self):
        pass

class ConcreteAbstractProductB3(AbstractProductB):
    def some_useful_function(self):
        pass