import collections

with open("../inputs/2019/day18.input", "r") as f:
    dataa = f.readlines()

with open("../inputs/2019/day18b.input", "r") as f:
    datab = f.readlines()


def reachablekeys(grid, start, havekeys):
    bfs = collections.deque([(start, 0)])
    seen = {start}
    keys = {}
    while bfs:
        h, dist = bfs.popleft()
        for pt in [h + 1, h - 1, h + 1j, h - 1j]:
            if pt not in grid:
                continue
            ch = grid[pt]
            if ch == '#':
                continue
            if pt in seen:
                continue
            seen.add(pt)
            if 'A' <= ch <= 'Z' and ch.lower() not in havekeys:
                continue
            if 'a' <= ch <= 'z' and ch not in havekeys:
                keys[ch] = dist + 1, pt
            else:
                bfs.append((pt, dist + 1))
    return keys


def reachable(grid, starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in reachablekeys(grid, start, havekeys).items():
            keys[ch] = dist, pt, i
    return keys


def minwalk(grid, starts, havekeys, cache):
    havekeys = frozenset(havekeys)
    try:
        return cache[starts, havekeys]
    except KeyError:
        pass
    keys = reachable(grid, starts, havekeys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else p
                            for i, p in enumerate(starts))
            poss.append(dist + minwalk(grid, nstarts, havekeys | {ch}, cache))
        ans = min(poss)
    return cache.setdefault((starts, havekeys), ans)


def part1(data):
    grid = dict((i + 1j*j, ch) for j, line in enumerate(data)
                for i, ch in enumerate(line))
    starts = tuple(k for k, v in grid.items() if v == "@")
    return minwalk(grid, tuple(starts), frozenset(), {})


def part2(data):
    grid = dict((i + 1j*j, ch) for j, line in enumerate(data)
                for i, ch in enumerate(line))
    starts = tuple(k for k, v in grid.items() if v == "@")
    return minwalk(grid, tuple(starts), frozenset(), {})


print("Part 1:", part1(dataa))
print("Part 2:", part1(datab))
