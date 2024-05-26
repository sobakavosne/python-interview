class Callable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define callable instance behaviour
    def __call__(self, z):
        """
        Call signature:
        __call__(z: int) -> int
        """
        return self.x + self.y + z


# Create an instance of Callable
callable_instance = Callable(1, 2)

# Call the instance as if it were a function
result = callable_instance(3)

print(result)  # Output: 6
