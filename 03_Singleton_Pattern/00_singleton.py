'''
Singleton pattern ensures that the class has only one instance and provide a
global point of access to it.

The Singleton class can be implemented in different ways in Python. Some
possible methods include: base class, decorator, metaclass. We will use the
metaclass because it is best suited for this purpose.


'''

class SingletonMeta(type):
    '''here we will store the instance in one private class variable and while creating object
    or instantiating the class we will if any instance of Singleton is present in this private
    variable, if it does then we simply return that instance otherwise we create an instance
    using super().__call__ method'''
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # can use this too -> 
            # instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            instance = super().__call__(*args, **kwargs)
            print(instance)
            cls._instances[cls] = instance
        return cls._instances[cls]

# we will use metaclass to override __call__ method
class Singleton(metaclass=SingletonMeta):
    # some bussiness logic
    pass

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
if id(obj1) == id(obj2):
    print("Same id of two instances of Singleton type meaning only one instances has been created")
else:
    print("they are both different instances")