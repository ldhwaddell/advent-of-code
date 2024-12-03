import fileinput
from typing import List


def validate(report: List[int]) -> bool:
    increasing = all(i < j for i, j in zip(report, report[1:]))
    decreasing = all(i > j for i, j in zip(report, report[1:]))
    valid_diff = all(1 <= abs(i - j) <= 3 for i, j in zip(report, report[1:]))

    return (increasing and valid_diff) or (decreasing and valid_diff)


safe_report_part_1 = 0
safe_report_part_2 = 0
for line in fileinput.input():
    report = [int(n) for n in line.split()]

    if validate(report):
        safe_report_part_1 += 1

    # Check all sublists
    if any(validate(report[:i] + report[i + 1 :]) for i in range(len(report))):
        safe_report_part_2 += 1


print(f"Part 1: {safe_report_part_1}")
print(f"Part 2: {safe_report_part_2}")
