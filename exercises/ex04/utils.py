"""List utility functions."""

__author__ = "730345086"


def all(x: list[int], y: int) -> bool:
    """Match the Index."""
    answer: bool = False
    i: int = 0
    if len(x) == 0:
        return answer
    else:
        while i < len(x):
            check: int = x[i]
            if check == y:
                answer = True
            else:
                if check != y:
                    return False 
            i += 1
    if answer is True:
        return True
    else:
        return answer


def is_equal(a: list[int], b: list[int]) -> bool:
    """Deep Equality."""
    i: int = 0
    fact: bool = True
    if len(a) != len(b):
        return False
    while i < len(a):
        while i < len(b):
            first: int = a[i]
            second: int = b[i]
            if first != second:
                return False
                i += 1
            else:
                return fact
    return fact


def max(v: list[int]) -> int:
    """Find Largest Value."""
    i: int = 0
    big_lebowski: int
    if len(v) == 0:
        raise ValueError("max() arg is an empty List")
    if len(v) > i:
        big_lebowski = v[i]
        j: int = i + 1
        while j < len(v):
            next_value: int = v[j]
            if next_value > big_lebowski:
                big_lebowski = next_value
            j += 1
    return big_lebowski