import fileinput
from itertools import product


# This feels like a DP problem...

operators = ["+", "*"]


def create_combinations(operators, n):
    return list(product(operators, repeat=n))


def apply_operator_combos(target, nums, operator_combos):
    for combination in operator_combos:
        value = nums[0]
        for op, num in zip(combination, nums[1:]):
            match op:
                case "+":
                    value = value + num

                case "*":
                    value = value * num

                case "||":
                    value = int(str(value) + str(num))

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
        operator_combos[n] = create_combinations(operators, n)

    operator_combinations = operator_combos[n]
    part_1 += apply_operator_combos(target, nums, operator_combinations)

print(f"Part 1: {part_1}")

operator_combos = {}
operators = ["+", "*", "||"]
part_2 = 0
for line in fileinput.input():
    raw_target, raw_nums = line.strip().split(": ")
    target = int(raw_target)
    nums = list(map(int, raw_nums.split(" ")))

    n = len(nums) - 1
    if n not in operator_combos:
        operator_combos[n] = create_combinations(operators, n)

    operator_combinations = operator_combos[n]
    part_2 += apply_operator_combos(target, nums, operator_combinations)

print(f"Part 2: {part_2}")
