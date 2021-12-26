from itertools import count

import numpy

positions = numpy.asarray(
    [[-7, 17, -11], [9, 12, 5], [-9, 0, -4], [4, 6, 0]], dtype=int
)


def part1(positions):
    positions = positions.copy()
    reshaped = positions.reshape(-1, 1, 3)
    velocities = numpy.zeros_like(positions)

    for _ in range(1000):
        dx = numpy.sign(positions - reshaped)
        dx = numpy.sum(dx, axis=1)
        velocities += dx
        positions += velocities

    pe = numpy.sum(numpy.abs(positions), axis=1)
    ke = numpy.sum(numpy.abs(velocities), axis=1)
    return numpy.sum(pe * ke)


def part2(positions):
    positions = positions.copy()
    reshaped = positions.reshape(-1, 1, 3)
    velocities = numpy.zeros_like(positions)

    cycle = numpy.full(3, -1)
    oldp = positions.copy()
    oldv = velocities.copy()
    for i in count(1):
        dx = numpy.sign(positions - reshaped)
        dx = numpy.sum(dx, axis=1)
        velocities += dx
        positions += velocities
        for j in range(3):
            if (positions[:, j] == oldp[:, j]).all() and (
                velocities[:, j] == oldv[:, j]
            ).all():
                cycle[j] = i
        if (cycle != -1).all():
            break
    return numpy.lcm.reduce(cycle)


print(f"Part 1: {part1(positions)}")
print(f"Part 2: {part2(positions)}")
