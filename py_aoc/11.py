from operator import itemgetter
from sets import Set
from collections import defaultdict
from util import get_data
import numpy

def get_score(x, y, gridsn):
    try:
        plevel = int(str((((x + 10) * y) + gridsn) * (x + 10))[-3]) - 5
    except:
        plevel = -5
    return plevel

def score_map(gridsn):
    scores = {}
    for x in range(1,301):
        for y in range(1,301):
            scores[x, y] = get_score(x, y, gridsn)
    return scores

def traverse_map(sm, width=3):
    tl_x = 1
    tl_y = 1
    scores = defaultdict(int)
    while (1 <= tl_x <= (301 - width)) and (1 <= tl_y <= (301 - width)):
        total = 0
        for x in range(tl_x, tl_x + width):
            for y in range(tl_y, tl_y + width):
                total += sm[(x, y)]
        scores[(tl_x, tl_y)] = total
        tl_x += 1
        if tl_x == (302 - width):
            tl_x = 1
            tl_y += 1
    return sorted(scores.items(), key=itemgetter(1))[-1]

def check_widths(sm):
     # really slow due to the terrible big O of my solution
     # but it works
    scores = {}
    # I found that I don't have to extend the range past 20 to
    # get the correct answer
    for w in range(3, 20):
        scores[w] = traverse_map(sm, w)
    return sorted(scores.items(), key=lambda s: s[1][1])[-1]

def part1(gridsn):
    sm = score_map(gridsn)
    return traverse_map(sm)

def part2(gridsn):
    sm = score_map(gridsn)
    return check_widths(sm)

def parsefunc(s):
    return s.strip()

gridsn = int(get_data(11, parsefunc)[0])

print("P1: ", part1(gridsn))
print("P2: ", part2(gridsn))
