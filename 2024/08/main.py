import fileinput
from collections import defaultdict
from itertools import combinations

grid = []
for line in fileinput.input():
    grid.append([c for c in line.strip()])


symbols = defaultdict(list)
rows, cols = len(grid), len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == ".":
            continue
        symbols[grid[row][col]].append((row, col))


def is_valid_point(row, col):
    return 0 <= row < rows and 0 <= col < cols


antinodes = set()
for symbol, coords in symbols.items():
    if len(coords) < 2:
        continue

    # Get all pairs of antennas with the same frequency
    for (ax, ay), (bx, by) in combinations(coords, 2):
        # Compute difference between antennas
        delta_row = bx - ax
        delta_col = by - ay

        # All combinations are attempted!

        # Antinode closer to A
        antinode1_row = ax - delta_row
        antinode1_col = ay - delta_col

        # Antinode closer to B
        antinode2_row = bx + delta_row
        antinode2_col = by + delta_col

        # Validate and add to the set
        if is_valid_point(antinode1_row, antinode1_col):
            antinodes.add((antinode1_row, antinode1_col))
        if is_valid_point(antinode2_row, antinode2_col):
            antinodes.add((antinode2_row, antinode2_col))

print(f"Part 1: {len(antinodes)}")
