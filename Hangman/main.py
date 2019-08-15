import random


def get_guess():
    wordy = "-" * len(secret_word)
    turnLeft = 10

    while turnLeft > -1 and not wordy == secret_word:

        print(wordy)
        print(str(turnLeft))
        guess = input("Guess:")
        if len(guess) != 1:
            print("Your guess is too long")
        elif guess in secret_word:
            print("You got a letter correct!")
            wordy = update_dashes(secret_word, wordy, guess)
        else:
            print("Letter not in word")
            turnLeft -= 1
    if turnLeft < 0:
        print("You lose, the word was " + str(secret_word))
    else:
        print("Congrats for winning, the word was " + str(secret_word))


def update_dashes(word, dash, guess):
    printer = ""
    for i in range(len(word)):
        if word[i] == guess:
            printer = printer + guess
        else:
            printer = printer + dash[i]
    return printer


words = ["one", "two", "three", "four", "five"]
secret_word = random.choice(words)
get_guess()