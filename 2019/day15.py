from functools import partial

import networkx as nx

from intcode import CPU, load

mem = load("day15.input")


def explore(mem):
    graph = nx.Graph()
    WALL, VALID, OXYGEN = range(3)
    directions = dict(zip((1j, -1j, -1, 1), range(1, 5)))

    def pairs(iterable):
        iterable = iter(iterable)
        a = next(iterable)
        for b in iterable:
            yield (a, b)
            a = b

    def peek(pos, toexplore, graph):
        for d in directions:
            n = pos + d
            if n not in graph:
                toexplore.add(n)
                graph.add_edge(pos, n)
        return pos, toexplore, graph

    def key(pos, p):
        X = pos - p
        return int(abs(X.real) + abs(X.imag))

    pos, toexplore, graph = peek(0, set(), graph)

    output = []
    explorer = CPU(mem)
    while toexplore:
        target = min(toexplore, key=partial(key, pos))
        for cur, target in pairs(nx.shortest_path(graph, source=pos, target=target)):
            explorer.run(../inputs/2019=[directions[target - cur]], outputs=output.append)
            if explorer.halted:
                raise RuntimeError("Halted prematurely")
            status = output.pop()
            toexplore.discard(target)
            if status != WALL:
                pos, toexplore, graph = peek(target, toexplore, graph)
                if status == OXYGEN:
                    oxygen = target
    return graph, oxygen


def part1(mem):
    graph, oxygen = explore(mem)
    return nx.shortest_path_length(graph, 0, oxygen)


def part2(mem):
    graph, oxygen = explore(mem)
    return max(nx.single_source_shortest_path_length(graph, oxygen).values())


print(f"Part 1: {part1(mem)}")
print(f"Part 2: {part2(mem)}")
