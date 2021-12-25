import time
from collections import Counter
from functools import cache
from itertools import product, repeat

start = time.time()
with open("../inputs/2021/day21.input", "r") as f:
    p1, p2 = f.read().split("\n")
    p1 = int(p1[-2:])
    p2 = int(p2[-2:])
    inp = p1, p2


def part1(inp):
    p1, p2 = inp
    p1 -= 1
    p2 -= 1
    s1 = 0
    s2 = 0

    die = 1

    def roll():
        nonlocal die
        val = 3 * (die + 1)
        die += 3
        return val

    while True:
        p1 = (p1 + roll()) % 10
        s1 += p1 + 1
        if s1 >= 1000:
            return s2 * (die - 1)
        p2 = (p2 + roll()) % 10
        s2 += p2 + 1
        if s2 >= 1000:
            return s1 * (die - 1)


def part2(inp):
    p1, p2 = inp
    p1 -= 1
    p2 -= 1

    moves = list(Counter(map(sum, product(*repeat(range(1, 4), 3)))).items())

    @cache
    def winners(A, B, s1, s2):
        if s1 >= 21:
            return (1, 0)
        if s2 >= 21:
            return (0, 1)
        winA = 0
        winB = 0
        for move, freq in moves:
            newA = (A + move) % 10
            news1 = s1 + newA + 1
            x, y = winners(B, newA, s2, news1)
            winA += y * freq
            winB += x * freq
        return (winA, winB)

    return max(winners(p1, p2, 0, 0))


print(
    f"Day 21     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>10.2f}"
)
