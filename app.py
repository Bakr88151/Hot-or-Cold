from colorama import Fore, Style, Back
import sys
import random

def main():
    guess = -1
    tries = 1
    goal = random.randint(0, get_level())
    # print(f'Goal: {goal}')
    while True:
        new = close(goal, guess, tries)
        if new == True:
            sys.exit(0)
        elif new[2] < 11:
            guess = new[1]
            tries = new[2]
        else: 
            print(Back.RED + "You lost :(" + Style.RESET_ALL)
            sys.exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print(Fore.RED + "Level must be greater than 9" + Style.RESET_ALL)
        else:
            if level > 9:
                break
            else:
                print(Fore.RED + "Level must be greater than 9" + Style.RESET_ALL)
                pass
    return level


def close(goal, previous, tries):
    while True:
        try:
            guess = int(input("guess: "))
        except ValueError:
            print(Fore.RED + "your Guess must be a positive number" + Style.RESET_ALL)
        else:
            if guess > 0:
                break
            else:
                print(Fore.RED + "your Guess must be a positive number" + Style.RESET_ALL)
                pass
    
    if guess != -1:
        if guess == goal:
            print(Fore.GREEN + "You won!!!" + Style.RESET_ALL)
            return(True)
        elif abs(goal - previous) > abs(goal - guess):
            print(Fore.GREEN + "HOT!!!" + Style.RESET_ALL)
            print(f'Remaining tries: {10 - tries}')
            return(False, guess, tries + 1)
        else :
            print(Fore.BLUE + "COLD" + Style.RESET_ALL)
            print(f'Remaining tries: {10 - tries}')
            return(False, guess, tries + 1)
    else:
            print(Fore.GREEN + "HOT!!!" + Style.RESET_ALL)
            print(f'Remaining tries: {10 - tries}')
            return(False, guess, tries + 1)


if __name__ == '__main__':
    main()
