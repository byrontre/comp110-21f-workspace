"""What a Fortunate Cookie."""

__author__ = "730345086"

from random import randint 
FORTUNE: int = int(randint(15, 40))

print("Your fortune cookie says . . . ")
fate: int = int(randint(15, 40)) 

if fate == FORTUNE:
    print("You won't be infected with the T-Virus! ")
else:
    if fate < FORTUNE < 25: 
        print("You will defeat Lady Dimitrescu and escape the castle! ")
    else:
        if fate > FORTUNE > 25:
            print("You will save your beloved Rose from Mother Miranda! ")
        else:
            print("You will survive the Raccoon City Outbreak! ")

print("Now, go spread positive vibes! ") 