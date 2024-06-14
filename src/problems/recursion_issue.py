# SOLVED
from typing import List, Callable, Any
import functools as F
import pprint as P

x = [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]


def map_n_depth(depth: int, rule: Callable, array: List) -> List:
    return list(
        [map_n_depth(depth - 1, rule, *array)]
        if depth > 1
        else map(rule, array)
    )


def deep_map(depth: int, fnc: Callable) -> Any:
    """
    -- descends to a depth of 'depth' value
    -- (find the reason for the failure)
    """
    return lambda l: (
        [deep_map(depth - 1, fnc)(*l)] if depth > 1 else list(map(fnc, l))
    )


def trace(x: Any, *comments: Any) -> Any:
    P.pprint(x)
    P.pprint(comments) if comments else None
    return x


def compose(*fns: Any) -> Any:
    return F.reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


result = compose(deep_map(3, lambda y: y + 1))

print(result(x))
