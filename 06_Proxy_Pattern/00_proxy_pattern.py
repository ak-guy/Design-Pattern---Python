'''
Proxy Pattern provides a surrogate or placeholder for another object to
control access to it

Reference:
1. https://www.youtube.com/watch?v=NwaabHqPHeM
2. https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Proxy/Conceptual/main.py 
'''

from abc import ABC, abstractmethod
from datetime import datetime

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print('This is RealSubject handling request')

class ProxySubject(Subject):
    def __init__(self, obj: RealSubject):
        self._real_subject_obj = obj

    def request(self):
        if self.check_access():
            self._real_subject_obj.request()
            print("made Proxy request at {}".format(datetime.utcnow()))
    
    def check_access(self):
        print("checking access via proxy")
        return True

def client_code(subject: Subject):
    subject.request()

if __name__ == '__main__':
    print("Client: Executing the client code with a real subject:")
    realsubject_obj = RealSubject()
    client_code(realsubject_obj)

    print('\n')

    print("Client: Executing the same client code with a proxy:")
    proxysubject_obj = ProxySubject(realsubject_obj)
    client_code(proxysubject_obj)