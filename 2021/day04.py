from itertools import product
from operator import lt, gt

N = 5
with open("../inputs/2021/day04.input") as f:
    moves, *boards = f.read().split("\n\n")
    moves = list(map(int, moves.strip().split(",")))
    boards = [list(map(int, board.strip().split()))
              for board in boards]


def time_to_win(board, times):
    col = [0] * N
    row = [0] * N
    for (r, c), n in zip(product(range(N), range(N)),
                         board):
        t = times[n]
        col[c] = max(col[c], t)
        row[r] = max(row[r], t)
    return min(*col, *row)


def solve(moves, boards, cmp, init):
    idx = 0
    win = init
    times = moves[:]
    for i, n in enumerate(moves):
        times[n] = i
    for i, board in enumerate(boards):
        t = time_to_win(board, times)
        if cmp(t, win):
            win = t
            idx = i
    score = sum(b for b in boards[idx] if times[b] > win)
    return score * moves[win]


def part1(moves, boards):
    return solve(moves, boards, lt, len(moves))


def part2(moves, boards):
    return solve(moves, boards, gt, 0)


print(f"Part 1: {part1(moves, boards)}")
print(f"Part 2: {part2(moves, boards)}")
