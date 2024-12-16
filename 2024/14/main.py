import re
from operator import mul
from functools import reduce
import fileinput

ROWS = 103
COLUMNS = 101
SECONDS = 100

dot_grid = [["." for _ in range(COLUMNS)] for _ in range(ROWS)]


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
for line in fileinput.input():
    i_col, i_row, v_col, v_row = map(int, re.findall(r"-?\d+", line))

    n_col = (i_col + (v_col * SECONDS)) % COLUMNS
    n_row = (i_row + (v_row * SECONDS)) % ROWS

    if dot_grid[n_row][n_col] == ".":
        dot_grid[n_row][n_col] = 1
    else:
        dot_grid[n_row][n_col] += 1

    quadrant = get_quadrant(n_row, n_col)

    if quadrant != -1:
        quadrant_counts[quadrant] += 1


print(quadrant_counts)
print(f"Part 1: {reduce(mul, quadrant_counts)}")
