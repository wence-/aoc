import time
from typing import Generic, Iterable, TypeVar

start = time.time()


with open("../inputs/2022/day20.input") as f:
    inp = list(map(int, f.read().split("\n")))

T = TypeVar("T")


class BucketList(Generic[T]):
    def __init__(self, bucket_size, data: Iterable[T]):
        self.bucket_size = bucket_size
        self.buckets = [[]]
        self.location = {}
        for d in data:
            self.add(d)

    def add(self, v: T):
        n = len(self.buckets) - 1
        bucket = self.buckets[n]
        if len(bucket) == self.bucket_size:
            bucket = []
            self.buckets.append(bucket)
            n += 1
        self.location[v] = n
        self.buckets[n].append(v)

    def shift(self, v: T, offset: int):
        b = self.location[v]
        offset += self.buckets[b].index(v)
        self.buckets[b].remove(v)
        while offset > (n := len(self.buckets[b])):
            offset -= n
            b = (b + 1) % len(self.buckets)
        self.buckets[b].insert(offset, v)
        self.location[v] = b

    def index(self, v: T) -> int:
        b = self.location[v]
        pos = self.buckets[b].index(v)
        pos += sum(len(self.buckets[i]) for i in range(b))
        return pos

    def __getitem__(self, i: int) -> T:
        b = 0
        while (i := i - len(self.buckets[b])) >= 0:
            b += 1
        return self.buckets[b][i]


def solve(inp: list[int], multiplier: int, rounds: int):
    zero = (inp.index(0), 0)
    data = [(i, n * multiplier) for i, n in enumerate(inp)]
    buckets = BucketList(128, data)
    N = len(data)
    for _ in range(rounds):
        for d in data:
            buckets.shift(d, d[1] % (N - 1))

    return sum((buckets[(buckets.index(zero) + i * 1000) % N][1] for i in range(1, 4)))


def part1(inp: list) -> int:
    return solve(inp, 1, 1)


def part2(inp: list) -> int:
    return solve(inp, 811589153, 10)


print(
    f"Day 20     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
