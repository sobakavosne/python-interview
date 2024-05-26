from typing import TypeAlias, List, Tuple

# Define a custom type alias
Vector: TypeAlias = List[Tuple[float, float, float]]


def scale_vector(vector: Vector, scalar: float) -> Vector:
    """
    return [tuple(point * scalar for point in x) for x in vector]
    > Expression of type "list[tuple[float, ...]]" is incompatible
    > with return type "Vector"

    The type checker interprets this as a tuple of an indeterminate
    number of elements (hence tuple[float, ...]), since generator
    expressions are not restricted to a specific length.
    """
    return [
        (point[0] * scalar, point[1] * scalar, point[2] * scalar) for point in vector
    ]


# Example usage
vector: Vector = [(1.0, 2.0, 3.0)]
scaled_vector = scale_vector(vector, 2.0)

print(scaled_vector)  # Output: [(2.0, 4.0, 6.0)]
