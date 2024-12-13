import fileinput

for line in fileinput.input():
    nums = list(map(int, [n for n in line.strip()]))
    break

# Generate dot map.
disk = []
curr_id = 0
for i in range(len(nums)):
    if i % 2 == 0:
        disk.extend([curr_id] * nums[i])
        curr_id += 1
    else:
        disk.extend(["."] * nums[i])

# Execute the swap
l, r = 0, len(disk) - 1

while l != r:
    if disk[l] != ".":
        l += 1
    elif disk[r] == ".":
        r -= 1
    else:
        disk[l], disk[r] = disk[r], disk[l]

# Calculate checksum
part_1 = sum(disk[i] * i for i in range(len(disk)) if disk[i] != ".")
print(f"Part 1: {part_1}")
