import numpy
from intcode import evaluate, load


def stringify(
    grid,
    *,
    default=0,
    characters=None,
    extents=None,
    flipx=False,
    flipy=False,
    imag=False,
):
    if imag:
        grid = dict(((int(X.real), int(X.imag)), v) for X, v in grid.items())
    if extents is not None:
        (minx, maxx), (miny, maxy) = extents
    else:
        extents = numpy.asarray(list(grid))
        minx, miny = extents.min(axis=0)
        maxx, maxy = extents.max(axis=0)
    if characters is None:
        characters = {0: " ", 1: "█"}
    canvas = numpy.full((maxy - miny + 1, maxx - minx + 1), default, dtype=int)
    for (x, y), v in grid.items():
        canvas[y - miny, x - minx] = v
    if flipx:
        canvas = canvas[:, ::-1]
    if flipy:
        canvas = canvas[::-1, :]
    return "\n".join("".join(characters.get(c, str(c)) for c in row) for row in canvas)


class Robot(object):
    directions = (1j, 1, -1j, -1)
    turns = (-1, 1)

    def __init__(self, mem):
        self.pos = 0
        self.facing = 0  # up
        self.grid = {}
        self.mem = mem

    def move(self, turn):
        self.facing = (self.facing + Robot.turns[turn]) % 4
        self.pos += Robot.directions[self.facing]

    def inputs(self, first=0):
        yield first
        while True:
            yield self.grid.get(self.pos, 0)

    def paint(self, first=0):
        outputs = evaluate(self.mem, inputs=self.inputs(first=first))
        for colour, turn in zip(outputs, outputs):
            self.grid[self.pos] = colour
            self.move(turn)

    def draw(self):
        return stringify(self.grid, characters={0: " ", 1: "█"}, flipy=True, imag=True)


mem = load("day11.input")


def part1(mem):
    robot = Robot(mem)
    robot.paint(first=0)
    return len(robot.grid)


def part2(mem):
    robot = Robot(mem)
    robot.paint(first=1)
    return robot.draw()


print(f"Part 1: {part1(mem)}")
print(f"Part 2:\n{part2(mem)}")
