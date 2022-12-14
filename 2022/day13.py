import time
from functools import cmp_to_key
from itertools import chain
from operator import mul

start = time.time()


with open("../inputs/2022/day13.input") as f:
    inp = [list(map(eval, block.split("\n"))) for block in f.read().split("\n\n")]


def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            return (right < left) - (left < right)
        else:
            return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    elif left and right:
        return (
            val if (val := compare(left[0], right[0])) else compare(left[1:], right[1:])
        )
    else:
        return bool(left) - bool(right)


def part1(inp: list) -> int:
    return sum(
        i
        for i, val in enumerate((compare(*pair) for pair in inp), start=1)
        if val == -1
    )


def part2(inp: list) -> int:
    return mul(
        *(
            i
            for i, val in enumerate(
                sorted([2, 6, *chain.from_iterable(inp)], key=cmp_to_key(compare)),
                start=1,
            )
            if val == 2 or val == 6
        )
    )


print(
    f"Day 13     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
