import fileinput
from functools import reduce
from collections import Counter
from typing import Dict
from operator import mul


PART_1_LIMITS = {"red": 12, "green": 13, "blue": 14}


def possible_game_1(line: str, d: Dict[str, int]) -> int:
    game, game_logs = line.strip().split(": ")
    game_id = int(game[5:])

    for game_log in game_logs.split("; "):
        for result in game_log.split(", "):
            count, color = result.split(" ")
            n = int(count)

            if n > PART_1_LIMITS[color]:
                return 0

    return game_id


def possible_game_2(line: str) -> int:
    game, game_logs = line.strip().split(": ")

    c = Counter()

    for game_log in game_logs.split("; "):
        for result in game_log.split(", "):
            count, color = result.split(" ")
            n = int(count)

            c[color] = max(c[color], n)

    power_set = reduce(mul, list(c.values()))

    return power_set


sum_1 = 0
sum_2 = 0

for line in fileinput.input():
    sum_1 += possible_game_1(line, PART_1_LIMITS)
    sum_2 += possible_game_2(line)

print(f"Part 1: {sum_1}")
print(f"Part 2: {sum_2}")
