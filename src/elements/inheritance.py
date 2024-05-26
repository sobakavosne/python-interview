# Diamond problem


class Base:
    def method(self):
        print("Method from Base")


class Parent1(Base):
    def method(self):
        print("Method from Parent1")


class Parent2(Base):
    def method(self):
        print("Method from Parent2")


class Child(Parent1, Parent2): ...


# Creating an instance of Child class
child_instance = Child()

# Calling the method to see which parent class method is invoked
child_instance.method()  # Output: Method from Parent1

# Viewing the Method Resolution Order
print(
    Child.__mro__
)  # Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Base'>, <class 'object'>)

# print(Child.__class__.__dict__)
