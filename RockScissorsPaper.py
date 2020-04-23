#!/usr/bin/python3

import os  # to type 'clear' command in terminal
import sys  # to get the OS name and exit the game
from random import randint  # to generate random numbers for the computer game
from getpass import getpass  # to securely input numbers from console

# the choice of the right command to clear screen for certain OS
CL_SCREEN = 'clear'
if sys.platform.startswith('win'):
    CL_SCREEN = 'cls'


# in this function you can either just clear the screen or clear it with the prompt to press Enter
def clear(w=0):
    if w:
        input('Press Enter to continue...')
    os.system(CL_SCREEN)


# a class which describes a player
class User:
    def __init__(self, name='Anonymous', points_count=0, in_game=True):
        self.name = name  # your nickname
        self.points_count = points_count  # your current points count
        self.in_game = in_game  # are you gonna be in game

    def increment_points(self):  # a method to increment your current score by 1
        self.points_count += 1


# the main game function
def game(p1, p2, func1, func2):
    # a dict of possible combinations between rock, scissors and paper
    choices = {
        1: {
            1: None,
            2: p1,
            3: p2
        }, 2: {
            1: p2,
            2: None,
            3: p1
        }, 3: {
            1: p1,
            2: p2,
            3: None
        }
    }
    # the main game cycle
    while p1.in_game and p2.in_game:
        one = func1()  # a function which describes behaviour of the first player
        two = func2()  # analogical function for the second one
        if one == 4 or two == 4:  # if someone chose 4 the game ends
            p1.in_game = False
        elif choices[one][two]:
            choices[one][two].increment_points()  # the winner gets +1 point
        print(f'{p1.name}: {p1.points_count}')  # a leaderboard
        print(f'{p2.name}: {p2.points_count}')
        clear(1)  # delay not to clean too quickly
    if p1.points_count > p2.points_count:  # final messages
        print(f'{p1.name} has won! Glory to Resistance!')
    elif p1.points_count < p2.points_count:
        print(f'{p2.name} has won! Glory to SkyNet!')
    else:
        print('Friendship has won! Glory to everyone!')
    clear(1)
    main()  # return to main function


# this function chooses the right number value from the certain range and starts again if this value is wrong
def choose(prompt, low=1, high=4):
    num = getpass(prompt=prompt)  # not to see player's input, you can input it as a password
    try:  # check proper values
        if int(num) in range(low, high + 1):
            clear()
            return int(num)
        raise ValueError
    except ValueError:
        print('Use proper values!')
        clear(1)
        choose(prompt, low, high)


def main():
    # choose the correct number of what you want to do
    num = choose("""Welcome to the RockScissorsPaper game! Firstly, choose one of the options:
    1. Single player game.
    2. Multi player game (one device)
    3. Exit
    """, high=3)
    if num == 1:  # single player with a computer, who chooses random numbers
        p1 = User(name=input('Write your name:'))
        p2 = User(name='Computer')
        func1 = lambda: choose("""Choose one of the options:
    1. Rock
    2. Scissors
    3. Paper
    4. Exit to main menu\n""")
        func2 = lambda: randint(1, 3)
        game(p1, p2, func1, func2)
    elif num == 2:  # one device multiplayer with two humans
        p1 = User(name=input('Write player\'s 1 name:'))
        p2 = User(name=input('Write player\'s 2 name:'))
        func1 = lambda: choose(f"""It's player's {p1.name} turn. Choose one of the options:
            1. Rock
            2. Scissors
            3. Paper
            4. Exit to main menu\n""")
        func2 = lambda: choose(f"""It's player's {p2.name} turn. Choose one of the options:
            1. Rock
            2. Scissors
            3. Paper
            4. Exit to main menu\n""")
        clear()
        game(p1, p2, func1, func2)
    elif num == 3:  # exit the game
        input('Goodbye! I hope you enjoyed this game. Press Enter to exit...')
        sys.exit(0)


main()  # the program starts here
