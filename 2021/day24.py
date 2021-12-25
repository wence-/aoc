import time

start = time.time()
with open("../inputs/2021/day24.input", "r") as f:
    data = f.read().strip().split("\n")
    blocklen = 18
    blocks = []
    while data:
        block = data[:blocklen]
        data = data[blocklen:]
        zdiv = int(block[4][5:])
        xadd = int(block[5][5:])
        yadd = int(block[15][5:])
        blocks.append((zdiv, xadd, yadd))
    blocks = tuple(blocks)
    inp = blocks


# Original solution
def block(z, w, zdiv, xadd, yadd):
    if w == z % 26 + xadd:
        return z // zdiv
    else:
        return z // zdiv * 26 + yadd + w


def possible_digits(z, zdiv, xadd, minp):
    if zdiv == 1:
        if minp:
            yield from range(1, 10)
        else:
            if z == 0:
                # Optimisation for our input
                yield 2
            else:
                yield from range(9, 0, -1)
    else:
        if 1 <= (p := z % 26 + xadd) < 10:
            yield p
        else:
            return


def candidates(z, blocks, can, minp):
    if len(blocks) == 0:
        yield can
    else:
        zdiv, xadd, yadd = blocks[0]
        for w in possible_digits(z, zdiv, xadd, minp):
            yield from candidates(
                block(z, w, zdiv, xadd, yadd), blocks[1:], can * 10 + w, minp
            )


def part1_slow(inp):
    return next(candidates(0, inp, 0, False))


def part2_slow(inp):
    return next(candidates(0, inp, 0, True))


def solve(blocks, guess):
    # See explanation here:
    # https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpuu3e0/
    lifo = []
    for i, (zdiv, chk, add) in enumerate(blocks):
        if zdiv == 1:
            lifo.append((i, add))
        if zdiv == 26:
            j, add = lifo.pop()
            guess[i] = guess[j] + add + chk
            if guess[i] > 9:
                guess[j] = guess[j] - (guess[i] - 9)
                guess[i] = 9
            elif guess[i] < 1:
                guess[j] = guess[j] + (1 - guess[i])
                guess[i] = 1
    return "".join(map(str, guess))


def part1(inp):
    return solve(inp, [9] * 14)


def part2(inp):
    return solve(inp, [1] * 14)


print(
    f"Day 24     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
