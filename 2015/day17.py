import time
from itertools import chain, combinations

start = time.time()
with open("../inputs/2015/17.input", "r") as f:
    data = list(map(int, f.read().strip().split("\n")))


part1 = sum(
    1
    for x in chain(*(combinations(data, i) for i in range(1, len(data) + 1)))
    if sum(x) == 150
)

for minc in range(1, len(data) + 1):
    nc = sum(1 for x in combinations(data, minc) if sum(x) == 150)
    if nc > 0:
        break

part2 = nc

print(f"Day 17     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
