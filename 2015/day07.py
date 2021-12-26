import time
from collections import defaultdict

start = time.time()
with open("../inputs/2015/07.input", "r") as f:
    lines = f.readlines()

graph = {}

for line in lines:
    line = line.strip()
    s = line.find("->")
    out = line[s + 3 :]
    arg = line[: s - 1].split(" ")
    graph[out] = tuple(arg)

assert len(graph) == len(lines)


def topo_sort(graph):
    def deps(arg):
        return tuple(
            a
            for a in arg
            if not (a.isdigit() or a in {"NOT", "OR", "RSHIFT", "AND", "LSHIFT"})
        )

    fdeps = dict((k, list(deps(v))) for k, v in graph.items())
    rdeps = defaultdict(set)
    for n, arg in fdeps.items():
        for dep in deps(arg):
            rdeps[dep].add(n)

    L = []
    S = list(n for n, arg in fdeps.items() if len(deps(arg)) == 0)
    while S:
        S = sorted(S, reverse=True)
        n = S.pop()
        L.append(n)
        for m in rdeps[n]:
            fdeps[m].remove(n)
            if not fdeps[m]:
                S.append(m)
    return L


order = topo_sort(graph)

values = {}


def get(n, values):
    if n.isdigit():
        return int(n) % 65536
    else:
        return values[n]


for node in order:
    deps = graph[node]
    if len(deps) == 1:
        values[node] = get(deps[0], values)
    elif deps[0] == "NOT":
        values[node] = (~get(deps[1], values)) % 65536
    else:
        x, op, y = deps
        x = get(x, values)
        y = get(y, values)
        if op == "OR":
            values[node] = (x | y) % 65536
        elif op == "AND":
            values[node] = (x & y) % 65536
        elif op == "LSHIFT":
            values[node] = (x << y) % 65536
        elif op == "RSHIFT":
            values[node] = (x >> y) % 65536
        else:
            raise ValueError


part1 = values["a"]

vb = {}

for node in order:
    deps = graph[node]
    if len(deps) == 1:
        if node == "b":
            vb[node] = values["a"]
        else:
            vb[node] = get(deps[0], vb)
    elif deps[0] == "NOT":
        vb[node] = (~get(deps[1], vb)) % 65536
    else:
        x, op, y = deps
        x = get(x, vb)
        y = get(y, vb)
        if op == "OR":
            vb[node] = (x | y) % 65536
        elif op == "AND":
            vb[node] = (x & y) % 65536
        elif op == "LSHIFT":
            vb[node] = (x << y) % 65536
        elif op == "RSHIFT":
            vb[node] = (x >> y) % 65536
        else:
            raise ValueError

part2 = vb["a"]

print(f"Day 07     {part1:<14} {part2:<14} {(time.time() - start)*1e3:>11.2f}")
