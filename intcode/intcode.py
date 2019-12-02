import os
from collections import namedtuple

import numpy

from .cintcode import evaluate_with_generator as evaluate
from .cintcode import evaluate_with_state

__all__ = ("CPU", "evaluate", "load")


def load(name):
    with open(os.path.join("inputs", name), "r") as f:
        return numpy.asarray(list(map(int, f.read().strip().split(","))),
                             dtype=numpy.int64)


def ignore(x):
    pass


class CPU(object):
    State = namedtuple("State", ["mem", "pc", "rbase", "halted"])

    def __init__(self, mem):
        self.state = CPU.State(mem.copy(), 0, 0, False)

    def run(self, inputs=None, outputs=ignore):
        if inputs is not None:
            inputs = iter(inputs)
        self.state = CPU.State(*evaluate_with_state(*self.state,
                                                    inputs=inputs,
                                                    outputs=outputs))

    @property
    def halted(self):
        return self.state.halted

    @property
    def mem(self):
        return self.state.mem
