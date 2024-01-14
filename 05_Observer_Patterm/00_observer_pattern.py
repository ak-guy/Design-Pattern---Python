'''
Lets us define a subscription mechanism to notify multiple objects about any
events that happen to the object they are observing

Reference:
1. https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Observer/Conceptual/main.py
2. https://www.youtube.com/watch?v=_BpmfnqjgzQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=2
'''
from abc import abstractmethod, ABC
from random import randint

# # # # Observer/Subscriber/Listner/Tracker implementation # # # #
class IObserver(ABC):
    @staticmethod
    def update(self, observable_state: int):
        pass

class SmartPhone(IObserver):
    def update(self, observable_state: int):
        print(f'new state change received, {observable_state}')

class WindowPhone(IObserver):
    def update(self, observable_state: int):
        print(f'new state change received, {observable_state}')

# # # # Observable Implementation # # # #
class IObservable(ABC):
    @staticmethod
    def add_subscription(self, obj: IObserver):
        pass

    @staticmethod
    def remove_subscription(self, obj: IObserver):
        pass

    @staticmethod
    def notify_observer(self):
        pass

class WeatherStation(IObservable):
    _state: int = None
    _observer_list: set = set()

    def add_subscription(self, obj: IObserver):
        self._observer_list.add(obj)

    def remove_subscription(self, obj: IObserver):
        self._observer_list.remove(obj)
    
    def notify_observer(self):
        print(f'Notifying {self._observer_list}')
        for observer in self._observer_list:
            observer.update(self._state)
    
    def some_logic(self):
        prev_state: int = self._state
        self._state: int = randint(0,100)
        print(f"Subject: state changed from {prev_state} to: {self._state}")
        self.notify_observer()

if __name__ == '__main__':
    observable_object: WeatherStation = WeatherStation()
    observing_obj1: SmartPhone = SmartPhone()
    observing_obj2: WindowPhone = WindowPhone()

    observable_object.add_subscription(observing_obj1)
    observable_object.add_subscription(observing_obj2)

    observable_object.some_logic()
    observable_object.some_logic()
    observable_object.some_logic()

    observable_object.remove_subscription(observing_obj1)
    observable_object.some_logic()