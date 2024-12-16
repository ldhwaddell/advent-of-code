import fileinput


for line in fileinput.input():
    nums = list(map(int, [n for n in line.strip()]))
    break

# Generate dot map.
disk = []
curr_id = 0


for i, n in enumerate(nums):
    if i % 2 == 0:
        disk.extend([curr_id] * n)
        curr_id += 1
    else:
        disk.extend(["."] * n)


# Iterate over the index of each blank space, swap with right most number.

space = [i for i, n in enumerate(disk) if disk[i] == "."]

for spot in space:
    # If right most spot is period, remove it
    while disk[-1] == ".":
        disk.pop()

    # If we have used up all our disk:
    if spot >= len(disk):
        break
    # Otherwise, swap current blank with end most
    disk[spot] = disk.pop()

part_1 = sum([n * i for n, i in enumerate(disk)])
print(f"Part 1: {part_1}")
