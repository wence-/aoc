from typing import Optional

with open("../inputs/2021/day10.input", "r") as f:
    lines = f.read().strip().split("\n")


match = {"(": ")", "{": "}", "[": "]", "<": ">"}
score1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score2 = {"(": "1", "[": "2", "{": "3", "<": "4"}


def check(line: str) -> tuple[Optional[int], int]:
    lifo: list[str] = []
    for c in line:
        if c in match:
            lifo.append(c)
        elif not lifo or match[lifo.pop()] != c:
            return score1[c], 0
    return None, int("".join(score2[c] for c in reversed(lifo)), 5)


def part1(lines):
    return sum(c for c, _ in map(check, lines) if c is not None)


def part2(lines):
    scores = [score for c, score in map(check, lines) if c is None]
    return sorted(scores)[len(scores) // 2]


print(part1(lines))
print(part2(lines))
