with open("../inputs/2021/day07.input", "r") as f:
    inp = sorted(map(int, f.read().strip().split(",")))


def part1(inp):
    # Probably doesn't work for all inputs
    median = inp[len(inp) // 2]
    return sum(abs(k - median) for k in inp)


def part2(inp):
    # Probably doesn't work for all inputs
    mean = sum(inp) // len(inp)
    return sum((abs(k - mean) * (abs(k - mean) + 1)) // 2 for k in inp)


# Original solutions
def part1_brute_force(inp):
    from collections import Counter

    inp = Counter(inp)
    lo = min(inp)
    hi = max(inp)

    def cost(n) -> int:
        return sum(abs(k - n) * v for k, v in inp.items())

    return min(cost(i) for i in range(lo, hi + 1))


def part2_brute_force(inp):
    from collections import Counter

    inp = Counter(inp)
    lo = min(inp)
    hi = max(inp)

    def cost(n):
        return sum(v * (abs(k - n) * (abs(k - n) + 1)) // 2 for k, v in inp.items())

    return min(cost(i) for i in range(lo, hi + 1))


print(part1(inp))
print(part2(inp))
