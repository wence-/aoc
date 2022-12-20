import time

start = time.time()
AIR = 0
ROCK = 1
SAND = 2
with open("../inputs/2022/day14.input") as f:
    inp = set()
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
                    inp.add((x, y))

    inp = inp, maxy - 1


def solve(inp, finished):
    grid, maxy = inp
    grid = grid.copy()
    for x in range(200, 700):
        grid.add((x, maxy + 2))
    nrock = len(grid)

    def fall(x, y):
        if (x, y) in grid:
            return True
        elif finished(x, y):
            return False
        elif fall(x, y + 1) and fall(x - 1, y + 1) and fall(x + 1, y + 1):
            grid.add((x, y))
            return True
        else:
            return False

    fall(500, 0)
    return len(grid) - nrock


def part1(inp):
    _, maxy = inp
    return solve(inp, lambda _, y: y > maxy)


def part2(inp):
    return solve(inp, lambda *_: False)


print(
    f"Day 14     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
