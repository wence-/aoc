import networkx as nx

with open("inputs/day06.input", "r") as f:
    data = f.readlines()


def part1(data):
    graph = nx.Graph()
    graph.add_edges_from([tuple(line.strip().split(")")) for line in data])
    return sum(nx.single_source_shortest_path_length(graph, 'COM').values())


def part2(data):
    graph = nx.Graph()
    graph.add_edges_from([tuple(line.strip().split(")")) for line in data])
    return nx.shortest_path_length(graph, source='YOU', target='SAN') - 2


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
