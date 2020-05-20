import sys
import re

from random import randint


DICE_MATCHING_EXPRESSION = r"^([1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9])d(2|3|4|6|8|10|12|20|100)$"


def dice_result(arg):
    throws, dice_faces = arg.split("d")

    for _ in range(int(throws)):
        print(randint(1, int(dice_faces)))


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("diceroller.py [NdX]")
        print("Parameter NdX at least one time.")
        print("N means the amount of dices and X means how many sides each dice has")
        print("Example:")
        print("diceroller.py 2d6 1d4")
        print("means two dices of 6 sides and one dice of 4 sides")

    for arg in args:
        if not re.match(DICE_MATCHING_EXPRESSION, arg):
            print("Invalid argument: " + arg)
            exit()

    for arg in args:
        print(arg + ":")
        dice_result(arg)
        print()
