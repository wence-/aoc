import math
from collections import defaultdict

with open("../inputs/2019/day14.input", "r") as f:
    data = f.read().strip().split("\n")


def setup(data):
    graph = defaultdict(list)
    for line in data:
        in_, out_ = line.strip().split("=")
        inputs = in_.strip().split(",")
        out_ = out_[2:]
        out = out_.split(" ")
        nout = int(out[0])
        out = str(out[1])
        for in_ in inputs:
            in_ = in_.strip().split(" ")
            nin = int(in_[0])
            in_ = in_[1]
            graph[out].append((in_, nin))
        graph[out].append(nout)
    return graph


def ore(n, graph):
    substances = defaultdict(int, [("FUEL", n)])
    while True:
        try:
            need, n = next(
                (e, n) for e, n in substances.items() if n > 0 and e != "ORE"
            )
        except StopIteration:
            break
        *reqs, makes = graph[need]
        full = math.ceil(n / makes)
        for r, v in reqs:
            substances[r] += v * full
        substances[need] -= full * makes
    return substances["ORE"]


def part1(data):
    graph = setup(data)
    return ore(1, graph)


def part2(data, target=10 ** 12):
    graph = setup(data)
    fuel = 1
    while True:
        made = ore(fuel + 1, graph)
        if made > target:
            return fuel
        else:
            fuel = max(fuel + 1, (fuel + 1) * target // made)


print("Part 1:", part1(data))
print("Part 2:", part2(data))
