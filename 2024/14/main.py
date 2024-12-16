import re
from operator import mul
from functools import reduce
from copy import deepcopy
import fileinput

ROWS = 103
COLUMNS = 101
SECONDS = 100

dot_grid = [["." for _ in range(COLUMNS)] for _ in range(ROWS)]


data = [list(map(int, re.findall(r"-?\d+", line))) for line in fileinput.input()]


def get_quadrant(row, col):
    # Skip the middle row and column
    middle_row = ROWS // 2
    middle_col = COLUMNS // 2
    if row == middle_row or col == middle_col:
        return -1

    if 0 <= row < middle_row and middle_col <= col < COLUMNS:
        return 0
    elif 0 <= row < middle_row and 0 <= col < middle_col:
        return 1
    elif middle_row < row < ROWS and 0 <= col < middle_col:
        return 2
    elif middle_row < row < ROWS and middle_col <= col < COLUMNS:
        return 3
    else:
        return -1


quadrant_counts = [0, 0, 0, 0]
for i_col, i_row, v_col, v_row in data:
    n_col = (i_col + (v_col * SECONDS)) % COLUMNS
    n_row = (i_row + (v_row * SECONDS)) % ROWS

    quadrant = get_quadrant(n_row, n_col)

    if quadrant != -1:
        quadrant_counts[quadrant] += 1


print(quadrant_counts)
print(f"Part 1: {reduce(mul, quadrant_counts)}")


min_sf = float("inf")
best_iter = 0


# Kind of a cheat.
# Assume the tree is in one quadrant.
# Then the overall safety factor would be low, because one quadrant will have a high # of robots
# But the others will have relatively few.
# So we just look for when the safety factor is lowest, based on the assumption that
# This will show us when the robots are most clutered, and probably in a tree.....
for i in range(10000):
    quadrant_counts = [0, 0, 0, 0]
    for i_col, i_row, v_col, v_row in data:
        n_col = (i_col + (v_col * i)) % COLUMNS
        n_row = (i_row + (v_row * i)) % ROWS

        quadrant = get_quadrant(n_row, n_col)

        if quadrant != -1:
            quadrant_counts[quadrant] += 1

    sf = reduce(mul, quadrant_counts)

    if sf < min_sf:
        min_sf = sf
        best_iter = i


print(f"Part 2: {best_iter}")
