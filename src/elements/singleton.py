class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        print(cls._instances)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta): ...


a = Singleton()
b = Singleton()

print(a is b)  # Output: True
