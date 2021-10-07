"""This is the Testing Arena for Things to See How They Run."""


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Let's Make a List."""
    sub_set: list[int] = []
    if len(a) == 0 or b >= len(a) or c <= 0:
        return sub_set
    for indices in a:
        if b < len(a) or c > len(a):
            if indices > b and indices <= c - 1:
                sub_set.append(indices)
    return sub_set