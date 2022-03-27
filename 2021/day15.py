import heapq
import time

start = time.time()

with open("../inputs/2021/day15.input", "r") as f:
    data = f.read().strip()
    inp = []
    for line in data.split("\n"):
        inp.append(list(map(int, line)))


DI = [1, 0, -1, 0]
DJ = [0, 1, 0, -1]


def neighbours(i, j, N, M):
    for di, dj in zip(DI, DJ):
        i_ = i + di
        j_ = j + dj
        if 0 <= i_ < N and 0 <= j_ < M:
            yield (i_, j_)


def d2(start, end, graph):
    N, M = len(graph), len(graph[0])
    dist = [[False] * M for _ in range(N)]
    Q = [[] for _ in range(10)]
    qi = 0
    Q[0].append(start)
    while True:
        Q[9].clear()
        Q[qi % 9], Q[9] = Q[9], Q[qi % 9]
        for vi, vj in Q[9]:
            if dist[vi][vj]:
                continue
            if (vi, vj) == end:
                return qi
            dist[vi][vj] = True
            for ui, uj in neighbours(vi, vj, N, M):
                if dist[ui][uj]:
                    continue
                Q[(qi + graph[ui][uj]) % 9].append((ui, uj))
        qi += 1


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
        for ui, uj in neighbours(vi, vj, N, M):
            if not seen[ui][uj]:
                seen[ui][uj] = True
                heapq.heappush(pq, (d + graph[ui][uj], (ui, uj)))


def part1(graph):
    start = (0, 0)
    end = len(graph) - 1, len(graph[0]) - 1
    return d2(start, end, graph)


def replicate(graph):
    nx, ny = len(graph), len(graph[0])
    return [
        [(graph[i % nx][j % ny] + i // nx + j // ny - 1) % 9 + 1 for j in range(ny * 5)]
        for i in range(nx * 5)
    ]


def part2(graph):
    start = (0, 0)
    graph = replicate(graph)
    end = len(graph) - 1, len(graph[0]) - 1
    return d2(start, end, graph)


print(
    f"Day 15     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
