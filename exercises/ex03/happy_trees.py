"""Drawing forests in a loop."""

__author__ = "730345086"

TREE: str = '\U0001F332'

pine: int = int(input("Depth: "))
i: int = 0 

if pine <= 0:
    print()
else: 
    while i < pine:
        print(TREE)
        oak: int = i + 1  
        while oak < pine:
            print(TREE * oak)
            oak = oak + 1
        i = i + 1