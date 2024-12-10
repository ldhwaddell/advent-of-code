import fileinput

input = [l.strip() for l in fileinput.input()]

input = input[0]

blocks = []
curr_id = 0
for i in range(len(input)):
    if i % 2 == 0:
        blocks.extend([curr_id for n in range(int(input[i]))])
        curr_id += 1
    else:
        blocks.extend(["." for n in range(int(input[i]))])

l, r = 0, len(blocks) - 1
while l != r:
    if blocks[l] != ".":
        l += 1

    elif blocks[r] == ".":
        r -= 1
    else:
        blocks[l], blocks[r] = blocks[r], blocks[l]
        l += 1
        r -= 1


part_1 = 0
for i in range(len(blocks)):
    if blocks[i] == ".":
        continue

    part_1 += i * blocks[i]

print(f"Part 1: {part_1}")
