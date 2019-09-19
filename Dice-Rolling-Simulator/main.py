from random import randint


def playAgain():
    if input("Do you want to play again? (yes or no)\n") == "yes":
        dice()


def dice():
    number = randint(1, 6)

    print("You rolled a " + str(number))
    playAgain()


dice()
