from util import get_data

def parsefunc(s):
    parts = s.split(', ')
    pos = tuple(int(c) for c in parts[0][len("pos=<"):-1].split(','))
    r = int(parts[1][2:])
    return (pos, r)

def distance(p1, p2):
    return (abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2]))

def part1(seq):
    m = max(seq, key=lambda n: n[1])
    total = 0
    for n in seq:
        if distance(n[0], m[0]) <= m[1]:
            total += 1
    return total

def part2():
    return True

seq = get_data(23, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
