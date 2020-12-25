from functools import cached_property
from math import sqrt

import numpy
from scipy.ndimage import convolve


class Tile:
    def __init__(self, n, image):
        self.n = n
        self.im = image
        self.top = sum(2**i * n for i, n in enumerate(image[0, :]))
        self.bottom = sum(2**i * n for i, n in enumerate(image[-1, :]))
        self.left = sum(2**i * n for i, n in enumerate(image[:, 0]))
        self.right = sum(2**i * n for i, n in enumerate(image[:, -1]))

    @cached_property
    def edges(self):
        return (self.top, self.right, self.bottom, self.left)

    def __hash__(self):
        return self.n

    @cached_property
    def image(self):
        return self.im[1:-1, 1:-1]

    @cached_property
    def variants(self):
        v = [self]
        for k in range(1, 4):
            v.append(self._rotate(k))
        v.append(self.flip)
        for k in range(1, 4):
            v.append(self.flip._rotate(k))
        return tuple(v)

    def _rotate(self, k=1):
        return Tile(self.n, numpy.rot90(self.im, k=k))

    @cached_property
    def flip(self):
        return Tile(self.n, self.im[::-1, :])


def create_tile(tile):
    n, *im = tile.strip().split("\n")
    n = int(n[5:-1])
    im = numpy.asarray([[1 if c == "#" else 0 for c in line]
                        for line in im])
    return Tile(n, im)


with open("inputs/day20.input", "r") as f:
    tiles = list(map(create_tile, f.read().split("\n\n")))


def fits(image, tile, size=12):
    N = len(image)
    if N + 1 - size > 0:
        if tile.top != image[N - size].bottom:
            return False
    if (N + 1) % size != 1:
        if tile.left != image[N - 1].right:
            return False
    return True


def assemble(image, seen, tiles, size=12):
    if len(image) == len(tiles):
        return image
    for tile in tiles:
        if tile not in seen:
            for variant in tile.variants:
                if fits(image, variant, size=size):
                    result = assemble(image + [variant], seen | {tile},
                                      tiles, size=size)
                    if result:
                        return result


N = int(sqrt(len(tiles)))
image = assemble([], set(), tiles, size=N)
image = numpy.asarray(image).reshape(N, N)


def part1(image):
    return image[0, 0].n * image[-1, 0].n * image[0, -1].n * image[-1, -1].n


def part2(image):
    X, _ = image.shape
    image = numpy.vstack([numpy.hstack([t.image for t in image[i, :]])
                          for i in range(X)])
    monster = Tile(-1, numpy.asarray([[1 if c == "#" else 0
                                       for c in line.strip()]
                                      for line in r"""
                                      ..................#.
                                      #....##....##....###
                                      .#..#..#..#..#..#...
                                      """.strip().split("\n")]))

    N = monster.im.sum()
    return image.sum() - sum((convolve(image, m.im, mode="constant") == N).sum()
                             for m in monster.variants)*N


print(f"Part 1: {part1(image)}")
print(f"Part 2: {part2(image)}")
