'''
Factory Method is a creational design pattern that provides an interface
for creating objects in a superclass, but allows subclasses to alter the
type of objects that will be created.


Reference -> https://www.youtube.com/watch?v=EcFVTgRHJLM&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=4
'''

from abc import ABC, abstractmethod
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Turtle(Animal):
    pass

class AnimalFactory(ABC):
    ''' "provides an interface for creating objects in a superclass" '''
    '''this work as an interface for creating Animal objects'''
    @abstractmethod
    def create_obj(self):
        pass

class RandomAnimalFactory(AnimalFactory):
    ''' "but allows subclasses to alter the type of objects that will be created" '''
    '''will use this class to create random animal'''
    def create_obj(self) -> Animal:
        # do some business logic
        pass

class BalancedAnimalFactory(AnimalFactory):
    ''' "but allows subclasses to alter the type of objects that will be created" '''
    '''will use this class to create balanced animal'''
    def create_obj(self) -> Animal:
        # do some business logic
        pass

