from typing import List


class Person:
    origin_country = "USA"

    def __init__(
        self, first_name: str, last_name: str, age: int, gender: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def speak(self, words: List) -> None:
        print(f"{self.first_name} speaks: {words}")

    @classmethod
    def change_origin_country(cls, new_country: str) -> None:
        cls.origin_country = new_country

    @staticmethod
    def is_adult(age: int) -> bool:
        return age > 18

    @property
    def email(self) -> str:
        return f"{self.first_name}.{self.last_name}@email.com"


person1 = Person("John", "Doe", 20, "Male")
person2 = Person("John", "Doe", 20, "Male")

# person.change_origin_country("UK")

person1.change_origin_country("UK")

print(person1.origin_country)  # output: UK
print(person2.origin_country)  # output: UK
