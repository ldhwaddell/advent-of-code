import fileinput

grid = []
for line in fileinput.input():
    line = [c for c in line.strip()]
    grid.append(line)

rows, cols = len(grid), len(grid[0])


def search(r, c):
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
    return region, len(region) * perimeter


part_1 = 0
visited = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            # Search for the region starting from (r, c)
            region, price = search(r, c)
            print(price)
            print("\n")
            part_1 += price
            visited.update(region)

print(f"Part 1: {part_1}")
