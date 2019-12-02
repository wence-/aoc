from functools import reduce
from operator import mul

import numpy

with open("inputs/day08.input", "r") as f:
    image = numpy.asarray(list(map(int, f.read().strip()))).reshape(-1, 6*25)


def part1(image):
    m = numpy.argmin(numpy.count_nonzero(image == 0, axis=1))
    x = image[m, ...]
    return reduce(mul, (numpy.count_nonzero(x == i) for i in [1, 2]))


def part2(image):
    combined = numpy.asarray([reduce(lambda a, b: b if a == 2 else a, row)
                              for row in image.T]).reshape(6, 25)
    return "\n".join("".join("█" if r else " " for r in row)
                     for row in combined)


print(f"Part 1: {part1(image)}")
print(f"Part 2: \n{part2(image)}")
