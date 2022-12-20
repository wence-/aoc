import time
from collections import defaultdict

start = time.time()
AIR = 0
ROCK = 1
SAND = 2
with open("../inputs/2022/day14.input") as f:
    inp = defaultdict(int)
    maxy = 0
    for line in f.read().split("\n"):
        pieces = line.split(" -> ")
        pieces = [tuple(map(int, piece.split(","))) for piece in pieces]
        for (startx, starty), (endx, endy) in zip(pieces, pieces[1:]):
            if startx >= endx:
                startx, endx = endx, startx
            if starty >= endy:
                starty, endy = endy, starty
            maxy = max(maxy, endy + 1)
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    inp[x, y] = ROCK

    inp = inp, maxy - 1


def solve(inp, finished):
    grid, maxy = inp
    grid = grid.copy()
    for x in range(200, 700):
        grid[x, maxy + 2] = ROCK
    obstacles = {k for k, v in grid.items() if v == ROCK}
    nrock = len(obstacles)
    sand: list[tuple[int, int]] = [(500, 0)]
    while sand:
        while True:
            xs, ys = sand[-1]
            for dx in [0, -1, 1]:
                if (c := (xs + dx, ys + 1)) not in obstacles:
                    sand.append(c)
                    break
            else:
                obstacles.add(sand.pop())
                break
            if finished(xs, ys):
                return len(obstacles) - nrock
    return len(obstacles) - nrock


def part1(inp):
    _, maxy = inp
    return solve(inp, lambda _, y: y >= maxy)


def part2(inp):
    return solve(inp, lambda *_: False)


print(
    f"Day 14     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
