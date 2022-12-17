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
def paths(node):
    q = deque([(0, node)])
    ret = {}
    while q:
        d, n = q.popleft()
        for dest in inp[n][1]:
            if dest not in ret:
                ret[dest] = d + 2
                q.append((d + 1, dest))
    return {n: t for n, t in ret.items() if inp[n][0] > 0}


def part1(inp: dict) -> int:
    # For pruning
    best = 0

    def search(current, time_left, enabled, node):
        """Worker at node with time_left time, and a set of enabled
        nodes, with current best guess for score"""
        nonlocal best
        benefit = current
        for dst, cur_time in paths(node).items():
            if dst not in enabled and cur_time <= time_left:
                new_time = time_left - cur_time
                new = current + new_time * inp[dst][0]
                prunep = new_time * 47  # magic number for A* pruning
                if new + prunep < best:
                    continue
                candidate = search(new, new_time, enabled | {dst}, dst)
                benefit = max(benefit, candidate)
        best = max(best, benefit)
        return benefit

    return search(0, 30, set(), "AA")


def part2(inp: dict) -> int:
    # For pruning
    best = 0

    # Could merge with part1 search, but meh
    def search(cur_benefit, time_left, enabled, me, you, you_budget):
        nonlocal best
        benefit = cur_benefit
        for dst, cur_time in paths(me).items():
            if dst not in enabled and cur_time <= time_left:
                if you_budget < cur_time:
                    new_me = you
                    new_you = dst
                    new_time_left = time_left - you_budget
                    new_budget = cur_time - you_budget
                else:
                    new_me = dst
                    new_you = you
                    new_time_left = time_left - cur_time
                    new_budget = you_budget - cur_time
                new = cur_benefit + (time_left - cur_time) * inp[dst][0]
                # magic number for A-* pruning
                prunep = (time_left - cur_time - you_budget) * 78
                if new + prunep < best:
                    continue
                candidate = search(
                    new,
                    new_time_left,
                    enabled | {dst},
                    new_me,
                    new_you,
                    new_budget,
                )
                benefit = max(benefit, candidate)
        best = max(best, benefit)
        return benefit

    return search(0, 26, set(), "AA", "AA", 0)


print(
    f"Day 16     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
