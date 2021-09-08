"""Wash, Rinse and, Repeat."""

__author__ = "730345086%"

rhythm: int = 0

funky: str = (input("What beat do you want to repeat? ")) 
groove: int = int(input("How many times do you want to repeat it? "))
filler: str = " " + funky 

if groove <= 0:
    print("No beat...")
else:
    while rhythm < groove - 1:
        funky = funky + filler 
        rhythm = rhythm + 1 
    print(funky)
    