# UNSOLVED
from typing import List


def longest_palindrome(base_string: str) -> str:
    def helper(string: str) -> str:
        if string == string[::-1]:
            return string
        else:
            return helper(string[:-1])

    def all_substrings(s: str) -> List[str]:
        n = len(s)
        return [s[i:j] for i in range(n) for j in range(i + 1, n + 1)]

    r1 = helper(base_string)
    r2 = helper(base_string[::-1])

    print(r1, r2)

    return r1 if (len(r1) >= len(r2)) else r2


print(longest_palindrome("cbbd"))
