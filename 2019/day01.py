with open("../inputs/2019/day01.input", "r") as f:
    data = list(map(lambda x: int(x.strip()), f.readlines()))


def fuel(x):
    return max((x // 3) - 2, 0)


def total(x):
    req = fuel(x)
    total = 0
    while req > 0:
        total += req
        req = fuel(req)
    return total


def part1(data):
    return sum(map(fuel, data))


def part2(data):
    return sum(map(total, data))


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
