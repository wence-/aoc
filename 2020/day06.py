from collections import Counter
from itertools import chain

with open("inputs/day06.input", "r") as f:
    data = f.read()
    groups = data.strip().split("\n\n")


def part1(groups):
    return sum(len(Counter(chain(*(a for a in group.split("\n")))))
               for group in groups)


def part2(groups):
    return sum(sum(a == len(group.split("\n"))
                   for a in Counter(chain(*(a for a in group.split("\n"))))
                   .values())
               for group in groups)


print(f"Part 1: {part1(groups)}")
print(f"Part 2: {part2(groups)}")
