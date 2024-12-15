import fileinput

grid = []
for line in fileinput.input():
    line = [c for c in line.strip()]
    grid.append(line)

rows, cols = len(grid), len(grid[0])


def find_region(r, c):
    curr_plant = grid[r][c]
    perimeter = 0

    # Cells in current region
    region = set()

    # Queue of cells to check
    queue = [(r, c)]

    # Above, Below, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.pop()

        # If current already seen, skip
        if (r, c) in region:
            continue

        # If current is invalid in any way, skip, increase perimeter.
        if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] != curr_plant:
            # At this point we know we arent connected, so there must be an edge, and therefore perimeter increase
            perimeter += 1
            continue

        # At this point, current cell should be in region.
        region.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (nr, nc) not in region:
                queue.append((nr, nc))

    # len region is the area
    return region, perimeter


part_1 = 0
visited = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            # Search for the region starting from (r, c)
            region, perimeter = find_region(r, c)
            part_1 += len(region) * perimeter
            visited.update(region)

print(f"Part 1: {part_1}")


# Ripped from HyperNeutrino
# https://www.youtube.com/watch?v=KXwKGWSQvS0
def find_sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [
            (r - 0.5, c - 0.5),
            (r + 0.5, c - 0.5),
            (r + 0.5, c + 0.5),
            (r - 0.5, c + 0.5),
        ]:
            corner_candidates.add((cr, cc))
    corners = 0
    for cr, cc in corner_candidates:
        config = [
            (sr, sc) in region
            for sr, sc in [
                (cr - 0.5, cc - 0.5),
                (cr + 0.5, cc - 0.5),
                (cr + 0.5, cc + 0.5),
                (cr - 0.5, cc + 0.5),
            ]
        ]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [
                False,
                True,
                False,
                True,
            ]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


part_2 = 0
visited = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            # Search for the region starting from (r, c)
            region, perimeter = find_region(r, c)
            sides = find_sides(region)
            part_2 += sides * len(region)
            visited.update(region)

print(f"Part 2: {part_2}")
