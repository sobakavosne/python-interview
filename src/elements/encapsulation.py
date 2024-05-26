class EncapsulationExample:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self._age = age  # protected attribute
        self.__salary = 0  # private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

    def get_salary(self):
        return self.__salary


person = EncapsulationExample("Alice", 30)

print(person.name)

# Accessing protected attribute (not recommended)
print(person._age)

# print(person.__salary)  # This will raise an AttributeError

person.set_salary(50000)
print(person.get_salary())  # Output: 50000

person.display_info()
