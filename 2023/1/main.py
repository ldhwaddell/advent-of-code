import fileinput
from typing import Dict

DIGITS = {str(i): i for i in range(1, 10)}

DIGIT_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calibrate(line: str, d: Dict[str, int]) -> int:
    first_match = None
    last_match = None
    for i, c in enumerate(line):
        for key, val in d.items():
            # Test each substr from line[i] to end of line against current dict key
            # If it is a match and start is none, then this is the first match in line.
            # End always gets updated to be the current match, so that if only 1 match, start = end.
            if line[i:].startswith(key):
                if not first_match:
                    first_match = val
                last_match = val

    # Equivalent to int(f"{first_match}{last_match}"). Think base 10.
    return first_match * 10 + last_match


sum_1 = 0
sum_2 = 0
for line in fileinput.input():
    sum_1 += calibrate(line, DIGITS)
    sum_2 += calibrate(line, DIGITS | DIGIT_WORDS)

print(f"Part 1: {sum_1}")
print(f"Part 2: {sum_2}")
