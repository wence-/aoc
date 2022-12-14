import time

start = time.time()
with open("../inputs/2022/day10.input") as f:
    data = f.read()
    inp = [
        0 if line == "noop" else int(line.split(" ")[1]) for line in data.split("\n")
    ]


def part1(inp: list) -> int:
    X = 1
    result = 0
    cycle = 1
    check = 20
    for op in inp:
        cycle += 1 + (op != 0)
        if cycle > check:
            result += X * check
            check += 40
        X += op
    return result


ALPHABET = {
    " ## \n#  #\n#  #\n####\n#  #\n#  #": "A",
    "### \n#  #\n### \n#  #\n#  #\n### ": "B",
    " ## \n#  #\n#   \n#   \n#  #\n ## ": "C",
    "####\n#   \n### \n#   \n#   \n####": "E",
    "####\n#   \n### \n#   \n#   \n#   ": "F",
    " ## \n#  #\n#   \n# ##\n#  #\n ###": "G",
    "#  #\n#  #\n####\n#  #\n#  #\n#  #": "H",
    " ###\n  # \n  # \n  # \n  # \n ###": "I",
    "  ##\n   #\n   #\n   #\n#  #\n ## ": "J",
    "#  #\n# # \n##  \n# # \n# # \n#  #": "K",
    "#   \n#   \n#   \n#   \n#   \n####": "L",
    " ## \n#  #\n#  #\n#  #\n#  #\n ## ": "O",
    "### \n#  #\n#  #\n### \n#   \n#   ": "P",
    "### \n#  #\n#  #\n### \n# # \n#  #": "R",
    " ###\n#   \n#   \n ## \n   #\n### ": "S",
    "#  #\n#  #\n#  #\n#  #\n#  #\n ## ": "U",
    "#   \n#   \n # #\n  # \n  # \n  # ": "Y",
    "####\n   #\n  # \n #  \n#   \n####": "Z",
}


def part2(inp: list) -> str:
    W = 40
    H = 6

    result: list[str] = [" "] * (W * H)

    x = 1
    cycle = 0
    for op in inp:
        for _ in range(1 + (op != 0)):
            result[cycle] = " " if abs(x - (cycle % W)) > 1 else "#"
            cycle += 1
        x += op

    return "".join(
        ALPHABET[
            "\n".join(
                "".join(result[W * row + c * 5 : W * row + c * 5 + 4])
                for row in range(H)
            )
        ]
        for c in range(8)
    )


print(
    f"Day 10     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
