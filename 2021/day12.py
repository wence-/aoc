from collections import defaultdict

with open("../inputs/2021/day12.input", "r") as f:
    nodes = defaultdict(list)
    lines = f.read().strip().split("\n")
    for line in lines:
        a, b = line.split("-")
        if b != "start":
            nodes[a].append(b)
        if a != "start":
            nodes[b].append(a)


def recurse(head, seen, twice, nodes):
    # Original implementation
    if head == "end":
        return 1
    return sum(
        recurse(c, seen if c.isupper() else (seen | {c}), twice or c in seen, nodes)
        for c in nodes[head]
        if not (twice and c in seen)
    )


def solve(head, twice, nodes):
    # Hand-managed call stack is a bit faster
    npath = 0
    stack = [(head, set(), twice)]
    while stack:
        end, seen, twice = stack.pop()
        if end == "end":
            npath += 1
        else:
            for c in nodes[end]:
                if not (twice and c in seen):
                    if c.isupper():
                        stack.append((c, seen, twice))
                    else:
                        stack.append((c, seen | {c}, twice or c in seen))
    return npath


def part1(nodes):
    return solve("start", True, nodes)


def part2(nodes):
    return solve("start", False, nodes)


print(part1(nodes))
print(part2(nodes))
