from collections import defaultdict
from util import get_data
import subprocess as sp

def parsefunc(s):
    return s.strip()

def get_plot(seq):
    plot = defaultdict(lambda: '.')
    for y, line in enumerate(seq):
        for x, c in enumerate(line):
            plot[(x, y)] = c
    return plot

def num_adjacent(xy, plot, c):
    x, y = xy
    adj = ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))
    return sum([1 for pxy, v in plot.items() if v == c and pxy in adj])

def mutate(plot):
    newplot = defaultdict(lambda: '.')
    for y in range(50):
        for x in range(50):
            if plot[(x, y)] == '.':
                if num_adjacent((x, y), plot, '|') >= 3:
                    newplot[(x, y)] = '|'
            elif plot[(x, y)] == '|':
                if num_adjacent((x, y), plot, '#') >= 3:
                    newplot[(x, y)] = '#'
            elif plot[(x, y)] == '#':
                if num_adjacent((x, y), plot, '#') < 1 or num_adjacent((x, y), plot, '|') < 1:
                    newplot[(x, y)] = '.'
                else:
                    newplot[(x, y)] = '#'
    return newplot

def print_plot(plot):
    outstr = ''
    for y in range(50):
        for x in range(50):
            outstr += plot[(x, y)]
        outstr += "\n"
    print outstr


def part1(seq):
    p = get_plot(seq)
    sp.call('clear',shell=True)
    print_plot(p)
    for _ in range(10):
        p = mutate(p)
        sp.call('clear',shell=True)
        print_plot(p)
    return sum([1 for _, t in p.items() if t == '|']) * sum([1 for _, l in p.items() if l == '#'])

def part2():
    return True

seq = get_data(18, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
