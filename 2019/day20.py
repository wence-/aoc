from collections import defaultdict

import networkx as nx

with open("inputs/day20.input", "r") as f:
    data = f.readlines()
    grid = {}
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch not in {"#", " "}:
                grid[x + 1j*y] = ch


def make_graph(data, level=0, graph=None):
    directions = (1, -1, 1j, -1j)
    graph = graph or nx.Graph()
    portals = defaultdict(list)
    for p, ch in grid.items():
        if ch != ".":
            continue
        for d in directions:
            try:
                val = grid[p + d]
            except KeyError:
                continue
            if val == ".":
                graph.add_edge((level, p), (level, p+d))
            else:
                # portal
                for d_ in directions:
                    val_ = grid.get(p + d + d_)
                    if val_ not in {".", None}:
                        key = val + val_ if val < val_ else val_ + val
                        portals[key].append(p)
    return graph, portals


def part1(data):
    graph, portals = make_graph(data)
    for p, v in portals.items():
        if len(v) == 2:
            a, b = v
            graph.add_edge((0, a), (0, b))
        else:
            a, = v
            graph.add_node((0, a))
    AA, = portals["AA"]
    ZZ, = portals["ZZ"]
    return nx.shortest_path_length(graph, (0, AA), (0, ZZ))


def part2(data, maxlevel=30):
    graph, portals = make_graph(data)
    for l in range(1, maxlevel-1):
        graph, _ = make_graph(data, level=l, graph=graph)
    for p, v in portals.items():
        if len(v) == 2:
            a, b = v
            if int(a.real) in {2, 132} or int(a.imag) in {2, 124}:
                outer, inner = a, b
            else:
                outer, inner = b, a
            for l in range(maxlevel-1):
                graph.add_edge((l, inner), (l+1, outer))
        else:
            a, = v
            graph.add_node((0, a))
    AA, = portals["AA"]
    ZZ, = portals["ZZ"]
    return nx.shortest_path_length(graph, (0, AA), (0, ZZ))


print("Part 1:", part1(data))
print("Part 2:", part2(data))
