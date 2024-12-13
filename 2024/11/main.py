import fileinput
from functools import cache

ITERATIONS = 75
for line in fileinput.input():
    nums = list(map(int, line.strip().split()))
    break


# The question we ask is: How many stones are produces from a stone n with x remaining iterations.


# @cache stores each unqieu result of (n, remaining_iters). Once it has been computed once, it doesnt happen again
@cache
def solve(n, remaining_iters):
    # If no more iterations we return 1 because we just count the stone itself
    if remaining_iters == 0:
        return 1

    # If stone is 0, convert to 1 and see how many stones result from that
    if n == 0:
        return solve(1, remaining_iters - 1)

    # If stones has even # of digits, figure out how many stones result from each half.
    if len(str(n)) % 2 == 0:
        n = str(n)
        return solve(int(n[: len(n) // 2]), remaining_iters - 1) + solve(
            int(n[len(n) // 2 :]), remaining_iters - 1
        )

    # Otherwise multiply by 2024 and see how many stones result from that.
    return solve(n * 2024, remaining_iters - 1)


total = sum([solve(n, ITERATIONS) for n in nums])
print(f"Total: {total}")
