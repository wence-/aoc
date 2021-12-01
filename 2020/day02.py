from collections import Counter

rules = []

with open("../inputs/2020/day02.input", "r") as f:
    for line in f.readlines():
        count, (char, _), passwd = line.strip().split(" ")
        lo, hi = map(int, count.split("-"))
        rules.append(((lo, hi), char, passwd))


def part1(rules):
    nvalid = 0
    for (lo, hi), char, passwd in rules:
        occurences = Counter(passwd).get(char, -1)
        if lo <= occurences <= hi:
            nvalid += 1
    return nvalid


def part2(rules):
    nvalid = 0
    for (lo, hi), char, passwd in rules:
        loc = passwd[lo-1]
        hic = passwd[hi-1]
        nvalid += (loc == char) ^ (hic == char)
    return nvalid


print(f"Part 1: {part1(rules)}")
print(f"Part 2: {part2(rules)}")
