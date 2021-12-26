from itertools import cycle

import numpy

with open("../inputs/2018/day13.input") as f:
    data = f.readlines()


parsed = []
translate = {
    " ": 0,
    "-": 1,
    "|": 2,
    "+": 3,
    "/": 4,
    "\\": 5,
    ">": 6,
    "v": 7,
    "<": 8,
    "^": 9,
    "X": 10,
}

back = dict((v, k) for k, v in translate.items())

for line in data:
    line = line[:-1]
    if line == "":
        continue
    parse = [translate[c] for c in line]
    parsed.append(parse)

shape = (max(map(len, parsed)), len(parsed))

grid = numpy.zeros(shape, dtype=int)

for i, p in enumerate(parsed):
    grid[: len(p), i] = p


def print_grid(grid, carts, cartmap):
    cols, rows = grid.shape
    for row in range(rows):
        for col in range(cols):
            if carts[col, row]:
                print(
                    {"right": ">", "left": "<", "down": "v", "up": "^", "crash": "X"}[
                        cartmap[carts[col, row]].state
                    ],
                    end="",
                )
            else:
                print(back[grid[col, row]], end="")
        print("")


class Cart(object):
    def __init__(self, state):
        if state == ">":
            self.state = "right"
        elif state == "<":
            self.state = "left"
        elif state == "v":
            self.state = "down"
        elif state == "^":
            self.state = "up"
        else:
            raise ValueError()
        self.turn = cycle(range(3))

    def next_loc(self, pos):
        x, y = pos
        if self.state == "right":
            return (x + 1, y)
        elif self.state == "left":
            return (x - 1, y)
        elif self.state == "down":
            return (x, y + 1)
        elif self.state == "up":
            return (x, y - 1)

    def next(self, grid, pos, carts, can_remove=False):
        npos = self.next_loc(pos)
        if grid[npos] == 0:
            raise ValueError("fucked")
        if carts[npos]:
            if not can_remove:
                self.state = "crash"
                return True, npos
            else:
                killed = carts[pos], carts[npos]
                carts[pos] = 0
                carts[npos] = 0
                return True, killed
        if back[grid[npos]] == "+":
            new = {0: "left", 1: "straight", 2: "right"}[next(self.turn)]
            self.state = {
                "left": {"right": "up", "left": "down", "down": "right", "up": "left"}[
                    self.state
                ],
                "straight": self.state,
                "right": {"right": "down", "left": "up", "down": "left", "up": "right"}[
                    self.state
                ],
            }[new]
        if back[grid[npos]] == "/":
            self.state = {"up": "right", "left": "down", "right": "up", "down": "left"}[
                self.state
            ]
        if back[grid[npos]] == "\\":
            self.state = {"down": "right", "right": "down", "left": "up", "up": "left"}[
                self.state
            ]
        carts[npos] = carts[pos]
        carts[pos] = 0
        return False, npos


ogrid = grid.copy()
cartmap = {}
carts = numpy.zeros_like(grid)
where = numpy.where(numpy.logical_and(5 < grid, grid < 10))

for x, (i, j) in enumerate(zip(*where), start=1):
    carts[i, j] = x
    cartmap[x] = Cart(back[grid[i, j]])

grid[grid == 6] = 1
grid[grid == 7] = 2
grid[grid == 8] = 1
grid[grid == 9] = 2

while True:
    where = numpy.where(carts > 0)
    done = False
    for i, j in zip(*where):
        cart = cartmap[carts[i, j]]
        crash, pos = cart.next(grid, (i, j), carts)
        if crash:
            done = True
            break
    if done:
        break

print(f"Part 1: {','.join(map(str, pos))}")


grid = ogrid
cartmap = {}
carts = numpy.zeros_like(grid)
where = numpy.where(numpy.logical_and(5 < grid, grid < 10))

for x, (i, j) in enumerate(zip(*where), start=1):
    carts[i, j] = x
    cartmap[x] = Cart(back[grid[i, j]])

grid[grid == 6] = 1
grid[grid == 7] = 2
grid[grid == 8] = 1
grid[grid == 9] = 2

while True:
    where = numpy.where(carts > 0)
    done = False
    for i, j in zip(*where):
        cart = carts[i, j]
        if cart == 0:
            continue
        cart = cartmap[cart]
        crash, pos = cart.next(grid, (i, j), carts, can_remove=True)
        if crash:
            del cartmap[pos[0]]
            del cartmap[pos[1]]
        if len(cartmap) == 1:
            (key,) = cartmap.keys()
            (i,), (j,) = numpy.where(carts == key)
            cart = cartmap[key]
            crash, pos = cart.next(grid, (i, j), carts, can_remove=True)
            assert not crash
            done = True
            break
    if done:
        break

print(f"Part 2: {','.join(map(str, pos))}")
