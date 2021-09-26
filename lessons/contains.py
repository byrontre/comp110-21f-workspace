"""Examples of writing a function to process a list."""


def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Jimin", "Suga"]
    print(contains("Jimin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True iff needle is in haystack, return False otherwise."""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    
    return False

    if __name__ == "__main__":
        main()
