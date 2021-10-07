"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730345086"


def test_only_evens_abyss() -> None:
    """Edge with No Integers."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_minor() -> None:
    """Use Case Two Integers."""
    x: list[int] = [4, 7]
    assert only_evens(x) == [4]


def test_only_evens_full() -> None:
    """Use Case with Many Integers."""
    x: list[int] = [3, 6, 9, 12, 44]
    assert only_evens(x) == [6, 12, 44]


def test_sub_void() -> None:
    """Edge Case with No a-list."""
    a: list[int] = []
    b: int = 0
    c: int = 0
    assert sub(a, b, c) == []


def test_sub_halfway() -> None:
    """Use Case with 'a and b'."""
    a: list[int] = [3, 4, 6, 7]
    b: int = -1
    c: int = 0
    assert sub(a, b, c) == []


def test_sub_complete() -> None:
    """Use Case with 'a, b, and c'."""
    a: list[int] = [15, 16, 17, 18, 19]
    b: int = 1
    c: int = 5
    assert sub(a, b, c) == [16, 17, 18, 19]


def test_concat_no_nums() -> None:
    """Edge Case with Two Blank Lists."""
    one: list[int] = []
    two: list[int] = []
    assert concat(one, two) == []


def test_concat_one_whole() -> None:
    """Use Case with One Full List."""
    one: list[int] = [62, 32, 18, 20]
    two: list[int] = []
    assert concat(one, two) == [62, 32, 18, 20]


def test_concat_connect_lists() -> None:
    """Use Case with Double Lists."""
    one: list[int] = [11, 10, 3, 25]
    two: list[int] = [2, 8, 10, 19]
    assert concat(one, two) == [11, 10, 3, 25, 2, 8, 10, 19]