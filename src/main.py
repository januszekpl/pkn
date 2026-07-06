from pkn import pkn
from pkn_helper import *


def main():
    # set required variables
    pkn_list = set_pkn_list()
    intro()

    # start game
    pkn(pkn_list)

    print("Game finished!")


if __name__ == "__main__":
    main()