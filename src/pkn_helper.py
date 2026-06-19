import random
import time as t

def wait(n : int = 1):
    t.sleep(n)


def roll(roll_list : list):
    x = 0
    y = len(roll_list) - 1
    roll_list = roll_list[random.randint(x, y)]
    return roll_list


def set_pkn_list():
    n = ["rock", "paper", "scissors"]
    return n


def print_loading_dots(n : int = 50):
    for dot in range(n):
        wait(.05)
        print(".", end="", flush=True)
    print("")


def startgame_loading():
    print("")
    wait()
    spell("ROCK PAPER SCISSORS")
    print("")
    wait()
    spell("LOADING THE GAME")
    wait()
    print_loading_dots()
    wait()
    print("")
    spell("The game started, good luck!\n")
    wait()


def spell(print_to_spell : str, value_to_spell = ""):

    for letter in print_to_spell:
        print(letter, end="", flush=True)
        wait(.05)

    value_to_spell = str(value_to_spell)
    for e_from_value in value_to_spell:
        print(e_from_value, end="", flush=True)
        wait(.05)