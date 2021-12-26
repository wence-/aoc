import re

from intcode import CPU, load

BAD_ITEMS = frozenset(
    ["photons", "giant electromagnet", "escape pod", "infinite loop", "molten lava"]
)
BACK = {"north": "south", "east": "west", "south": "north", "west": "east"}


def parse(state):
    doors = []
    items = set()
    for line in state.split("\n"):
        if line.startswith("=="):
            room = line[3:-3]
        elif re.match("- (north|south|east|west)$", line):
            doors.append(line[2:])
        elif line.startswith("-"):
            items.add(line[2:])
    return room, doors, items - BAD_ITEMS


class Player(CPU):
    def run(self, *commands, record_output=True):
        inputs = map(ord, "\n".join(commands + ("",)))
        if record_output:
            output = []
            super().run(inputs=inputs, outputs=output.append)
            return "".join(map(chr, output))
        else:
            super().run(inputs=inputs)


def explore(cpu, path, state, inventory=None, paths=None):
    room, doors, items = parse(state)
    if room in paths:
        return inventory, paths
    paths[room] = path
    cpu.run(*(f"take {item}" for item in items), record_output=False)
    inventory = inventory | items
    for d in doors:
        state = cpu.run(d)
        inventory, paths = explore(
            cpu, path + (d,), state, inventory=inventory, paths=paths
        )
        cpu.run(BACK[d], record_output=False)
    return inventory, paths


def play(mem):
    cpu = Player(mem)
    inventory, paths = explore(cpu, (), cpu.run(), set(), {})
    checkpoint = "Security Checkpoint"
    cpu.run(*paths[checkpoint], record_output=False)
    inventory = tuple(sorted(inventory))
    n = len(inventory)
    gray = 0
    for i in range(1, 1 << n):
        state = cpu.run("west")
        try:
            (password,) = re.findall("([0-9]{10})", state)
            return password, tuple(inventory[j] for j in range(n) if ~gray & (1 << j))
        except ValueError:
            pass
        diff = (i ^ (i >> 1)) - gray
        gray += diff
        c = "take" if diff < 0 else "drop"
        (j,) = (j for j in range(n) if abs(diff) & (1 << j))
        cpu.run(f"{c} {inventory[j]}", record_output=False)


def perfectplay(mem):
    cpu = Player(mem)
    commands = [
        "north",
        "north",
        "take monolith",
        "north",
        "take hypercube",
        "south",
        "south",
        "east",
        "east",
        "take easter egg",
        "east",
        "south",
        "take ornament",
        "west",
        "south",
    ]
    cpu.run(*commands, record_output=False)
    (password,) = re.findall("([0-9]{10})", cpu.run("west"))
    return password, ("easter egg", "hypercube", "monolith", "ornament")


mem = load("day25.input")
password, items = play(mem)
print("Part 1:", password)
print("Correct items:", ", ".join(items))
