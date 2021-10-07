"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730345086"


def test_only_evens_full() -> None:
    x: list[int] = [3, 6, 9, 12, 44]
    assert only_evens(x) == [6, 12, 44]


def test_sub_void() -> None:
    a: list[int] = []
    b: int = 0
    c: int = 0
    assert sub(a, b, c) == []


def test_concat_connect_lists() -> None:
    one: list[int] = [11, 10, 3, 25]
    two: list[int] = [2, 8, 10, 19]
    assert concat(one, two) == [11, 10, 3, 25, 2, 8, 10, 19]