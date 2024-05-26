from typing import NewType

# Define a new type
UserId = NewType("UserId", int)


def get_user_name(user_id: UserId) -> str:
    return f"User{user_id}"


# Example usage
user_id = UserId(42)

print(get_user_name(user_id))  # Output: User42
