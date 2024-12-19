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
