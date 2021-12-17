import heapq
import time

start = time.time()
with open("../inputs/2021/day15.input", "r") as f:
    data = f.read().strip()
    inp = []
    for line in data.split("\n"):
        inp.append(list(map(int, line)))


def neighbours(i, j, graph):
    N, M = len(graph), len(graph[0])
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    for n in range(4):
        i_ = i + di[n]
        j_ = j + dj[n]
        if 0 <= i_ < N and 0 <= j_ < M:
            yield (i_, j_)


def dijkstra(start, end, graph):
    N, M = len(graph), len(graph[0])
    dist = [[False] * M for _ in range(N)]
    pq = []
    seen = [[False] * M for _ in range(N)]
    i, j = start
    seen[i][j] = True
    heapq.heappush(pq, (1, start))
    while pq:
        d, (vi, vj) = heapq.heappop(pq)
        if dist[vi][vj]:
            continue  # already searched this node.
        if (vi, vj) == end:
            return d - 1
        dist[vi][vj] = d
        for ui, uj in neighbours(vi, vj, graph):
            if not seen[ui][uj]:
                seen[ui][uj] = True
                heapq.heappush(pq, (d + graph[ui][uj], (ui, uj)))


def part1(graph):
    start = (0, 0)
    end = len(graph) - 1, len(graph[0]) - 1
    return dijkstra(start, end, graph)


def replicate(graph):
    nx, ny = len(graph), len(graph[0])

    newgraph = [[None] * ny * 5 for _ in range(nx * 5)]
    for ki in range(nx):
        for kj in range(ny):
            v = graph[ki][kj]
            for i in range(0, 5):
                for j in range(0, 5):
                    kx = ki + i * nx
                    ky = kj + j * ny
                    newval = v + i + j
                    if newval > 9:
                        newval = newval % 9
                    newgraph[kx][ky] = newval
    return newgraph


def part2(graph):
    start = (0, 0)
    graph = replicate(graph)
    end = len(graph) - 1, len(graph[0]) - 1
    return dijkstra(start, end, graph)


print(
    f"Day 15     {part1(inp):<13} {part2(inp):<14} {(time.time() - start)*1e6:>13.0f}"
)
