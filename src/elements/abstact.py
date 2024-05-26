from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self) -> None:
        pass

    def move(self) -> None:
        print("Moving...")


class Dog(Animal):
    def sound(self) -> None:
        print("Woof")


class Cat(Animal):
    def sound(self) -> None:
        print("Meow")
