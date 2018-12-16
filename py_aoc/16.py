from util import get_data
from sets import Set
from opcodes import *
import re

OPCODES = {
    addr: set(),
    addi: set(),
    mulr: set(),
    muli: set(),
    banr: set(),
    bani: set(),
    borr: set(),
    bori: set(),
    setr: set(),
    seti: set(),
    gtir: set(),
    gtri: set(),
    gtrr: set(),
    eqir: set(),
    eqri: set(),
    eqrr: set(),
}

def parsefunc(s):
    return s.strip()

def main(inst):
    total = 0
    ops = {opcode : set(OPCODES) for opcode in range(16)}
    for i in inst:
        b = i[0]
        d = i[1]
        a = i[2]
        t = try_instructions(b, d, a)
        if t[0] >= 3:
            total += 1
        ops[d[0]].intersection_update(t[1])
    return (total, ops)


def try_instructions(b, d, a):
    tally = 0
    successful = set()
    for opcode, n in OPCODES.items():
        A = [a[0], a[1], a[2], a[3]]
        if opcode(b, *d[1:]) == A:
            tally += 1
            successful.add(opcode)
    return (tally, successful)


def get_instructions(seq):
    inst = []
    for i, s in enumerate(seq):
        if 'Before' in s:
            b1 = re.search(r'(\d*), (\d*), (\d*), (\d*)', s)
            b2 = re.search(r'(\d*) (\d*) (\d*) (\d*)', seq[i + 1])
            b3 = re.search(r'(\d*), (\d*), (\d*), (\d*)', seq[i + 2])
            inst.append(((int(b1.group(1)), int(b1.group(2)), int(b1.group(3)), int(b1.group(4))), (int(b2.group(1)), int(b2.group(2)), int(b2.group(3)), int(b2.group(4))), (int(b3.group(1)), int(b3.group(2)), int(b3.group(3)), int(b3.group(4)))))
            pass
            pass
    return inst

def part1(seq):
    inst = get_instructions(seq)
    return main(inst)[0]


def part2(seq):
    inst = get_instructions(seq)
    return main(inst)[1]

seq = get_data(16, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2(seq))
