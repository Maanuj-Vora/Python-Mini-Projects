import random


def get_guess():
    dashes = "-" * len(secret_word)
    guesses_left = 10

    while guesses_left > -1 and not dashes == secret_word:

        print(dashes)
        print(str(guesses_left))
        guess = input("Guess:")
        if len(guess) != 1:
            print("Your guess is too long")
        elif guess in secret_word:
            print("You got a letter correct!")
            dashes = update_dashes(secret_word, dashes, guess)
        else:
            print("Letter not in word")
            guesses_left -= 1
    if guesses_left < 0:
        print("You lose, the word was " + str(secret_word))
    else:
        print("Congrats for winning, the word was " + str(secret_word))


def update_dashes(secret, cur_dash, rec_guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess
        else:
            result = result + cur_dash[i]
    return result


words = ["one", "two", "three", "four", "five"]
secret_word = random.choice(words)
get_guess()