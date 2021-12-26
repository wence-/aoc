from collections import defaultdict
from functools import cached_property, reduce
from math import sqrt
from operator import add, mul, sub

import numpy
from scipy.ndimage import convolve


class Tile:
    def __init__(self, n, image):
        self.n = n
        self.im = image
        self.edges = (
            sum(2 ** i * n for i, n in enumerate(image[0, :])),  # top
            sum(2 ** i * n for i, n in enumerate(image[:, -1])),  # right
            sum(2 ** i * n for i, n in enumerate(image[-1, :])),  # bottom
            sum(2 ** i * n for i, n in enumerate(image[:, 0])),
        )  # left
        self.image = self.im[1:-1, 1:-1]

    def __hash__(self):
        return self.n

    @cached_property
    def variants(self):
        v = [self]
        for k in range(1, 4):
            v.append(Tile(self.n, numpy.rot90(self.im, k=k)))
        flip = Tile(self.n, self.im[::-1, :])
        v.append(flip)
        for k in range(1, 4):
            v.append(Tile(flip.n, numpy.rot90(flip.im, k=k)))
        return tuple(v)


monster = Tile(
    -1,
    numpy.asarray(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        ]
    ),
)


def create_tile(tile):
    n, *im = tile.strip().split("\n")
    n = int(n[5:-1])
    im = numpy.asarray([[1 if c == "#" else 0 for c in line] for line in im])
    return Tile(n, im)


with open("../inputs/2020/day20.input", "r") as f:
    data = f.read()
    tiles = list(map(create_tile, data.split("\n\n")))

edge2tiles = defaultdict(set)
for tile in tiles:
    for v in tile.variants:
        for edge in v.edges:
            edge2tiles[edge].add(tile)


def part1(tiles):
    iscorner = lambda tile: sum(len(edge2tiles[e]) for e in tile.edges) == 6
    return reduce(mul, (c.n for c in filter(iscorner, tiles)))


def part2(tiles):
    move = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    seen = set()
    queue = [((0, 0), tiles[0])]
    image = dict(queue)
    # Place tiles on grid
    while queue:
        loc, cur = queue.pop()
        seen.add(cur.n)
        for i, e in enumerate(cur.edges):
            try:
                (new,) = (t for t in edge2tiles[e] if t.n != cur.n)
            except ValueError:
                continue
            if new.n in seen:
                continue
            newloc = tuple(map(add, loc, move[i]))
            (new,) = (v for v in new.variants if v.edges[(i + 2) % 4] == e)
            image[newloc] = new
            queue.append((newloc, new))

    assert len(seen) == len(tiles) == len(image)
    min_ = min(image)
    max_ = max(image)

    # Assemble image
    nx, ny = tuple(map(sub, max_, min_))
    assert nx == ny == int(sqrt(len(tiles))) - 1
    tx, ty = tiles[0].image.shape
    assembled = numpy.empty(((nx + 1) * tx, (ny + 1) * ty), dtype=int)
    for loc, tile in image.items():
        x, y = map(sub, loc, min_)
        assembled[y * ty : (y + 1) * ty, x * tx : (x + 1) * tx] = tile.image[::-1, :]
    # Check for monsters
    N = monster.im.sum()
    return assembled.sum() - N * sum(
        (convolve(assembled, m.im, mode="constant") == N).sum()
        for m in monster.variants
    )


print(f"Part 1: {part1(tiles)}")
print(f"Part 2: {part2(tiles)}")
