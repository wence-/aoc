from collections import deque

from intcode import CPU, load

mem = load("day23.input")


class Network(object):
    def __init__(self, mem, n):
        self.cpus = tuple(CPU(mem, i, self) for i in range(n))
        self.NAT = None

    def __getitem__(self, i):
        return self.cpus[i]

    def run(self):
        for cpu in self.cpus:
            cpu.run()

    @property
    def idle(self):
        return all(c.idle for c in self.cpus)

    def resume(self, i):
        assert self.NAT is not None
        self[i].queue_packet(self.NAT)


class CPU(CPU):
    def __init__(self, mem, i, network):
        super().__init__(mem)
        self.network = network
        self.output = []
        self.packet_queue = deque([i])
        self.missed_reads = 0

    @property
    def idle(self):
        return self.missed_reads > 1

    def queue_packet(self, packet):
        self.packet_queue.extend(packet)
        self.missed_reads = 0

    def inp(self):
        if self.packet_queue:
            yield self.packet_queue.popleft()
        else:
            self.missed_reads += 1
            yield -1

    def outp(self, val):
        self.missed_reads = 0
        self.output.append(val)
        if len(self.output) == 3:
            dest, *packet = self.output
            self.output.clear()
            if dest == 255:
                self.network.NAT = packet
            else:
                self.network[dest].queue_packet(packet)

    def run(self):
        super().run(inputs=self.inp(), outputs=self.outp)


def part1(mem):
    network = Network(mem, 50)
    while network.NAT is None:
        network.run()
    _, Y = network.NAT
    return Y


def part2(mem):
    network = Network(mem, 50)
    lasty = None
    while True:
        network.run()
        if network.idle:
            _, Y = network.NAT
            if Y == lasty:
                return Y
            network.resume(0)
            lasty = Y


print("Part 1:", part1(mem))
print("Part 2:", part2(mem))
