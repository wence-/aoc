import time

start = time.time()
with open("../inputs/2021/day13.input", "r") as f:
    coords, folds = f.read().strip().split("\n\n")
    coords = [list(map(int, line.split(","))) for line in coords.split("\n")]
    folds = [(int(fold[11] == "y"), int(fold[13:])) for fold in folds.split("\n")]
    inp = (coords, folds)


def solve(coords, folds):
    points = {}
    comp, n = folds[0]
    for coord in coords:
        for comp, n in folds:
            p = coord[comp]
            coord[comp] = p if p < n else p - 2 * (p - n)
        points[tuple(coord)] = "#"
    return points


def part1(inp):
    coords, folds = inp
    return len(solve(coords, folds[:1]))


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


def part2(inp):
    coords, folds = inp
    points = solve(coords, folds)
    width = 4
    chars = []
    for c in range(8):
        char = "\n".join(
            "".join(
                points.get((i, j), " ")
                for i in range(c * (width + 1), c * (width + 1) + width)
            )
            for j in range(6)
        )
        chars.append(ALPHABET[char])
    return "".join(chars)


print(
    f"Day 13     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
