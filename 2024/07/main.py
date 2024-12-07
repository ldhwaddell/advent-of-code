import fileinput
from itertools import product


operators = ["+", "*"]


def create_combinations(n):
    return list(product(operators, repeat=n))


def apply_operator_combos(target, nums, operator_combos):
    for combination in operator_combos:
        value = nums[0]
        for op, num in zip(combination, nums[1:]):
            value = value + num if op == "+" else value * num

        if value == target:
            return target

    return 0


operator_combos = {}
part_1 = 0
for line in fileinput.input():
    raw_target, raw_nums = line.strip().split(": ")
    target = int(raw_target)
    nums = list(map(int, raw_nums.split(" ")))

    n = len(nums) - 1
    if n not in operator_combos:
        operator_combos[n] = create_combinations(n)

    operator_combinations = operator_combos[n]
    part_1 += apply_operator_combos(target, nums, operator_combinations)

print(f"Part 1: {part_1}")
