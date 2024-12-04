import fileinput
import re


def parse_muls(line: str):
    line_sum = 0
    for match in re.findall(r"mul\((\d{1,3},\d{1,3})\)", line):
        l, r = list(map(int, match.split(",")))
        line_sum += l * r

    return line_sum


part_1 = 0
for line in fileinput.input():
    part_1 += parse_muls(line)


part_2 = 0
# Concat everything into one line
input = "".join([l.strip() for l in fileinput.input()])

# Remove everything between a don't and a do. Ensure that:
#   - Match any white space or non-whitespace character.
#   - Make the match between dont and do non-greedy. Otherwise the .* will match while rest of line.
#   - The last do is optional. We could match until end of line, in which case whole rest of line should       be removed.
cleaned = re.sub(r"don\'t\(\).*?(do\(\)|$)", "", input)
part_2 = parse_muls(cleaned)


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
