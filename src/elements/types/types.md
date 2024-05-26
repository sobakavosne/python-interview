Python Type System

1. Dynamic Typing

```python
x = 10  # x is an integer
x = "hello"  # Now x is a string
```

2. Strong Typing

```python
x = "10"
y = x + 5  # This will raise a TypeError because you can't add an integer to a string
```

3. Type Annotations

```python
age: int = 25
```

4. In-Built Types

```text
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Text Type:      str
Binary Types:   bytes, bytearray, memoryview
Set Types:      set, frozenset
Mapping Type:   dict
Boolean Type:   bool
None Type:      NoneType
```

5. Custom Types

```python
class MyType:
    def __init__(self, value):
        self.value = value
```

6. Type Checking

7. Type Hints and typing Module

```text
• List, Dict, Set, Tuple:
• Optional (None or value)
• Union (different values)
• Any
• NewType
• TypeAlias
```

8. Static Type Checking with Mypy

9. Generic Types

10. Protocols (Structural Subtyping)
