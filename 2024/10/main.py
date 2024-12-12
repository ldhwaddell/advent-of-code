import fileinput

grid = []
for line in fileinput.input():
    row = list(map(int, [n for n in line.strip()]))
    grid.append(row)


rows, cols = len(grid), len(grid[0])


def search(r, c, target, nines):
    # If target is 10, we are currently on a 9. Add it and return from fn.
    if target == 10:
        nines.add((r, c))
        return

    # Check up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target:
            # Continue search from here
            search(nr, nc, target + 1, nines)


part_1 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            # Create a set to keep track of the nines for this 0
            nine_set = set()

            # Search for all 9's reachable from this 0
            # Search
            search(r, c, 1, nine_set)

            # Add the # of results to part_1
            part_1 += len(nine_set)


print(f"Part 1: {part_1}")

seen = {}


def count_paths(r, c, target):
    # Successfuly found path, increment
    if target == 10:
        return 1

    # Check how many existing paths we have to a location
    if (r, c, target) in seen:
        return seen[(r, c, target)]

    # Counter for total # of paths starting at current location
    paths = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target:
            # Increment by # of paths to the next target...
            paths += count_paths(nr, nc, target + 1)

    # Update the number of paths to the current position
    seen[(r, c, target)] = paths

    return paths


part_2 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            # Add the # of results to part_1
            part_2 += count_paths(r, c, 1)


print(f"Part 2: {part_2}")
