from functools import reduce


def reverse(string: str) -> str:
    return reduce(lambda acc, x: x + acc, string)


def sliced_reverse(string: str) -> str:
    return string[::-1]
