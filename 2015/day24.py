import time
from functools import partial, reduce
from itertools import combinations
from operator import mul

start = time.time()
with open("../inputs/2015/24.input", "r") as f:
    data = set(map(int, f.read().strip().split()))


def give_next_combination(data, goal):
    yield from (
        set(c)
        for n in range(1, len(data))
        for c in combinations(data, n)
        if (sum(c) == goal)
    )


def partition_exists(data, goal, i):
    for c in give_next_combination(data, goal):
        if i > 2:
            return partition_exists(data - c, goal, i - 1)
        else:
            return True


def partition(data, n):
    size = len(data)
    goal = sum(data) // n
    assert goal * n == sum(data)
    for c in give_next_combination(data, goal):
        if partition_exists(data - c, goal, n - 1):
            if len(c) > size:
                return
            yield c
            size = len(c)


part1 = min(map(partial(reduce, mul), partition(data, 3)))
part2 = min(map(partial(reduce, mul), partition(data, 4)))

print(f"Day 24     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
