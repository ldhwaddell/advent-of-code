import fileinput

SYMBOLS = {}
PARTS = []


def parse_input():
    for y, line in enumerate(fileinput.input()):
        num = ""
        for x, c in enumerate(line):
            # If not a . or digit, its a symbol and we want to know (x, y)
            if not c.isdigit() and c != "." and c != "\n":
                SYMBOLS[(x, y)] = c

            # Now we need to add each num, with its value, start, end, y
            if c.isdigit():
                num += c
            # This runs on the first symbol that comes after a num
            elif num:
                PARTS.append((int(num), x - len(num), x - 1, y))
                num = ""


seen_parts = set()


def sum_adjacent():
    sum_1 = 0
    sum_2 = 0

    for x, y in SYMBOLS:
        adj = []
        print(x, y, SYMBOLS[(x, y)])
        for i, (part_num, start, end, yy) in enumerate(PARTS):
            # If the part y is symbol y - 1 OR symbol y + 1 -> means symbol y is within part y +- 1
            # AND part end is symbol x - 1 or part start is symbol x + 1 -> means symbol x is within start - 1 and end + 1
            if (yy - 1 <= y <= yy + 1) and (start - 1 <= x <= end + 1):
                part_num = int(part_num)
                adj.append(part_num)
                sum_1 += part_num

        if SYMBOLS[(x, y)] == "*" and len(adj) == 2:
            sum_2 += adj[0] * adj[1]

    print(f"Part 1: {sum_1}")
    print(f"Part 2: {sum_2}")


parse_input()
sum_adjacent()
