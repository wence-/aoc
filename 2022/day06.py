import time
from functools import partial

from more_itertools import windowed

start = time.time()
with open("../inputs/2022/day06.input") as f:
    inp = f.read()


def solve(n: int, inp: str):
    return next(
        filter(lambda iwin: len(set(iwin[1])) == n, enumerate(windowed(inp, n), n))
    )[0]


part1 = partial(solve, 4)
part2 = partial(solve, 14)


print(
    f"Day 06     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
