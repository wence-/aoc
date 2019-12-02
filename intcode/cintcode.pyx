# cython: language_level=3
import cython
import numpy as np

cimport numpy as np
from cython.view cimport array as cvarray


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
cdef inline np.int64_t get_val(np.int64_t[::1] mem,
                               np.int64_t i,
                               np.int64_t pc,
                               np.int64_t rbase,
                               np.int64_t[::1] modes) nogil:
    cdef np.int64_t r, m, n
    r = mem[pc+i]
    m = modes[i]
    n = mem.shape[0]
    if m == 1:
        return r
    elif m == 2:
        if r + rbase >= n:
            return 0
        else:
            return mem[r+rbase]
    else:
        if r >= n:
            return 0
        else:
            return mem[r]


@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline np.int64_t[::1] put_val(np.int64_t val,
                                    np.int64_t[::1] mem,
                                    np.int64_t i,
                                    np.int64_t pc,
                                    np.int64_t rbase,
                                    np.int64_t[::1] modes):
    cdef np.int64_t r, m, n
    r = mem[pc+i]
    m = modes[i]
    n = mem.shape[0]
    if m == 2:
        r += rbase
    if r >= n:
        newmem = np.zeros(r*2, dtype=np.int64)
        newmem[:n] = mem[:]
        mem = newmem
    if m == 2:
        mem[r] = val
    elif m == 0:
        mem[r] = val
    else:
        raise ValueError(f"Unhandled mode {m}")
    return mem


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_state(mem_,
                        int pc, int rbase, halted, *,
                        inputs=None, outputs=None, int maxreads=-1):
    cdef np.int64_t[::1] mem = mem_
    cdef np.int64_t[::1] modes = cvarray(shape=(4, ), itemsize=sizeof(np.int64_t), format="l")
    cdef np.int64_t a, b, i, op
    if halted:
        return mem, pc, rbase, True
    while True:
        op = mem[pc]
        modes[0] = (op // 100) % 10
        modes[1] = (op // 1000) % 10
        modes[2] = (op // 10000) % 10
        op %= 100
        pc += 1
        if op == BRK:
            return mem, pc, rbase, True
        elif op == ADD:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(a + b, mem, 2, pc, rbase, modes)
            pc += 3
        elif op == MUL:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(a * b, mem, 2, pc, rbase, modes)
            pc += 3
        elif op == JZ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            pc = b if a != 0 else pc + 2
        elif op == LT:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(<np.int64_t>(a < b), mem, 2, pc, rbase, modes)
            pc += 3
        elif op == EQ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(<np.int64_t>(a == b), mem, 2, pc, rbase, modes)
            pc += 3
        elif op == IRB:
            rbase += get_val(mem, 0, pc, rbase, modes)
            pc += 1
        elif op == GET:
            try:
                val = next(inputs)
            except StopIteration:
                return mem, pc - 1, rbase, False
            mem = put_val(val, mem, 0, pc, rbase, modes)
            pc += 1
            maxreads -= 1
            if maxreads == 0:
                return mem, pc, rbase, False
        elif op == PUT:
            outputs(get_val(mem, 0, pc, rbase, modes))
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
@cython.cdivision(True)
def evaluate_with_generator(mem_, *, inputs=None):
    cdef np.int64_t[::1] mem = mem_.copy()
    cdef np.int64_t[::1] modes = cvarray(shape=(4, ), itemsize=sizeof(np.int64_t), format="l")
    cdef np.int64_t a, b, i, op, pc = 0, rbase = 0
    if inputs is not None:
        inputs = iter(inputs)
    while True:
        op = mem[pc]
        modes[0] = (op // 100) % 10
        modes[1] = (op // 1000) % 10
        modes[2] = (op // 10000) % 10
        op %= 100
        pc += 1
        if op == BRK:
            return
        elif op == ADD:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(a + b, mem, 2, pc, rbase, modes)
            pc += 3
        elif op == MUL:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(a * b, mem, 2, pc, rbase, modes)
            pc += 3
        elif op == JZ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            pc = b if a == 0 else pc + 2
        elif op == JNZ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            pc = b if a != 0 else pc + 2
        elif op == LT:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(<np.int64_t>(a < b), mem, 2, pc, rbase, modes)
            pc += 3
        elif op == EQ:
            a = get_val(mem, 0, pc, rbase, modes)
            b = get_val(mem, 1, pc, rbase, modes)
            mem = put_val(<np.int64_t>(a == b), mem, 2, pc, rbase, modes)
            pc += 3
        elif op == IRB:
            rbase += get_val(mem, 0, pc, rbase, modes)
            pc += 1
        elif op == GET:
            mem = put_val(next(inputs), mem, 0, pc, rbase, modes)
            pc += 1
        elif op == PUT:
            yield get_val(mem, 0, pc, rbase, modes)
            pc += 1
        else:
            raise ValueError(f"Unknown opcode {op}")
