import fileinput

corrupted_coords = []
for line in fileinput.input():
    cr, cc = map(int, line.split(","))
    corrupted_coords.append((cr, cc))

ROWS = 70
COLUMNS = 70


def bfs(num_coords, start, end):
    # Treat walls as seen
    # And only inspect first n
    seen = {*corrupted_coords[:num_coords]}

    # Keep track of the # of steps and current coords
    steps = [(0, (0, 0))]

    # Keeps track of each possible path, and the distance to that point
    # When we reach the end, the first set of coords to do so will be shortest path.
    for dist, (row, col) in steps:
        if (row, col) == end:
            return dist

        for n_row, n_col in [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]:
            if (
                n_row in range(ROWS + 1)
                and n_col in range(COLUMNS + 1)
                and (n_row, n_col) not in seen
            ):
                steps.append((dist + 1, (n_row, n_col)))
                seen.add((n_row, n_col))

    return None


part_1 = bfs(1024, (0, 0), (ROWS, COLUMNS))
print(f"Part 1: {part_1}")


# We know at least the first 1024 bytes mean it is still possible to find end...
num_bytes = 1024

while True:
    print(f"Checking first {num_bytes} bytes")
    path = bfs(num_bytes, (0, 0), (ROWS, COLUMNS))
    if not path:
        # Lists are 0-indexed!!
        breaking_coords = corrupted_coords[num_bytes - 1]
        print(f"Part 2: {breaking_coords}")
        break

    else:
        num_bytes += 1
