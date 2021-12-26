import time

start = time.time()
with open("../inputs/2015/14.input", "r") as f:
    data = f.readlines()

mapping = {}
for line in data:
    name, _, _, speed, _, _, t, *_, rest, _ = line.split()
    mapping[name] = tuple(map(int, (speed, t, rest)))


def dist(name, time):
    speed, duration, rest = mapping[name]
    n, r = divmod(time, duration + rest)
    return (n * duration + min(duration, r)) * speed


part1 = max(dist(name, 2503) for name in mapping)


def sim(mapping, time):
    score = dict((n, 0) for n in mapping)
    dist = dict((n, 0) for n in mapping)
    for i in range(time):
        for n, (speed, time, rest) in mapping.items():
            if divmod(i, time + rest)[1] < time:
                dist[n] += speed
        maxdist = max(dist.values())
        for n, d in dist.items():
            if d == maxdist:
                score[n] += 1
    return score


part2 = max(sim(mapping, 2503).values())

print(f"Day 14     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
