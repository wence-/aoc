import time
from itertools import islice

start = time.time()
with open("../inputs/2022/day05.input") as f:
    stacks, moves = f.read().split("\n\n")
    moves = [tuple(map(int, move.split(" ")[1::2])) for move in moves.split("\n")]
    stacks = [
        # Will reverse when copying later
        list(filter(lambda x: x != " ", stack))
        for stack in islice(zip(*stacks.split("\n")[:-1]), 1, None, 4)
    ]
    inp = moves, stacks


def part1(inp: tuple[list[tuple[int, ...]], list[list[str]]]) -> str:
    moves, stacks = inp
    stacks = [s[::-1] for s in stacks]
    for n, src, dst in moves:
        stacks[dst - 1].extend(stacks[src - 1].pop() for _ in range(n))
    return "".join(s.pop() for s in stacks)


def part2(inp: tuple[list, list]) -> str:
    moves, stacks = inp
    stacks = [s[::-1] for s in stacks]
    for n, src, dst in moves:
        stacks[dst - 1].extend(reversed(list(stacks[src - 1].pop() for _ in range(n))))
    return "".join(s.pop() for s in stacks)


print(
    f"Day 05     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
