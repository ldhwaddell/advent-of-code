import re

import fileinput

MAX_BUTTON_PRESSES = 100
TOKENS_PER_A_PRESS = 3
TOKENS_PER_B_PRESS = 1
PART_2_INCREASE = 10000000000000

file = "".join([line for line in fileinput.input()])
file = file.strip().split("\n\n")


button_pattern = r"X\+(-?\d+),\s*Y\+(-?\d+)"
prize_pattern = r"X\=(-?\d+),\s*Y\=(-?\d+)"


def solve(ax, ay, bx, by, px, py):
    # a = # times button a is pressed.
    # b = # times button b is pressed.

    for a in range(MAX_BUTTON_PRESSES):
        for b in range(MAX_BUTTON_PRESSES):
            if (ax * a) + (bx * b) == px and (ay * a) + (by * b) == py:
                token_cost = (a * TOKENS_PER_A_PRESS) + (b * TOKENS_PER_B_PRESS)
                return token_cost

    return 0


# Instead look to see if the equations of the 2 lines meet at some point.
def fast_solve(ax, ay, bx, by, px, py):
    # Formula to find intersection of 2 lines:
    ca = ((bx * (-py)) - (by * (-px))) / ((ax * by) - (ay * bx))
    cb = ((ay * (-px)) - (ax * (-py))) / ((ax * by) - (ay * bx))

    return ca, cb


part_1 = 0
part_2 = 0
for group in file:
    a, b, prize = group.split("\n")
    a_matches = re.search(button_pattern, a)
    b_matches = re.search(button_pattern, b)
    prize_matches = re.search(prize_pattern, prize)

    ax, ay = int(a_matches.group(1)), int(a_matches.group(2))
    bx, by = int(b_matches.group(1)), int(b_matches.group(2))
    px, py = int(prize_matches.group(1)), int(prize_matches.group(2))

    ca, cb = fast_solve(ax, ay, bx, by, px, py)
    if ca.is_integer() and cb.is_integer() and ca <= 100 and cb <= 100:
        part_1 += int(ca * TOKENS_PER_A_PRESS + cb * TOKENS_PER_B_PRESS)

    ca2, cb2 = fast_solve(ax, ay, bx, by, px + PART_2_INCREASE, py + PART_2_INCREASE)
    if ca2.is_integer() and cb2.is_integer():
        part_2 += int(ca2 * TOKENS_PER_A_PRESS + cb2 * TOKENS_PER_B_PRESS)


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
