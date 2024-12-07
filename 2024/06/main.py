import fileinput

# Build grid
grid = []
for line in fileinput.input():
    grid.append(list(line.strip()))

# Find grid dimensions
rows, cols = len(grid) - 1, len(grid[0]) - 1


def find_start():
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "^":
                return col, row


curr_direction = "N"

# Find the starting position
col, row = find_start()
# set((col, row)) Tries to iterate over the tuple and create a set out of it.
seen = {(col, row)}


def advance(col, row, curr_direction):
    match curr_direction:
        case "N":
            return col, row - 1
        case "S":
            return col, row + 1
        case "E":
            return col + 1, row
        case "W":
            return col - 1, row
        case _:
            raise Exception("BAD")


def rotate(curr_direction):
    match curr_direction:
        case "N":
            return "E"
        case "E":
            return "S"
        case "S":
            return "W"
        case "W":
            return "N"
        case _:
            raise Exception("BAD")


print(f"cols: {cols}, rows: {rows}")

while True:
    # If we can advance, advance, and add current position to seen
    ncol, nrow = advance(col, row, curr_direction)
    if ncol < 0 or ncol > cols or nrow < 0 or nrow > rows:
        # We have reached edge
        break

    # Haven't reached edge. Check position
    if grid[nrow][ncol] == "#":
        curr_direction = rotate(curr_direction)
    else:
        seen.add((ncol, nrow))
        col, row = ncol, nrow

print(f"Part 1: {len(seen)}")
