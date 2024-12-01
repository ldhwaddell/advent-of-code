import fileinput
from collections import Counter

left, right = [], []

for line in fileinput.input():
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total_distance = 0
for l, r in zip(left, right):
    total_distance += abs(r - l)

print(f"Part 1: {total_distance}")

counter = Counter(right)

similarity_score = 0
for l in left:
    occurrences = counter.get(l, 0)
    similarity_score += l * occurrences

print(f"Part 2: {similarity_score}")
