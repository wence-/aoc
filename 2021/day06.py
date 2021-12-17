import time
from collections import deque

start = time.time()
with open("../inputs/2021/day06.input", "r") as f:
    inp = list(map(int, f.read().strip().split(",")))


def solve(ages, rounds):
    fish = deque([0] * 9, maxlen=9)
    for a in ages:
        fish[a] += 1
    for _ in range(rounds):
        fish.rotate(-1)
        fish[6] += fish[8]
    return sum(fish)


print(
    f"Day 06     {solve(inp, 80):<13} {solve(inp, 256):<14} {(time.time() - start)*1e6:>13.0f}"
)
