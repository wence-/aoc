from itertools import permutations

from intcode import evaluate, load


def power(mem, phases):
    out = None

    def go(amp):
        # First input is always the phase
        assert amp >= 0
        yield phases[amp]
        if amp == 0:
            # First amplifier gets input 0 to start off
            yield 0
            while True:
                # Then the final output
                yield out
        else:
            # Next amplifier just evaluates with ../inputs/2019 from
            # lower-numbered amplifier
            yield from evaluate(mem, inputs=go(amp - 1))

    # Ugly part: need to bind the output here.
    for out in evaluate(mem, inputs=go(len(phases) - 1)):
        pass
    return out


mem = load("day07.input")


def part1(mem):
    return max(power(mem, phases) for phases in permutations(range(5)))


def part2(mem):
    return max(power(mem, phases) for phases in permutations(range(5, 10)))


print(f"Part 1: {part1(mem)}")
print(f"Part 2: {part2(mem)}")
