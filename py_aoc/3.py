from collections import defaultdict

def parse(line):
    id, _, coords, dims = line.split()
    minx, miny = coords[:-1].split(",")
    width, height = dims.split("x")
    return id, int(minx), int(miny), int(width), int(height)

def overlap(seq):
    d = [parse(line) for line in seq]
    pointmap = defaultdict(int)
    for _, x, y, w, h in d:
        for i in range(x, x + w):
            for j in range(y, y + h):
                pointmap[(i, j)] += 1

    buff = 0
    for v in pointmap.values():
        if v > 1:
            buff += 1
    print("Q1: %d" % buff)
    return pointmap

def id_no_overlap(seq, pointmap):
    d = [parse(line) for line in seq]
    for id, x, y, w, h in d:
        valid = True
        for i in range(x, x + w):
            for j in range(y, y + h):
                if pointmap[(i, j)] != 1:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("Q2: %s" % id[1:])

seq = [s.strip() for s in open("../data/input_3").readlines()]
p = overlap(seq)
id_no_overlap(seq, p)
