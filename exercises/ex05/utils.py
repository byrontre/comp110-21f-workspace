"""List utility functions part 2."""

__author__ = "730345086"


def only_evens(x: list[int]) -> list[int]:
    """Find the Even Ints."""
    i: int = 0
    while i < len(x):
        read: int = x[i]
        if read % 2 > 0:
            x.pop(i)
        i += 1
    return x


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Let's Make a List."""
    i: int = 0
    sub_set: list[int] = []
    if len(a) == 0 or b >= len(a) or c <= 0:
        return sub_set
    while i < len(a):
        if i >= b and i <= c - 1: 
            sub_set.append(a[i])
        i += 1
    return sub_set


def concat(one: list[int], two: list[int]) -> list[int]:
    """Put It All Together."""
    all_in: list[int] = []
    for i in one:
        all_in.append(i)
    for i in two:
        all_in.append(i)
    return all_in