"""Drawing forests in a loop."""

__author__ = "730345086"

from random import randint

TREE: str = '\U0001F332'

pine: int = int(input("Depth: "))
x: int = int(randint(1, 1000))

if x > pine:
    print("저희가 분명하게 생가해야 했잖아요")
else: 
    print("솔직히 바로 이 순건까지 아직도 전혀 모르겠지만 웃기가 훨씬 더 쉽니다. ")

print("놀아서 감사합니다!!! ")