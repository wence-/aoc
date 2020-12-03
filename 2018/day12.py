import numpy

with open("inputs/day12.input", "r") as f:
    state_ = f.readline()[14:].strip()
    f.readline()
    rules_ = f.readlines()

state = numpy.asarray([0, 0, 0, 0] + [1 if c == "#" else 0 for c in state_] + [0, 0, 0, 0], dtype=int)
rules = {}
for r in rules_:
    rules[tuple([1 if c == "#" else 0 for c in r[:5]])] = 1 if r[9] == "#" else 0


def print_state(state):
    print("".join("#" if s else "." for s in state))


offset = 4

for i in range(20):
    new_state = numpy.zeros(state.shape, dtype=int)
    for x in range(2, len(state)-2):
        new_state[x] = rules.get(tuple(state[x-2:x+3]), 0)
    if new_state[0] or new_state[1] or new_state[3]:
        new_state = numpy.concatenate([[0, 0, 0, 0], new_state])
        offset += 4
    if new_state[-1] or new_state[-2] or new_state[-3]:
        new_state = numpy.concatenate([new_state, [0, 0, 0, 0]])
    state = new_state

print(f"Part 1: {sum(numpy.where(state == 1)[0] - offset)}")

state = numpy.asarray([0, 0, 0, 0] + [1 if c == "#" else 0 for c in state_] + [0, 0, 0, 0], dtype=int)

offset = 4

for i in range(50000000):
    new_state = numpy.zeros(state.shape, dtype=int)
    for x in range(2, len(state)-2):
        new_state[x] = rules.get(tuple(state[x-2:x+3]), 0)
    if numpy.allclose(numpy.roll(state, 1), new_state):
        break
    if new_state[0] or new_state[1] or new_state[3]:
        new_state = numpy.concatenate([[0, 0, 0, 0], new_state])
        offset += 4
    if new_state[-1] or new_state[-2] or new_state[-3]:
        new_state = numpy.concatenate([new_state, [0, 0, 0, 0]])
    state = new_state

print(f"Part 2: {sum(numpy.where(state == 1)[0] - offset + 50000000000 - i)}")
