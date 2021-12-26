with open("../inputs/2018/day08.input", "r") as f:
    input = f.read().strip()


class Rose(object):
    def __init__(self, data, *children):
        self.data = tuple(data)
        self.children = tuple(children)

    @property
    def leaf(self):
        return not self.children


def parse(data):
    nchildren = data.pop()
    ndata = data.pop()
    if nchildren == 0:
        meta = []
        for _ in range(ndata):
            meta.append(data.pop())
        return Rose(meta)
    else:
        children = [parse(data) for _ in range(nchildren)]
        meta = []
        for _ in range(ndata):
            meta.append(data.pop())
        return Rose(meta, *children)


def sum_(rose):
    return sum(rose.data) + sum(map(sum_, rose.children))


data = list(map(int, input.split(" ")))
rev = list(reversed(data))
rose = parse(rev)

print(f"Part 1: {sum_(rose)}")


def fmap(rose):
    if not rose.children:
        return Rose([sum(rose.data)])
    else:
        c = list(map(fmap, rose.children))
        data = rose.data
        return Rose([sum(sum(c[i - 1].data) for i in data if 0 < i <= len(c))], *c)


nrose = fmap(rose)

print(f"Part 2: {sum(nrose.data)}")
