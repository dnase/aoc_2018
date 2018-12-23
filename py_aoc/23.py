from util import get_data
from Queue import PriorityQueue

def parsefunc(s):
    parts = s.split(', ')
    pos = tuple(int(c) for c in parts[0][len("pos=<"):-1].split(','))
    r = int(parts[1][2:])
    return (pos, r)

def distance(p1, p2):
    return (abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2]))

def part1(seq):
    m = max(seq, key=lambda n: n[1])
    return sum([1 for n in seq if distance(n[0], m[0]) <= m[1]])

def part2(seq):
    q = PriorityQueue()
    for n in seq:
        x,y,z,r = n[0][0], n[0][1], n[0][2], n[1]
        d = abs(x) + abs(y) + abs(z)
        q.put((max(0, d - r),1))
        q.put((d + r,-1))
    c, m, r = 0, 0, 0
    while not q.empty():
        dist, e = q.get()
        c += e
        if c > m:
            r = dist
            m = c
    return r

seq = get_data(23, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2(seq))
