import random
import time

def wait(n : int):
    time.sleep(n)


def roll(roll_list : list):
    x = 0
    y = len(roll_list) - 1
    rollo = roll_list[random.randint(x, y)]
    return rollo