import fileinput

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
