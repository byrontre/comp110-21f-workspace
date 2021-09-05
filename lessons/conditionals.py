"""An example of conditional (if else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly! ")
    print("You're not a dumb slut. Congrats! ")
else:
    print("Sorry, you guessed incorrectly, you dumb hoe! ")
    if guess > SECRET: 
        print("Bring down your guess, saweetie. We said 1-5. ")
    else:
        print("Reach a little further, babe. Your guess was a bit too low. ")

print("GAME OVER!!! ")