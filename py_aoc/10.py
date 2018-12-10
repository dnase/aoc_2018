from util import parse_file
import time
import re

class point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def parsefunc(s):
    return s.strip()

def size(pm):
    return ((max([p.x for p in pm]) - min([p.x for p in pm])) + (max([p.y for p in pm]) - min([p.y for p in pm])))

def translate(pm):
    buff = []
    for p in pm:
        buff.append(point(p.x + p.vx, p.y + p.vy, p.vx, p.vy))
    return buff

def printstate(i, pm):
    map = [[' '] * 200 for j in xrange(200)]
    for p in pm:
        map[p.y + i * p.vy][p.x + i * p.vx - 100] = '*'

    for m in map:
        print ''.join(m)

def get_point(line):
    buff = re.match(r"position=<\s*?([\-\d]*),\s*?([\-\d]*)> velocity=<\s*?([\-\d]*),\s*?([\d\-]*)>", line)
    return(int(buff.group(1)), int(buff.group(2)), int(buff.group(3)), int(buff.group(4)))

def get_pointmap(seq):
    pointmap = []
    for line in seq:
        x, y, vx, vy = get_point(line)
        pointmap.append(point(x, y, vx, vy))
    return pointmap

def part1(seq):
    pointmap = get_pointmap(seq)
    buff = pointmap
    sizes = []
    for _ in range(20000):
        buff = translate(buff)
        sizes.append(size(buff))
    alignment = sizes.index(min(sizes)) + 1
    printstate(alignment, pointmap)
    return alignment


def part2():
    return True

seq = parse_file("../data/input_10", parsefunc)

i = part1(seq)

print("P1: ", "see above")
print("P2: ", i)
