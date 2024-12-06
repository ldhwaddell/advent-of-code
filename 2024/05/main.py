import fileinput
from functools import cmp_to_key
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
            coords = (update[i], update[j])
            # If update[i] should not come before update[j], break
            if not rule_map.get(coords, True):
                return 0

    # else, return middle value
    return update[len(update) // 2]


count_1 = 0
for update in updates.split("\n")[:-1]:
    update = list(map(int, update.split(",")))
    count_1 += validate(update)

print(f"Part 1: {count_1}")


rule_map = {}


# This approach uses a comparator function.
# With this:
#   - cmp(x, y) == -1 if x comes before y
#   - cmp(x, y) == 0 if x == y
#   - cmp(x, y) == 1 if x comes after y
for rule in rules.split("\n"):
    before, after = list(map(int, rule.split("|")))
    rule_map[(before, after)] = -1
    rule_map[(after, before)] = 1


def validate(update: List[int]) -> int:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            coords = (update[i], update[j])
            # If update[i] comes after update[j], false
            if rule_map.get(coords, 0) == 1:
                return False

    return True


# This function takes the current and next value from the list and compares them.
# If the pair is not in rule_map, we assume 0, meaning no swap is necessary.
# If the pair returns -1, we leave the pair as is because 'a' should come before 'b'.
# If the pair returns 1, it indicates 'a' should come after 'b', so the two elements
# will be swapped during sorting.
def cmp(a, b):
    return rule_map.get((a, b), 0)


count_2 = 0
for update in updates.split("\n")[:-1]:
    update = list(map(int, update.split(",")))
    if validate(update):
        continue

    # Sort based on the rule pairs
    sorted_update = sorted(update, key=cmp_to_key(cmp))

    count_2 += sorted_update[len(update) // 2]

print(f"Part 2: {count_2}")
