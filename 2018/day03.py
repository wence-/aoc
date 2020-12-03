import numpy


class Patch(object):
    def __init__(self, string):
        id_, _, coords, area = string.split()
        self.id_ = int(id_[1:])
        self.coords = tuple(map(int, coords[:-1].split(",")))
        self.area = tuple(map(int, area.split("x")))


with open("inputs/day03.input", "r") as f:
    patches = list(map(Patch, f.readlines()))


shape = (1000, 1000)
claims = numpy.zeros(shape, dtype=int)

for patch in patches:
    x, y = patch.coords
    a, b = patch.area
    claims[x:x+a, (1000 - y - b):(1000 - y)] += 1


print(f"Part 1: {numpy.sum(claims > 1)}")

for patch in patches:
    x, y = patch.coords
    a, b = patch.area
    claim = claims[x:x+a, (1000 - y - b):(1000 - y)]
    if numpy.sum(claim) == a*b:
        print(f"Part 2: {patch.id_}")
        break
