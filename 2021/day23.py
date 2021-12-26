import heapq
import time

start = time.time()

with open("../inputs/2021/day23.input", "r") as f:
    data = f.read()
    chars = [ord(c) - ord("A") + 1 for c in data if c in {"A", "B", "C", "D"}]
    state1 = [0] * 11
    for i in range(4):
        state1.append(chars[i])
        state1.append(chars[4 + i])

    state2 = list(state1[:11])
    # D#C#B#A#
    # D#B#A#C#
    new = [[4, 4], [3, 2], [2, 1], [1, 3]]
    for i in range(4):
        state2.append(state1[11 + 2 * i])
        state2.extend(new[i])
        state2.append(state1[11 + 2 * i + 1])
    inp = tuple(state1), tuple(state2)


# Basically implements the scheme of github.com/orlp/aoc2021/
def heuristic(state, room_size):
    # Idea, amphipods can move through each other
    cost = 0
    noutside = [0, 0, 0, 0]
    # Check the hallway
    for i in range(11):
        room = state[i] - 1
        if room >= 0:
            # Non-empty slot, needs to go to target room
            noutside[room] += 1
            cost += abs(i - (2 + 2 * room)) * 10 ** room

    for room in range(4):
        for offset in range(room_size):
            # For any amphipod in a room that is not its target room
            i = 11 + room_size * room + offset
            target = state[i] - 1
            if target >= 0 and target != room:
                # It needs to go to a room
                noutside[target] += 1
                cost += (1 + offset + 2 * abs(room - target)) * 10 ** target

    for i, k in enumerate(noutside):
        cost += (k * (k + 1)) // 2 * 10 ** i
    return cost


def sym_range(a, b):
    return range(min(a, b), max(a, b) + 1)


def to_room(state, source, room, room_states, room_occ, room_size):
    path = sym_range(source, 2 + 2 * room)
    if all(s == 0 or s == room + 1 for s in room_states[room]) and all(
        i == source or state[i] == 0 for i in path
    ):
        # If there's a clear path and the target room is empty or only
        # contains the correct amphipods
        vacant = room_occ[room] - 1
        yield (source, 11 + room_size * room + vacant, len(path) + vacant)


def from_room(state, room, hallway, room_states, room_occ, room_size):
    occ = room_occ[room]
    if occ == room_size:
        return
    path = sym_range(hallway, 2 + 2 * room)
    target = room_states[room][occ] - 1
    direct = hallway in sym_range(2 + 2 * room, 2 + 2 * target)
    if (
        not (direct and len(path) > 2)
        and all(i == hallway or state[i] == 0 for i in path)
        # Check that this wouldn't cause a deadlock
        # Doesn't work for all inputs, happens to work for mine
        and not any(
            s > 0 and hallway in sym_range(2 + 2 * target, 2 + 2 * (s - 1))
            for s in room_states[target]
        )
    ):
        yield (11 + room_size * room + occ, hallway, len(path) + occ)


def generate_moves(state, room_size):
    room_start = lambda r: 11 + r * room_size
    room_states = [state[room_start(i) : room_start(i + 1)] for i in range(4)]
    room_occ = []
    for s in room_states:
        for i, ss in enumerate(s):
            if ss > 0:
                room_occ.append(i)
                break
        else:
            room_occ.append(room_size)

    for hallway in [0, 1, 3, 5, 7, 9, 10]:
        if state[hallway] == 0:
            for room in range(4):
                yield from from_room(
                    state, room, hallway, room_states, room_occ, room_size
                )
        else:
            yield from to_room(
                state, hallway, state[hallway] - 1, room_states, room_occ, room_size
            )


def astar(state):
    pq = []
    heapq.heappush(pq, (0, 0, state))
    mincost = {state: 0}
    room_size = (len(state) - 11) // 4
    while pq:
        _, cost, state = heapq.heappop(pq)
        if cost > mincost.get(state, 10 ** 100):
            continue
        elif all(w <= x for w, x in zip(state, state[1:])):
            return cost
        for source, target, distance in generate_moves(state, room_size):
            new_state = list(state)
            amphipod = new_state[source]
            new_state[target] = amphipod
            new_state[source] = 0
            new_state = tuple(new_state)
            new_cost = cost + distance * 10 ** (amphipod - 1)
            if new_cost < mincost.get(new_state, 10 ** 100):
                mincost[new_state] = new_cost
                approx_cost = new_cost + heuristic(new_state, room_size)
                heapq.heappush(pq, (approx_cost, new_cost, new_state))
    return 0


def part1(inp):
    state, _ = inp
    return astar(state)


def part2(inp):
    _, state = inp
    return astar(state)


print(
    f"Day 23     {part1(inp):<14} {part2(inp):<14} {(time.time() - start)*1e3:>11.2f}"
)
