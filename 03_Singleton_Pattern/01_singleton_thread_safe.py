from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                obj = super().__call__(*args, **kwargs)
                cls._instances[cls] = obj
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

def test_singleton():
    obj = Singleton()
    print(obj)

if __name__ == '__main__':
    Thread1 = Thread(target=test_singleton)
    Thread2 = Thread(target=test_singleton)

    Thread1.start()
    Thread2.start()