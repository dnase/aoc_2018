from collections import Counter, defaultdict
from util import parse_file

def parsefunc(s):
    buff = [n.strip() for n in s.split(",")]
    return (int(buff[0]), int(buff[1]))

def manhattan_distance(x1, x2, y1, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

def get_range(seq, idx):
    return (max(zip(*seq)[idx])+2)

def get_grid(seq):
    g = defaultdict(lambda: -1)
    g2 = {}
    for x in range(get_range(seq, 0)):
        for y in range(get_range(seq, 1)):
            g2[(x, y)] = sum(manhattan_distance(x, i, y, j) for i, j in seq) < 10000
            mindistance = min(manhattan_distance(x, i, y, j) for i, j in seq)
            for n, (i, j) in enumerate(seq):
                checkdistance = manhattan_distance(x, i, y, j)
                if checkdistance == mindistance:
                    if g[(x, y)] != -1:
                        g[(x, y)] = -1
                        break
                    g[(x, y)] = n
    return (g, g2)

def part1(g, seq):
    bounds = set(g[(x, max(zip(*seq)[1]))] for x in range(max(zip(*seq)[0]))).union(set(g[(x, 0)] for x in range(max(zip(*seq)[0])))).union(set(g[(max(zip(*seq)[0]), y)] for y in range(max(zip(*seq)[1])))).union(set(g[(0, y)] for y in range(max(zip(*seq)[1]))))
    for i in Counter(g.values()).most_common():
        if i[0] not in bounds:
            return i[1]

def part2(g):
    return sum(g.values())

seq = parse_file("../data/input_6", parsefunc)

grid = get_grid(seq)

print("Q1: %d" % part1(grid[0], seq))
print("Q2: %d" % part2(grid[1]))
