"""
*What is this pattern about?

In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.

The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.

*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the factory we chose (Dog or Cat, or random_animal)
This works because both Dog/Cat and random_animal respect a common
interface (callable for creation and .speak()).
Now my application can create pets abstractly and decide later,
based on my own criteria, dogs over cats.

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/abstract_factory

Note: Provides a way to encapsulate a group of individual factories.
"""
import random
from typing import Type
from abc import ABC

class Pet:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def do_speak(self) -> None:
        raise NotImplementedError
    
    def __str__(self) -> None:
        raise NotImplementedError

class Dog(Pet):
    def do_speak(self) -> None:
        print('woof')
    
    def __str__(self) -> None:
        return f'Dog {self.name}'

class Cat(Pet):
    def do_speak(self) -> None:
        print('meow')
    
    def __str__(self) -> None:
        return f'Cat(name={self.name})'
    
class PetFactory:
    def __init__(self, animal: Type[Pet]) -> None:
        self.pet_factory = animal

    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f'Here is your lovely {pet}')
        return pet
    
if __name__ == '__main__':
    pet1 = PetFactory(Dog)
    print(pet1.__dict__)
    pet = pet1.buy_pet('Tommy')
    print(pet.do_speak())
    print('='*20)