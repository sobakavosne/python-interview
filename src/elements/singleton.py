from typing import Type, Any, Dict


class SingletonMeta(type):
    _instances: Dict[Type["Singleton"], Any] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        # print(cls._instances)
        print(type(cls._instances[cls]))
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta): ...


a = Singleton()
b = Singleton()

print(a is b)  # Output: True
