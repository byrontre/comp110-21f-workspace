"""Where Them Doubles At."""

__author__ = "730345086"


select: str = input("Enter a word: ")
tag: bool = False
i: int = 0

while i < len(select):
    current_letter: str = select[i] 
    k: int = i + 1
    while k < len(select):
        next_letter: str = select[k] 
        if current_letter == next_letter:
            tag = True 
        k = k + 1
    i = i + 1
if tag is True:
    print("Found duplicate: True ")
else:
    print("Found duplicate False ")