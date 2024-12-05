import fileinput
from typing import List


def find_xmas(slice: List[str]) -> int:
    if slice == ["X", "M", "A", "S"] or slice == ["S", "A", "M", "X"]:
        return 1
    return 0


grid = []
for line in fileinput.input():
    grid.append(list(line.strip()))

rows, cols = len(grid), len(grid[0])
count_1 = 0
for y in range(rows):
    for x in range(cols):
        if x < cols - 3:
            count_1 += find_xmas(grid[y][x : x + 4])

        if y < rows - 3:
            col_slice = [grid[y][x], grid[y + 1][x], grid[y + 2][x], grid[y + 3][x]]
            count_1 += find_xmas(col_slice)

        if x < cols - 3 and y < rows - 3:
            diag_slice = [
                grid[y][x],
                grid[y + 1][x + 1],
                grid[y + 2][x + 2],
                grid[y + 3][x + 3],
            ]
            count_1 += find_xmas(diag_slice)

        if x > 2 and y > 2:
            diag_slice = [
                grid[y][x],
                grid[y - 1][x - 1],
                grid[y - 2][x - 2],
                grid[y - 3][x - 3],
            ]
            count_1 += find_xmas(diag_slice)

    print("\n\n")

print(f"Part 1: {count_1}")


def is_mas(slice: List[str]) -> bool:
    return slice == ["M", "A", "S"] or slice == ["S", "A", "M"]


rows, cols = len(grid), len(grid[0])
count_2 = 0
for y in range(rows - 2):
    for x in range(cols - 2):
        top = grid[y][x : x + 3]
        mid = grid[y + 1][x : x + 3]
        bottom = grid[y + 2][x : x + 3]
        left_diag = [grid[y][x], grid[y + 1][x + 1], grid[y + 2][x + 2]]
        right_diag = [grid[y][x + 2], grid[y + 1][x + 1], grid[y + 2][x]]

        if is_mas(left_diag) and is_mas(right_diag):
            count_2 += 1

print(f"Part 2: {count_2}")
