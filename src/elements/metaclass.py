class UppercaseAttributesMeta(type):
    def __new__(
        cls, name: str, bases: tuple, dct: dict
    ) -> "UppercaseAttributesMeta":
        uppercase_attrs = {}
        for name, val in dct.items():
            if not name.startswith("__"):
                uppercase_attrs[name.upper()] = val
            else:
                uppercase_attrs[name] = val
        print(uppercase_attrs)
        return super().__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UppercaseAttributesMeta):
    foo = "bar"
    baz = "qux"


obj = MyClass()

# Attributes will be uppercase
print(hasattr(MyClass, "foo"))  # Output: False
print(hasattr(MyClass, "FOO"))  # Output: True
