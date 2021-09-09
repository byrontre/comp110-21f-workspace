"""Counting Letters is as Easy as Chasing Pavements."""

__author__ = "730345086"

i: int = 0

alpha: str = input("What letter do you want to search for?: ")
phrase: str = input("Enter a word: ")
position = alpha

while i < len(phrase):
    amnt: int = len(alpha)
    line: str = phrase[amnt]
    print("Count: " + line)
    i = len(phrase)