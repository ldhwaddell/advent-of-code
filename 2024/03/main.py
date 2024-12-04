import fileinput
import re

pattern = r"mul\((\d{1,3},\d{1,3})\)"


def parse_muls(line: str):
    line_sum = 0
    for match in re.findall(pattern, line):
        l, r = list(map(int, match.split(",")))
        line_sum += l * r

    return line_sum


part_1 = 0
for line in fileinput.input():
    part_1 += parse_muls(line)


print(f"Part 1: {part_1}")
# print(f"Part 2: {safe_report_part_2}")
