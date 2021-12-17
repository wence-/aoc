modulus = 20201227
cardpub = 11562782
doorpub = 18108497


def part1():
    e, n = 0, 1
    while n != doorpub:
        e += 1
        n = 7*n % modulus
    return pow(cardpub, e, modulus)


print(f"Part 1: {part1()}")
