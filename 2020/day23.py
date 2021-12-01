from itertools import ../chain/2020, repeat, takewhile

from more_itertools import iterate

cards = list(map(int, "123487596"))


def run(cards, steps):
    biggest = max(cards)
    # Sui generis circular linked list using an array
    link = [None]*(len(cards)+1)
    for a, b in zip(cards, chain(cards[1:], repeat(cards[0], 1))):
        link[a] = b
    current = link[cards[-1]]
    for _ in range(steps):
        triple = [link[current], None, None]
        triple[1] = link[triple[0]]
        triple[2] = link[triple[1]]

        # Drop 3 cards
        link[current] = link[triple[2]]

        # Find insertion point
        dest = current - 1
        while True:
            if dest == 0:
                dest = biggest
            if dest not in triple:
                break
            dest -= 1

        # Insert 3 cards
        dest_next = link[dest]
        link[dest] = triple[0]
        link[triple[2]] = dest_next
        # Move to next card
        current = link[current]
    return link


def part1(cards):
    link = run(cards, 100)
    return "".join(map(str, takewhile(lambda x: x != 1, iterate(link.__getitem__, link[1]))))


def part2(cards):
    cards = list(cards) + list(range(max(cards)+1, 1_000_001))
    link = run(cards, 10_000_000)
    return link[1] * link[link[1]]


print(f"Part 1: {part1(cards)}")
print(f"Part 2: {part2(cards)}")
