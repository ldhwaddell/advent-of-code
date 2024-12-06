import fileinput
from typing import List

input = "".join([l for l in fileinput.input()])
rules, updates = input.split("\n\n")

rule_map = {}

# Extract rules into lookup
for rule in rules.split("\n"):
    before, after = list(map(int, rule.split("|")))
    rule_map[(before, after)] = True
    rule_map[(after, before)] = False


def validate(update: List[int]) -> int:
    # Compare each pair in the update list
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            # If the pair in rule map, and update[i] does not come before update[j], return invalid
            coords = (update[i], update[j])
            if coords in rule_map and not rule_map[coords]:
                return 0

    # else, return middle value
    return update[len(update) // 2]


count_1 = 0
for update in updates.split("\n")[:-1]:
    update = list(map(int, update.split(",")))
    count_1 += validate(update)

print(f"Part 1: {count_1}")
