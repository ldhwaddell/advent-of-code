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


# Keep track of files in a map. id -> (start, length)
files = dict()
# Keep track of blanks in order [(start, length)]
spaces = []

start = 0
curr_id = 0


for i, n in enumerate(nums):
    # n is the number of times the id/blank is repeated.

    if i % 2 == 0:
        files[curr_id] = (start, n)
        curr_id += 1
    else:
        # Make sure we dont append space if it has 0 width
        if n != 0:
            spaces.append((start, n))
    start += n

# While there are ids to check:
while curr_id > 0:
    curr_id -= 1
    curr_file_start, curr_file_length = files[curr_id]

    for i, (space_start, space_length) in enumerate(spaces):
        # If the space starts after our file does, then we cannot use it.
        # We also know that we wont need to search any of the following spaces ever, because our spaces are ordered, and the files starts will decrease as the curr_id does.
        if space_start >= curr_file_start:
            spaces = spaces[:i]
            break

        # This means we use the entire space and can remove it from list.
        if curr_file_length == space_length:
            files[curr_id] = (space_start, curr_file_length)
            spaces.pop(i)
            break

        elif curr_file_length < space_length:
            files[curr_id] = (space_start, curr_file_length)
            # We havent used the full space, it now starts after the file intertion
            # and is shorter by the file size.
            spaces[i] = (
                space_start + curr_file_length,
                space_length - curr_file_length,
            )
            break


part_2 = 0
for f_id, (f_start, f_length) in files.items():
    # Suppose we had id 9 starting at 7 with length 3
    # This would add (9 * 7), (9 * 8), and (9 * 9) to the total.
    # Conveniently don't need to deal with . this way
    for i in range(f_start, f_start + f_length):
        part_2 += f_id * i


print(f"Part 2: {part_2}")
