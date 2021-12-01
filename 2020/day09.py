from more_itertools import windowed

with open("../inputs/2020/day09.input", "r") as f:
    data = list(map(int, f.readlines()))


def part1(data, window_size=25):
    return next(want for want, have in
                zip(data[window_size:], map(set, windowed(data, window_size)))
                if not any(want - h in have for h in have))


def part2(data, want):
    data = data[:data.index(want)]
    left = 0
    right = 0
    subseq_sum = 0
    for right, n in enumerate(data):
        while subseq_sum > want and left < right:
            subseq_sum -= data[left]
            left += 1
        if subseq_sum == want:
            subseq = data[left:right]
            return min(subseq) + max(subseq)
        subseq_sum += n
    raise RuntimeError("")


want = part1(data)
print(f"Part 1: {want}")
print(f"Part 2: {part2(data, want)}")
