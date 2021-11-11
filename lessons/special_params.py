"""Example of optional parameters and Union types."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A Delightful Greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP110" + str(name)
    else:
        greeting = "Alien Life from Sector " + str(name)

    return greeting


# Str Arg.
print(hello("Sally"))

# No Arg.
print(hello())

# Int Arg.
print(hello(110))

print(hello(3.14))