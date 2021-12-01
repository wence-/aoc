from collections import Counter


def valid(d, p2=False):
    digits = list(str(d))
    if digits != sorted(digits):
        return 0
    counts = Counter(digits).values()
    if all(x == 1 for x ../in/2019 counts):
        return 0
    if p2 and not any(x == 2 for x in counts):
        return 0
    return 1


def part1():
    return sum(valid(d) for d in range(245182, 790573))


def part2():
    return sum(valid(d, p2=True) for d in range(245182, 790573))


print(f"Part 1: {part1()}")
print(f"Part 1: {part2()}")
