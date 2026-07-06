import random
import time as t
import subprocess

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


def intro():
    subprocess.run("cls", shell=True)
    wait(.5)
    spell("ROCK PAPER SCISSORS")


def spell(print_to_spell : str, value_to_spell = "", is_end=True):

    for letter in print_to_spell:
        print(letter, end="", flush=True)
        wait(.05)

    value_to_spell = str(value_to_spell)
    for e_from_value in value_to_spell:
        print(e_from_value, end="", flush=True)
        wait(.05)
    
    if is_end:
        print("")


def pkn_scenarios():
    return {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper"
    }


def loading(seconds=2):
    spinner = "/-\\|"

    end_time = t.time() + seconds
    i = 0

    while t.time() < end_time:
        print(f"\r{spinner[i % len(spinner)]}", end="", flush=True)
        t.sleep(0.1)
        i += 1