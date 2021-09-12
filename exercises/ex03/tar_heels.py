"""Tar Heels Win Regardless."""

__author__ = "730345086"


puzzle: int = int(input("Enter an int: "))

if puzzle % 2 == puzzle % 7 == 0:
    print("TAR HEELS")
else:
    if puzzle % 2 == 0:
        print("TAR")
    else:
        if puzzle % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")