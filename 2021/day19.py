import time
from functools import cmp_to_key
from itertools import cycle

import numpy

start = time.time()

rotations = numpy.asarray(
    [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
        [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
        [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
        [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
        [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
        [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
        [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
    ],
    dtype=numpy.int32,
)

transformations = numpy.concatenate(
    [rotations, rotations[..., [1, 2, 0]], rotations[..., [2, 0, 1]]]
)


def msb_less(x, y):
    return x < y and x < (x ^ y)


def z_order(lhs, rhs):
    lhs = lhs.astype(numpy.uint32)
    rhs = rhs.astype(numpy.uint32)
    msd = 1 if msb_less(lhs[0] ^ rhs[0], lhs[1] ^ rhs[1]) else 0
    msd = 2 if msb_less(lhs[msd] ^ rhs[msd], lhs[2] ^ rhs[2]) else msd
    if lhs[msd] < rhs[msd]:
        return -1
    elif lhs[msd] == rhs[msd]:
        return 0
    else:
        return 1


key_z_order = cmp_to_key(z_order)


def sort_coords(coords):
    return numpy.asarray(sorted(coords, key=key_z_order), dtype=numpy.int32)


with open("../inputs/2021/day19.input", "r") as f:
    data = f.read().strip()
    scanners = data.strip().split("\n\n")
    inp = []
    for scanner in scanners:
        scans = scanner.split("\n")[1:]
        coords = []
        for scan in scans:
            scan = list(map(int, scan.split(",")))
            coords.append(scan)
        inp.append(numpy.asarray(coords, dtype=numpy.int32))


def windows(coords):
    return dict(
        (tuple(w1 - w0), i) for i, (w0, w1) in enumerate(zip(coords, coords[1:]))
    )


def solve(inp):
    refscan, *scanners = inp
    positions = [(0, 0, 0)]
    found = set()
    transforms = cycle(transformations)
    unknown = set(range(len(scanners)))
    while unknown:
        transform = next(transforms)
        toremove = set()
        for u in unknown:
            if len(found) != len(refscan):
                refscan = sort_coords(refscan)
                found.update(map(tuple, refscan))
                known_diff = windows(refscan)
            rotated = sort_coords(numpy.einsum("ij,kj->ki", transform, scanners[u]))

            unknown_diff = windows(rotated)
            common = {
                tuple(refscan[known_diff[d]] - rotated[i])
                for d, i in unknown_diff.items()
                if d in known_diff
            }
            for translation in common:
                translated = rotated + translation
                if len([t for t in translated if tuple(t) in found]) >= 12:
                    positions.append(translation)
                    refscan = numpy.unique(
                        numpy.concatenate([refscan, translated]), axis=0
                    )
                    toremove.add(u)
                    break
        unknown -= toremove

    return numpy.asarray(positions), len(refscan)


positions, nbeacon = solve(inp)


def part1(inp):
    return nbeacon


def part2(inp):
    return max(
        numpy.linalg.norm(p1 - p2, ord=1).astype(numpy.uint32)
        for p1 in positions
        for p2 in positions
    )


print(
    f"Day 19     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
