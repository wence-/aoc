with open("inputs/14.input", "r") as f:
    data = f.readlines()

mapping = {}
for line in data:
    name, _, _, speed, _, _, time, *_, rest, _ = line.split()
    mapping[name] = tuple(map(int, (speed, time, rest)))


def dist(name, time):
    speed, duration, rest = mapping[name]
    n, r = divmod(time, duration + rest)
    return (n*duration + min(duration, r))*speed


print("Part 1:", max(dist(name, 2503) for name in mapping))


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


print("Part 2:", max(sim(mapping, 2503).values()))
