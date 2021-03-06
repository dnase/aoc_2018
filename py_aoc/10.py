from util import get_data
import re

class point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def parsefunc(s):
    return s.strip()

def printstate(i, pm):
    canvas = [[' '] * 200 for _ in xrange(200)]
    for p in pm:
        canvas[p.y + i * p.vy][p.x + i * p.vx - 100] = '*'

    for c in canvas:
        print ''.join(c)

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
    alignment = 10459
    # uncomment the following to find your alignment time
    # I hardcoded mine, which was 10459 so that it runs faster.
    #buff = pointmap
    #sizes = []
    #for _ in range(20000):
    #    buff = translate(buff)
    #    sizes.append(size(buff))
    #alignment = sizes.index(min(sizes)) + 1
    printstate(alignment, pointmap)
    return alignment


def part2():
    return True

seq = get_data(10, parsefunc)

i = part1(seq)

print("P1: ", "see above")
print("P2: ", i)
