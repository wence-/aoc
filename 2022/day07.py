import time
from collections import defaultdict
from functools import partial
from operator import ge, le

start = time.time()
with open("../inputs/2022/day07.input") as f:
    inp = f.read().split("\n")


def traverse(inp: list) -> dict[tuple, int]:
    loc = ()
    tree = defaultdict(int)
    for line in inp:
        if line[:3] == "$ c":
            p = line.split(" ")[-1]
            if p == "..":
                loc = loc[:-1]
            else:
                loc = loc + (p,)
        elif line[0] not in {"d", "$"}:
            size = int(line.split(" ")[0])
            for i in range(len(loc) + 1):
                tree[loc[:i]] += size
    return tree


def part1(inp: list) -> int:
    return sum(filter(partial(ge, 100_000), traverse(inp).values()))


def part2(inp: list) -> int:
    tree = traverse(inp)
    capacity = 70000000
    want = 30000000
    size = tree[("/",)]
    need = want - (capacity - size)
    return min(filter(partial(le, need), tree.values()))


print(
    f"Day 07     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
