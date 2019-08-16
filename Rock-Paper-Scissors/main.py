from random import randint


def rock():
    p1 = int(input("OK. You are going to be player 1 and the computer will be player 2. "
                   "\nYou will select your choice and the computer will randomly select one. "
                   "\nThen, we will see who wins. "
                   "\n\nChoose one from the following: rock (0), paper (1), scissors (2)."))
    p2 = randint(0,2)
    outcome = ['Rock', 'Paper', 'Scissors']
    print ('Player 1 has chosen ' + outcome[p1])
    print ('Player 2 has chosen ' + outcome[p2])
    if p1 == p2:
        print('It is a draw!')
    elif (p2+1) % 3 == p1:
        print('Player One Wins!')
    else:
        print('Player Two Wins!')
    playagain()


def playagain():
    if input('Do you want to play again? (yes or no)') == 'yes':
        rock()


rock()