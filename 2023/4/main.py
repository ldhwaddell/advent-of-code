import fileinput

from collections import Counter


def points_1(line: str) -> int:
    card_id, nums = line.strip().split(": ")
    winning_nums, card_nums = nums.split(" | ")

    winning_set = set(filter(lambda c: c != "", winning_nums.split(" ")))
    card_nums_set = set(filter(lambda c: c != "", card_nums.split(" ")))
    matches = winning_set & card_nums_set

    if not matches:
        return 0

    return 2 ** (len(matches) - 1)


counter = Counter()


def points_2(line: str) -> int:
    card_id, nums = line.strip().split(": ")
    card_id = int(card_id[5:])
    winning_nums, card_nums = nums.split(" | ")

    winning_set = set(filter(lambda c: c != "", winning_nums.split(" ")))
    card_nums_set = set(filter(lambda c: c != "", card_nums.split(" ")))
    matches = winning_set & card_nums_set

    # Add original card to the count
    counter[card_id] += 1

    if not matches:
        return

    # Suppose card 1 has 2 matches.
    # This iterates from card 2 to 5.
    # We then increase the cound of this copied card id, by the count of the card id.
    # So if we have 2 card 1's, then we increase count by 2 for cards 2, 3, 4, 5.
    for copy_card_id in range(card_id + 1, card_id + len(matches) + 1):
        counter[copy_card_id] += counter[card_id]


sum_1 = 0

for line in fileinput.input():
    sum_1 += points_1(line)
    points_2(line)

print(f"Part 1: {sum_1}")
print(f"Part 2: {sum(counter.values())}")
