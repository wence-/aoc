import time
from functools import partial
from itertools import product
from math import sqrt

start = time.time()
with open("../inputs/2021/day04.input") as f:
    moves, *boards = f.read().split("\n\n")
    moves = list(map(int, moves.strip().split(",")))
    boards = [list(map(int, board.strip().split())) for board in boards]
    N = int(sqrt(len(boards[0])))


def time_to_win(board: list[int], times: list[int]) -> int:
    col = [0] * N
    row = [0] * N
    for (r, c), n in zip(product(range(N), range(N)), board):
        t = times[n]
        col[c] = max(col[c], t)
        row[r] = max(row[r], t)
    return min(*col, *row)


def solve(moves: list[int], boards: list[list[int]], pick) -> int:
    times = sorted(range(len(moves)), key=dict(enumerate(moves)).__getitem__)
    win, idx = pick((time_to_win(b, times), i) for i, b in enumerate(boards))
    score = sum(b for b in boards[idx] if times[b] > win)
    return score * moves[win]


part1 = partial(solve, pick=min)
part2 = partial(solve, pick=max)
print(
    f"Day 04     {part1(moves, boards):<13} {part2(moves, boards):<13} {(time.time() - start)*1e6:>13.0f}"
)
