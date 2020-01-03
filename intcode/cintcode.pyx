# cython: language_level=3
import cython
import numpy as np

cimport numpy as np


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
cdef inline np.int64_t get_val(np.int64_t[::1] mem,
                               np.int64_t pc,
                               np.int64_t rbase,
                               np.int64_t m) nogil:
    cdef np.int64_t r
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
cdef inline np.int64_t[::1] put_val(np.int64_t val,
                                    np.int64_t[::1] mem,
                                    np.int64_t pc,
                                    np.int64_t rbase,
                                    np.int64_t m):
    cdef np.int64_t r, n
    cdef np.int64_t[::1] newmem
    r = mem[pc]
    n = mem.shape[0]
    if m == 2:
        r += rbase
    if r >= n:
        newmem = np.zeros(r*2, dtype=np.int64)
        newmem[:n] = mem[:]
        mem = newmem
    mem[r] = val
    return mem


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_state(mem_,
                        int pc, int rbase, halted, *,
                        inputs=None, outputs=None, int maxreads=-1):
    cdef np.int64_t[::1] mem = mem_
    cdef np.int64_t a, b, op, amode, bmode, cmode
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
            mem = put_val(a + b, mem, pc+2, rbase, cmode)
            pc += 3
        elif op == MUL:
            mem = put_val(a * b, mem, pc+2, rbase, cmode)
            pc += 3
        elif op == JZ:
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            pc = b if a != 0 else pc + 2
        elif op == LT:
            mem = put_val(<np.int64_t>(a < b), mem, pc+2, rbase, cmode)
            pc += 3
        elif op == EQ:
            mem = put_val(<np.int64_t>(a == b), mem, pc+2, rbase, cmode)
            pc += 3
        elif op == IRB:
            rbase += a
            pc += 1
        elif op == GET:
            try:
                a = next(inputs)
            except StopIteration:
                return mem, pc - 1, rbase, False
            mem = put_val(a, mem, pc, rbase, amode)
            pc += 1
            maxreads -= 1
            if maxreads == 0:
                return mem, pc, rbase, False
        elif op == PUT:
            outputs(get_val(mem, pc, rbase, amode))
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_generator(mem_, *, inputs=None):
    cdef np.int64_t[::1] mem = mem_.copy()
    cdef np.int64_t a, b, op, pc = 0, rbase = 0, amode, bmode, cmode
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
            mem = put_val(a + b, mem, pc+2, rbase, cmode)
            pc += 3
        elif op == MUL:
            mem = put_val(a * b, mem, pc+2, rbase, cmode)
            pc += 3
        elif op == JZ:
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            pc = b if a != 0 else pc + 2
        elif op == LT:
            mem = put_val(<np.int64_t>(a < b), mem, pc+2, rbase, cmode)
            pc += 3
        elif op == EQ:
            mem = put_val(<np.int64_t>(a == b), mem, pc+2, rbase, cmode)
            pc += 3
        elif op == IRB:
            rbase += a
            pc += 1
        elif op == GET:
            a = next(inputs)
            mem = put_val(a, mem, pc, rbase, amode)
            pc += 1
        elif op == PUT:
            yield a
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")
