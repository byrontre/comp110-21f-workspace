"""Demonstrate defining a module iported elsewhere."""

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Rasie x to the power of n."""
    return x ** n

# Idiom for making a module run as a program
# or having its global definitions imported elsewhere


if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helpers.py was imported: {__name__}")
