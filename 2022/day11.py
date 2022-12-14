import time
from collections.abc import Callable
from functools import partial, reduce
from operator import add, mul
from typing import NamedTuple

start = time.time()


class Monkey(NamedTuple):
    items: list[int]
    op: Callable[[int], int]
    divisor: int
    target: tuple[int, int]

    def copy(self):
        return Monkey(self.items[:], self.op, self.divisor, self.target)


with open("../inputs/2022/day11.input") as f:
    inp = []
    for monkey in f.read().split("\n\n"):
        lines = monkey.split("\n")
        items = list(map(int, lines[1][18:].split(", ")))
        op = lines[2][19:]
        operator = {"+": add, "*": mul}[op[4]]
        try:
            r = int(op[6:])
            op = partial(operator, r)
        except ValueError:
            op = lambda o: o * o
        divisor = int(lines[3][21:])
        target = (int(lines[5][-1]), int(lines[4][-1]))
        inp.append(Monkey(items, op, divisor, target))


def solve(inp: list[Monkey], happiness: int, rounds: int):
    inp = [m.copy() for m in inp]
    counts = [0] * len(inp)
    reducer = reduce(mul, (m.divisor for m in inp))
    for _ in range(rounds):
        for i, (items, op, divisor, target) in enumerate(inp):
            for item in items:
                item = (op(item) // happiness) % reducer
                inp[target[item % divisor == 0]].items.append(item)
            counts[i] += len(items)
            items.clear()
    counts = sorted(counts)
    return mul(*counts[-2:])


def part1(inp: list) -> int:
    return solve(inp, 3, 20)


def part2(inp: list) -> int:
    return solve(inp, 1, 10_000)


print(
    f"Day 11     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
