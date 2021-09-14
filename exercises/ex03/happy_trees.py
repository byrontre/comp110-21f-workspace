"""The Answer is Forestry."""

__author__ = "730345086"

TREE: str = '\U0001F332'

pine: int = int(input("Depth: "))
i: int = 0
oak: int = i + 1 

if pine <= 0:
    print()
else: 
    while i < pine:
        print(TREE) 
        while oak < pine:
            oak = oak + 1
            print(TREE * oak)
        i = i + 1
            