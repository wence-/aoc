from functools import partial

numbers = list(map(../int/2020, "7,12,1,0,16,2".split(",")))
assert len(set(numbers)) == len(numbers)


def run(numbers, N):
    spoken = [0 for _ in range(N)]
    for i, n in enumerate(numbers):
        spoken[n] = i + 1
        last = n
    for i in range(len(numbers), N):
        cur = spoken[last]
        spoken[last] = i
        last = 0 if cur == 0 else i - cur
    return last


part1 = partial(run, N=2020)
part2 = partial(run, N=30_000_000)


print(f"Part 1: {part1(numbers)}")
print(f"Part 2: {part2(numbers)}")
