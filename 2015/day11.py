invalid_chars = frozenset([c - ord('a') for c in map(ord, "iol")])


def next_(password):
    rev = list(reversed(password))
    carry = 0

    carry, p = divmod(rev[0] + 1, 26)
    rev[0] = p
    i = 1
    while carry:
        carry, p = divmod(rev[i] + carry, 26)
        rev[i] = p
        i += 1

    n = len(rev)
    res = []
    for i, c in enumerate(reversed(rev)):
        if c in invalid_chars:
            res.append(c + 1)
            for _ in range(i+1, n):
                res.append(0)
            break
        else:
            res.append(c)
    return res


def valid(password):
    if not any(a + 1 == b and b + 1 == c
               for a, b, c in zip(password, password[1:], password[2:])):
        return False
    pairs = set((a, b) for a, b in zip(password, password[1:]) if a == b)
    if len(pairs) < 2:
        return False
    return True


def p(password):
    return "".join(chr(c + ord('a')) for c in password)


start = "cqjxjnds"
chars = [c - ord('a') for c in map(ord, start)]
while not valid(chars):
    chars = next_(chars)

print("Part 1:", p(chars))

chars = next_(chars)
while not valid(chars):
    chars = next_(chars)

print("Part 2:", p(chars))
