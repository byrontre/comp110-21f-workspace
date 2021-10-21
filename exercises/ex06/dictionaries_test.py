"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_colors, count

__author__ = "730345086"


def test_invert_bland() -> None:
    """Edge Case with No Values."""
    trace: dict[str, str] = {}
    assert invert(trace) == {}


def test_invert_small_set() -> None:
    """Use Case with Minimal Key & Values."""
    trace: dict[str, str] = {"a": "tuna", "b": "salmon"}
    assert invert(trace) == {"tuna": "a", "salmon": "b"}


def test_invert_completion() -> None:
    """Use Case with Many Keys & Values."""
    trace: dict[str, str] = {"c": "bunny", "d": "turtle", "e": "squid", "f": "mouse", "g": "owl"}
    assert invert(trace) == {"bunny": "c", "turtle": "d", "squid": "e", "mouse": "f", "owl": "g"}


def test_favorite_colors_busted() -> None:
    """Edge Case with No Dict."""
    red: dict[str, str] = {}
    assert favorite_colors(red) == ""
    

def test_favorite_colors_simple() -> None:
    """Use Case with Basic Dict."""
    red: dict[str, str] = {"sugar": "red", "milk": "blue", "butter": "red"}
    assert favorite_colors(red) == "red"


def test_favorite_colors_valhalla() -> None:
    """Use Case with Full Dict."""
    red: dict[str, str] = {"earth": "yellow", "wind": "pink", "fire": "green", "water": "pink", "lightning": "yellow"}
    assert favorite_colors(red) == "yellow"


def test_count_lukewarm() -> None:
    """Edge Case with No List."""
    value: list[str] = []
    assert count(value) == {}


    """Use Case with Minor List."""
    value: list[str] = ["tea", "tea", "egg", "bacon"]
    assert count(value) == {"tea": 2, "egg": 1, "bacon": 1}


def test_count_fuego() -> None:
    """Use Case with Full List."""
    value: list[str] = ["chile", "jalapeno", "ghost", "bell", "jalapeno", "pimento", "jalapeno", "bell"]
    assert count(value) == {"chile": 1, "jalapeno": 3, "ghost": 1, "bell": 2, "pimento": 1}