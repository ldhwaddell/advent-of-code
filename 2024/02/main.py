import fileinput
from typing import List


def validate(report: List[int]) -> bool:
    if all(i < j for i, j in zip(report, report[1:])) or all(
        i > j for i, j in zip(report, report[1:])
    ):
        for i, j in zip(report, report[1:]):
            diff = abs(i - j)
            if diff < 1 or diff > 3:
                return False
        return True
    return False


safe_report = 0
for line in fileinput.input():
    report = [int(n) for n in line.split()]
    if validate(report):
        safe_report += 1


print(f"Part 1: {safe_report}")
