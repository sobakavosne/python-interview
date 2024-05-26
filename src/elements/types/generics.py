from __future__ import annotations

from typing import TypeVar, Generic

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.__content = content

    def get_content(self) -> T:
        return self.__content


# Creating instances of Box with different types
int_box = Box(42)
str_box = Box("hello")

# Accessing the content
print(int_box.get_content())  # Output: 42
print(str_box.get_content())  # Output: hello
