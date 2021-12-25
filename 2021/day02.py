import time

start = time.time()
F = object()
D = object()


with open("../inputs/2021/day02.input", "r") as f:
    moves = []
    for line in f.read().strip().split("\n"):
        if line[0] == "f":
            moves.append((F, int(line[8:])))
        elif line[0] == "d":
            moves.append((D, int(line[5:])))
        elif line[0] == "u":
            moves.append((D, -int(line[3:])))
        else:
            raise ValueError


def part1(moves):
    h, d = 0, 0
    for move, n in moves:
        if move is F:
            h += n
        else:
            d += n
    return h * d


def part2(moves):
    h, d, a = 0, 0, 0
    for move, n in moves:
        if move is F:
            h += n
            d += a * n
        else:
            a += n
    return h * d


print(
    f"Day 02     {part1(moves):<14} {part2(moves):<14} {(time.time() - start)*1e3:>11.2f}"
)
