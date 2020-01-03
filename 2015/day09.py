from itertools import permutations

distances = {}
with open("inputs/09.input", "r") as f:
    for line in f.readlines():
        (source, _, dest, _, distance) = line.split()
        distances[source, dest] = int(distance)
        distances[dest, source] = int(distance)

distances = list(sum(map(distances.__getitem__, zip(path, path[1:])))
                 for path in permutations(set(x for x, _ in distances)))
shortest = min(distances)
longest = max(distances)
print("Part 1:", shortest)
print("Part 2:", longest)
