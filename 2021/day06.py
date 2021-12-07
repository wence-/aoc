from collections import deque

with open("../inputs/2021/day06.input", "r") as f:
    ages = list(map(int, f.read().strip().split(",")))


def solve(ages, rounds):
    fish = deque([0] * 9, maxlen=9)
    for a in ages:
        fish[a] += 1
    for _ in range(rounds):
        fish.rotate(-1)
        fish[6] += fish[8]
    return sum(fish)


print(solve(ages, 80))
print(solve(ages, 256))
