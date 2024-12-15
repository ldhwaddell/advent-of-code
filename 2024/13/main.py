import re
import fileinput

MAX_BUTTON_PRESSES = 100
TOKENS_PER_A_PRESS = 3
TOKENS_PER_B_PRESS = 1

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


part_1 = 0
for group in file:
    a, b, prize = group.split("\n")
    a_matches = re.search(button_pattern, a)
    b_matches = re.search(button_pattern, b)
    prize_matches = re.search(prize_pattern, prize)

    ax, ay = int(a_matches.group(1)), int(a_matches.group(2))
    bx, by = int(b_matches.group(1)), int(b_matches.group(2))
    px, py = int(prize_matches.group(1)), int(prize_matches.group(2))

    part_1 += solve(ax, ay, bx, by, px, py)

print(f"Part 1: {part_1}")
