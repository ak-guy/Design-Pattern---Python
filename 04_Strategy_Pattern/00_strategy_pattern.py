'''
The strategy pattern defined a family of algorithms, it encapsulates each one and makes them interchangeable.
Strategy lets the algorithm vary independently from client that use it.

Reference : 
1. https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc
2. https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Strategy/Conceptual/main.py
'''
from abc import ABC, abstractmethod

class Duck:
    def __init__(self, speak: SpeakStrategy, fly: FlyStrategy):
        self._speak = speak
        self._fly = fly

    @property
    def do_speak(self):
        return self._speak
    
    @do_speak.setter
    def do_speak(self, speak):
        self._speak = speak
    
    @property
    def do_fly(self):
        return self._fly
    
    @do_fly.setter
    def do_fly(self, fly):
        self._fly = fly

    def do_logic(self):
        return_val = self.do_speak.algorithm('Arpit')
        return_val = return_val + "   " + self.do_fly.algorithm()
        print(return_val)
    
class SpeakStrategy(ABC):
    @abstractmethod
    def algorithm(self):
        pass

class SpeakStrategyA(SpeakStrategy):
    def algorithm(self, text: str):
        return "-".join(char for char in text)

class SpeakStrategyB(SpeakStrategy):
    def algorithm(self, text: str):
        return "_".join(char for char in text)

class FlyStrategy(ABC):
    @abstractmethod
    def algorithm(self):
        pass

class FlyStrategyA(FlyStrategy):
    def algorithm(self):
        return "flying with jet motor"

class FlyStrategyB(FlyStrategy):
    def algorithm(self):
        return "flying with fan motor"
    
if __name__ == '__main__':
    obj1 = Duck(SpeakStrategyA(), FlyStrategyB())
    print(obj1.do_logic())