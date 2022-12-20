import time
from collections import deque
from functools import cache

start = time.time()
with open("../inputs/2022/day16.input") as f:
    inp = {}
    for line in f.read().split("\n"):
        src = line[6:8]
        a, b = line.split("; ")
        rate = int(a[23:])
        edges = b[22:].split(",")
        inp[src] = (rate, list(s.strip() for s in edges))


@cache
def paths(node: str) -> dict[str, int]:
    q: deque[tuple[int, str]] = deque([(0, node)])
    ret = {}
    while q:
        d, n = q.popleft()
        for dest in inp[n][1]:
            if dest not in ret:
                ret[dest] = d + 2
                q.append((d + 1, dest))
    return {n: t for n, t in ret.items() if inp[n][0] > 0}


def part1(inp: dict) -> int:
    def search(node: str, best: int, current: int, time_left: int, enabled: set[str]):
        score = current
        for dst, cur_time in paths(node).items():
            if dst in enabled or cur_time > time_left:
                continue
            new_time = time_left - cur_time
            new_score = current + new_time * inp[dst][0]
            # magic number for A-* pruning
            if new_score + new_time * 47 < best:
                continue
            candidate, best = search(dst, best, new_score, new_time, enabled | {dst})
            score = max(score, candidate)
        return score, max(best, score)

    return search("AA", 0, 0, 30, set())[0]


def part2(inp: dict) -> int:
    # Could merge with part1 search, but meh
    def search(
        me: str,
        you: str,
        best: int,
        current: int,
        time_left: int,
        enabled: set[str],
        budget: int,
    ):
        score = current
        for dst, cur_time in paths(me).items():
            if dst in enabled or cur_time > time_left:
                continue
            if budget < cur_time:
                new_me = you
                new_you = dst
                new_time_left = time_left - budget
                new_budget = cur_time - budget
            else:
                new_me = dst
                new_you = you
                new_time_left = time_left - cur_time
                new_budget = budget - cur_time
            new = current + (time_left - cur_time) * inp[dst][0]
            # magic number for A-* pruning
            if new + (time_left - cur_time - budget) * 78 < best:
                continue
            candidate, best = search(
                new_me,
                new_you,
                best,
                new,
                new_time_left,
                enabled | {dst},
                new_budget,
            )
            score = max(score, candidate)
        return score, max(best, score)

    return search("AA", "AA", 0, 0, 26, set(), 0)[0]


print(
    f"Day 16     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
