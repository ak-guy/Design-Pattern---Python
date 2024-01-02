'''
ISP -> Interface Segregation Principle => The principle states that many client-specific interfaces are better
than one general-purpose interface. Clients should not be forced to implement a function they do not need. 
'''
class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
class MultiFunctionalPrinter(Machine):
    def print(self, document):
        pass
    
    def scan(self, document):
        pass
    
    def fax(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        pass
    
    def scan(self, document):
        '''Does not work for Old Fashioned Printer'''
        pass
    
    def fax(self, document):
        '''Does not work for Old Fashioned Printer'''
        pass

'''
So the idea of interface segregation is basically that having one large interface with several members in it,
what we should do is keep things granular
'''
from abc import abstractmethod
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

'''
So takeaway from this is, that making interfaces which feature too many elements is not a good idea bcz we are
forcing our developer to define methods, which they might not even need
'''