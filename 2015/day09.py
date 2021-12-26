import time
from itertools import permutations

distances = {}
start = time.time()
with open("../inputs/2015/09.input", "r") as f:
    for line in f.readlines():
        (source, _, dest, _, distance) = line.split()
        distances[source, dest] = int(distance)
        distances[dest, source] = int(distance)

distances = list(
    sum(map(distances.__getitem__, zip(path, path[1:])))
    for path in permutations(set(x for x, _ in distances))
)
part1 = min(distances)
part2 = max(distances)

print(f"Day 09     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
