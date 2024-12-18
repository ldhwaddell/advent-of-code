import sys

# Shoutout HyperNeutrino https://www.youtube.com/watch?v=aCqtVmSSkUs


top, bottom = open(sys.argv[1]).read().split("\n\n")


grid = [list(l) for l in top.split("\n")]
moves = bottom.replace("\n", "")

rows, cols = len(grid), len(grid[0])


def find_start(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                return (r, c)


r, c = find_start(grid, rows, cols)


directions = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}

for move in moves:
    dr, dc = directions[move]

    curr_row, curr_col = r, c

    can_advance = True

    # Assume we will be advancing from current position
    to_be_advanced = []

    while True:
        curr_row, curr_col = curr_row + dr, curr_col + dc

        # If the curr position is a wall, break out
        if grid[curr_row][curr_col] == "#":
            can_advance = False
            break

        # Means we have a box to advance
        if grid[curr_row][curr_col] == "O":
            to_be_advanced.append((curr_row, curr_col))

        # Means we found an empty spot to advance everything into.
        if grid[curr_row][curr_col] == ".":
            break

    # This means we have hit a wall. Nothing can be advanced from here, so wait for next move.
    if not can_advance:
        continue

    # Advance our @
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"

    # Advance all the boxes by one in the curr direction
    for ar, ac in to_be_advanced:
        grid[ar + dr][ac + dc] = "O"

    # increase the coords of @ for next iteration
    r, c = r + dr, c + dc

part_1 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "O":
            part_1 += 100 * r + c

print(f"Part 1: {part_1}")


# Expand the grid.
grid = [
    list(l.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
    for l in top.split("\n")
]

rows, cols = len(grid), len(grid[0])
r, c = find_start(grid, rows, cols)

directions = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}


for move in moves:
    dr, dc = directions[move]

    to_be_advanced = [(r, c)]

    can_advance = True

    for curr_r, curr_c in to_be_advanced:
        next_r, next_c = curr_r + dr, curr_c + dc

        # If we have already seen the current char, continue
        if (next_r, next_c) in to_be_advanced:
            continue

        # If we reached a wall, we can't advance so break
        if grid[next_r][next_c] == "#":
            can_advance = False
            break

        if grid[next_r][next_c] == "[":
            to_be_advanced.append((next_r, next_c))
            # Also append the ']'
            to_be_advanced.append((next_r, next_c + 1))

        if grid[next_r][next_c] == "]":
            to_be_advanced.append((next_r, next_c))
            # Also append the '['
            to_be_advanced.append((next_r, next_c - 1))

    # This means we have hit a wall. Nothing can be advanced from here, so wait for next move.
    if not can_advance:
        continue

    copy = [list(r) for r in grid]

    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"

    for br, bc in to_be_advanced[1:]:
        grid[br][bc] = "."
    for br, bc in to_be_advanced[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]

    # increase the coords of @ for next iteration
    r, c = r + dr, c + dc

part_2 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "[":
            part_2 += 100 * r + c

print(f"Part 2: {part_2}")
