# cython: language_level=3
import cython
import numpy as np
from libc.stdint cimport int64_t

from cython cimport view


DEF ADD = 1
DEF MUL = 2
DEF GET = 3
DEF PUT = 4
DEF JNZ = 5
DEF JZ = 6
DEF LT = 7
DEF EQ = 8
DEF IRB = 9
DEF BRK = 99


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
cdef inline int64_t get_val(int64_t[::1] mem,
                            int64_t pc,
                            int64_t rbase,
                            int64_t m) nogil:
    cdef int64_t r
    r = mem[pc]
    if m == 1:
        return r
    elif m == 2:
        r += rbase
    if r >= mem.shape[0]:
        return 0
    else:
        return mem[r]


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
cdef inline int64_t[::1] maybe_realloc(int64_t[::1] mem, int64_t r):
    cdef int64_t n = mem.shape[0]
    cdef int64_t[::1] newmem
    if r >= n:
        newmem = view.array((r*2, ), sizeof(int64_t), "l")
        newmem[:n] = mem[:]
        return newmem
    else:
        return mem


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_state(int64_t[::1] mem,
                        int pc, int rbase, halted, *,
                        inputs=None, outputs=None, int maxreads=-1):
    cdef int64_t a, b, r, op, amode, bmode, cmode
    if halted:
        return mem, pc, rbase, True
    while True:
        op = mem[pc]
        amode = (op // 100) % 10
        bmode = (op // 1000) % 10
        cmode = (op // 10000) % 10
        op %= 100
        pc += 1
        a = get_val(mem, pc, rbase, amode)
        b = get_val(mem, pc+1, rbase, bmode)
        if op == BRK:
            return mem, pc, rbase, True
        elif op == ADD:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = a + b
            pc += 3
        elif op == MUL:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = a * b
            pc += 3
        elif op == JZ:
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            pc = b if a != 0 else pc + 2
        elif op == LT:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = <int64_t>(a < b)
            pc += 3
        elif op == EQ:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = <int64_t>(a == b)
            pc += 3
        elif op == IRB:
            rbase += a
            pc += 1
        elif op == GET:
            try:
                a = next(inputs)
            except StopIteration:
                return mem, pc - 1, rbase, False
            r = mem[pc] + (rbase if amode == 2 else 0)
            mem[r] = a
            pc += 1
            maxreads -= 1
            if maxreads == 0:
                return mem, pc, rbase, False
        elif op == PUT:
            outputs(a)
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_generator(int64_t[::1] mem, *, inputs=None):
    cdef int64_t a, b, op, r, pc = 0, rbase = 0, amode, bmode, cmode
    mem = mem.copy()
    if inputs is not None:
        inputs = iter(inputs)
    while True:
        op = mem[pc]
        amode = (op // 100) % 10
        bmode = (op // 1000) % 10
        cmode = (op // 10000) % 10
        op %= 100
        pc += 1
        a = get_val(mem, pc, rbase, amode)
        b = get_val(mem, pc+1, rbase, bmode)
        if op == BRK:
            return
        elif op == ADD:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = a + b
            pc += 3
        elif op == MUL:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = a * b
            pc += 3
        elif op == JZ:
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            pc = b if a != 0 else pc + 2
        elif op == LT:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = <int64_t>(a < b)
            pc += 3
        elif op == EQ:
            r = mem[pc+2] + (rbase if cmode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = <int64_t>(a == b)
            pc += 3
        elif op == IRB:
            rbase += a
            pc += 1
        elif op == GET:
            a = next(inputs)
            r = mem[pc] + (rbase if amode == 2 else 0)
            mem = maybe_realloc(mem, r)
            mem[r] = a
            pc += 1
        elif op == PUT:
            yield a
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")
