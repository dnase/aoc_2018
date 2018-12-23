from collections import defaultdict
from util import get_data
import re

def parsefunc(s):
    return s.strip()

def get_grid(seq):
    clay = defaultdict(bool)
    for s in seq:
        a, b, c = map(int, re.findall("([\d]+)", s))
        if s.startswith('x='):
            for y in range(b, c+1):
                clay[a + y * 1j] = True
        else:
            for x in range(b, c+1):
                clay[x + a * 1j] = True
    return clay

def print_grid(g):
    outbuff = ''
    for y in range(ymin(g), ymax(g) + 1):
        for x in range(xmin(g) + 100, xmax(g) + 1):
            outbuff += g[(x, y)]
        outbuff += "\n"
    print outbuff

def sum_grid(g):
    total = 0
    for y in range(ymin(g), ymax(g) + 1):
        for x in range(xmin(g), xmax(g) + 1):
            total += (1 if g[(x, y)] == '.' else 0)
    return total

def xmax(g):
    return max(*g.keys()[0])

def xmin(g):
    return min(*g.keys()[0])

def ymax(g):
    return max(*g.keys()[1])

def ymin(g):
    return min(*g.keys()[1])

def part1(seq):
    return True

def part2():
    return True

seq = get_data(17, parsefunc)

print seq

print("P1: ", part1(seq))
print("P2: ", part2())
