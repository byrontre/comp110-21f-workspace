"""Choose Your Own Adventure."""

__author__ = "730345086"

from random import randint
points: int = 0
player = str
ROSE: str = '\U0001F339'
MOON: str = '\U0001F319'
TRUTH: str = '\U0001F338'
TRUTH_X: str = '\U0001F340'
FINAL: int = randint(1, 10)


def main() -> None:
    """Chapelwell Chronicles."""
    print(greet())
    global points
    print(f"Total Tokens: {points}")
    path: int = int(input(f"From here, {player}, your journey will begin with a shaman giving you a choice between three cards labeled 0, 1, and 2: "))
    while path != 0:
        print(f"Total Tokens: {points}")
        if path == 1:
            points = points + 5
            print(alp_wood())
            new_path: int = int(input("If you would like to test your fate on a different path, please choose between 0, 1, and 2 again: "))
            path = new_path
        else:
            if path == 2:
                points = points + 5
                points = un_palace(points)
                print(fin_valley())
                new_path: int = int(input("If you would like to test your fate on a different path, please choose between 0, 1, and 2 again: "))
                path = new_path
    if path == 0:
        while path == 0:
            print(the_end())
            new_path: int = int(input("If you would like to test your fate on a different path, please choose between 0, 1, and 2 again: "))
            path = new_path
    if path != (0, 2):
        print(f"Seeing as you are really determined to end your Game of Fates, let this final statement symbolize your potentially eternal departure. Chapelwell bids you farewell, {player}.")
        print(f"Total Tokens: {points}")


def greet() -> None:
    """Introduction."""
    print("The Lordes and Titans of Chapelwell welcome you and ask that you oblige us in the Game of Fates! As the game progresses, you will receive varying amounts of tokens based on the choices you make so choose wisely.")
    global player 
    player = input("How may we address you, traveler?: ")
    return 


def alp_wood() -> None:
    """The First Adventure."""
    global points
    print(f"{player}, you have been teleported to the Alpine Wood and encountered Jeff. He will gift you one of two emeralds that will lead you to your fate.")
    red = 3
    blue = 4
    emerald: int = int(input("Two cards labeled 3 and 4 magically levitate before you. Make your choice: "))
    if emerald == red:
        points = points + 7 
        print(f"Jeff hands you the {ROSE} emerald. As you stare into the stone, you begin to hear thunder right above you growing and growing until a bolt of lightning strikes you!")
        print(fin_valley())
        return
    else:
        if emerald == blue:
            points = points + 6
            print(f"Jeff hands you the {MOON} emerald. As you stare into the stone, it begins to shimmer brighter and brighter until a blinding white light consumes you!")
            print(fin_valley())
            return 


def un_palace(x: int) -> int:
    """The Second Adventure."""
    global points
    print(f"{player}, you have been teleported to the Union Palace and encountered Anti-Jeff. He will gift you one of two scrolls that will lead you to your fate.")
    hidden: int = x + FINAL
    guess: int = int(input("You must pick an integer between 6 and 15: "))
    if guess <= hidden:
        x = guess + points
        return x 
    else:
        x = hidden + points
        return x


def fin_valley() -> None:
    """The Final Adventure."""
    global points
    print(f"Well, {player}, not many are as fortunate and courageous as you have been in this Game of Fates. You have been summoned to the Final Valley, a mountain fortress overlooking the entirety of Chapelwell from the Great Carboroll Hills to the Very Cary Meadows. Your final task awaits you.")
    closer: int = int(input("Upon entering the fortress, you are immediately met with two parallel corridors. You must choose either 5 or 6: "))
    life: int = 5
    death: int = 6
    if closer == life: 
        points = points + 10
        print("Anti-Jeff has reppeared and transformed into a hideous warlock named Chelsea. You must battle him in order to escape.")
        chelsea: int = FINAL
        if chelsea == FINAL: 
            rate: int = int(input("In order to defeat Chelsea, you must answer this question; How would rate the show Friends on a scale of 1-10?: "))
            if rate != 10: 
                print("You must suffer the consequences of rating incorrectly! Your points have been reduced!")
                points = points - 3
                return 
            else:
                points = points + chelsea
                chelsea = chelsea - 10
                print(f"You have defeated the wicked Chelsea! Now take this {TRUTH}, and discover what your fate truly is.")
                print("After leaving the Final Valley, you stand at the peak of the mountain overlooking the land. Your Fate Flower begins to whisper, and you bring it to your ear. The flower says 'You must go and spread the Gospel of Jesus Christ to all peoples everywhere'.")
                print("With determination in your heart and a sack of stolen pixie dust, you fly away into the fading sunset following your true fate.")
                print(f"Goodbye, {player}.")
                return
    else: 
        if closer == death:
            points = points + 8
            print("At the end of the corridor, you encounter a adorably young child named Sarafina.")
            yes: int = 7
            no: int = 8
            love: int = int(input("Will you surrender your life for this child by choosing 7 or curse this child by choosing 8: "))
            if love == yes:
                print("Sarafina suddenly turns into Marilyn Manson, and starts yelling at you about beautiful people. Your points have been reduced.")
                points = points - 3
                return
            else:
                if love == no: 
                    points = points + 10
                    print("Sarafina is immediately consumed with flames, scorching the horrific monster that she truly is.")
                    print(f"You have defeated that horrid creature, Sarafina. Her breath was dreadful. Anyway, now that you have completed your final task, take this {TRUTH_X}, and see what fate lies beyond.")
                    print("After leaving the Final Valley, you come upon the River of Lenoir flowing from the top of the mountain. As the water rushes by, the Fate Clover begins to whisper. You hold the clover up to your ear as it says 'You must go and expose the truth behind the U.S. moon landing of 1969.")
                    print("With the white, hot passion of 1,000 suns and an expired Sheetz gift card, you set off down the river following your true fate.")


def the_end() -> None:
    """The Continuous Ending."""
    print("Unfortunately, your Game of Fates has come to an end. However, all of Chapelwell wishes you great prosperity and blessing. One day, perhaps, we'll meet again.")
    global points
    print(f"Total Tokens: {points}")


if __name__ == "__main__":
    main()
