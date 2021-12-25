import time
from collections import Counter

start = time.time()
with open("../inputs/2021/day14.input", "r") as f:
    data = f.read()
    polymer, lines = data.strip().split("\n\n")
    rules = {}
    for line in lines.split("\n"):
        (a, b), c = line.split(" -> ")
        rules[a, b] = c
    inp = (polymer, rules)


def solve(polymer, rules, reps):
    pairs = Counter(zip(polymer, polymer[1:]))
    counts = Counter(polymer)
    for _ in range(reps):
        newpairs = Counter()
        for (a, b), count in pairs.items():
            c = rules[a, b]
            counts[c] += count
            newpairs[a, c] += count
            newpairs[c, b] += count
            pairs = newpairs
    return max(counts.values()) - min(counts.values())


def part1(inp: tuple[str, dict]):
    return solve(*inp, 10)


def part2(inp: tuple[str, dict]):
    return solve(*inp, 40)


print(
    f"Day 14     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
