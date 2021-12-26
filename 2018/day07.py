from collections import defaultdict

with open("../inputs/2018/day07.input", "r") as f:
    input = f.readlines()


graph = defaultdict(set)

nodes = set()
for line in input:
    dep = line[5:6]
    node = line[36:37]
    nodes.add(dep)
    nodes.add(node)
    graph[node].add(dep)

for n in nodes:
    graph.setdefault(n, set())


def topo_sort(graph):
    fdeps = dict((k, v.copy()) for k, v in graph.items())
    rdeps = defaultdict(set)
    for n, deps in fdeps.items():
        for dep in deps:
            rdeps[dep].add(n)
    L = []
    S = list(n for n, deps in fdeps.items() if not deps)
    while S:
        S = sorted(S, reverse=True)
        n = S.pop()
        L.append(n)
        for m in rdeps[n]:
            fdeps[m].remove(n)
            if not fdeps[m]:
                S.append(m)
    return L


print(f"Part 1: {''.join(topo_sort(graph))}")


def topo_sort_time(graph, nworker=5):
    fdeps = dict((k, v.copy()) for k, v in graph.items())
    rdeps = defaultdict(set)
    for n, deps in fdeps.items():
        for dep in deps:
            rdeps[dep].add(n)
    L = []
    S = list(n for n, deps in fdeps.items() if not deps)
    time = 0

    cost = dict((n, 60 + ord(n) - ord("A") + 1) for n in graph)
    while S:
        S_ = sorted(S, key=lambda x: (cost[x], x))
        for _, n in zip(range(nworker), S_):
            cost[n] -= 1
            if cost[n] == 0:
                S.remove(n)
                L.append(n)
                for m in rdeps[n]:
                    fdeps[m].remove(n)
                    if not fdeps[m]:
                        S.append(m)
        time += 1
    return time


print(f"Part 2: {topo_sort_time(graph, nworker=5)}")
