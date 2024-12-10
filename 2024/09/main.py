import fileinput


def parse_input(input_line):
    blocks = []
    curr_id = 0
    for i in range(len(input_line)):
        count = int(input_line[i])
        if i % 2 == 0:
            blocks.extend([curr_id] * count)
            curr_id += 1
        else:
            blocks.extend(["."] * count)
    return blocks


def rearrange_blocks_1(blocks):
    l, r = 0, len(blocks) - 1
    while l < r:
        if blocks[l] != ".":
            l += 1
        elif blocks[r] == ".":
            r -= 1
        else:
            blocks[l], blocks[r] = blocks[r], blocks[l]
            l += 1
            r -= 1
    return blocks


def calculate_score(blocks):
    return sum(i * block for i, block in enumerate(blocks) if block != ".")


input_line = [line.strip() for line in fileinput.input()][0]
blocks = parse_input(input_line)
blocks = rearrange_blocks_1(blocks)
part_1 = calculate_score(blocks)
print(f"Part 1: {part_1}")


def rearrange_blocks_contiguous(blocks):
    return blocks


input_line = [line.strip() for line in fileinput.input()][0]
blocks = parse_input(input_line)
blocks = rearrange_blocks_contiguous(blocks)
part_2 = calculate_score(blocks)
print(f"Part 2: {part_2}")
