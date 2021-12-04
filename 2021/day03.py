with open("../inputs/2021/day03.input") as f:
    inp = [[int(c) for c in line.strip()]
           for line in f.readlines()]


def part1(inp: list[list[int]]) -> int:
    N, n = len(inp), len(inp[0])
    N = (N + 1) // 2
    gamma = sum((c >= N) << (n - i - 1)
                for i, c in enumerate(map(sum, zip(*inp))))
    return gamma * ((1 << n) - 1 - gamma)


def prune(inp: list[list[int]], bit: int, flip: bool) -> int:
    keep = flip ^ (sum(b[bit] for b in inp) >= (len(inp) + 1) // 2)
    filtered = [b for b in inp if b[bit] == keep]
    try:
        x, = filtered
        n = len(x) - 1
        return sum(c << (n - i) for i, c in enumerate(x))
    except ValueError:
        return prune(filtered, bit+1, flip)


def part2(inp: list[list[int]]) -> int:
    return prune(inp, 0, False)*prune(inp, 0, True)


print(f"Part 1: {part1(inp)}")
print(f"Part 2: {part2(inp)}")
