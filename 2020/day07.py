import re
from collections import defaultdict

graph = defaultdict(list)
invgraph = defaultdict(set)
with open("../inputs/2020/day07.input", "r") as f:
    for line in f:
        colour, = re.match(r"(.+?) bags contain", line).groups()
        for n, inner in re.findall(r"(\d+) (.+?) bags?[,.]", line):
            graph[colour].append((inner, int(n)))
            invgraph[inner].add(colour)


def part1(invgraph):
    seen = set()
    lifo = ["shiny gold"]
    while lifo:
        top = lifo.pop()
        for c in invgraph[top]:
            seen.add(c)
            lifo.append(c)
    return len(seen)


def part2(graph):
    n = 0
    lifo = [("shiny gold", 1)]
    while lifo:
        top, b = lifo.pop()
        n += b
        for (k, w) in graph[top]:
            lifo.append((k, w*b))
    return n-1


print(f"Part 1: {part1(invgraph)}")
print(f"Part 2: {part2(graph)}")
