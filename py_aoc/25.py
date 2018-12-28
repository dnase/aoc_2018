from sets import Set
from collections import deque
from util import get_data

def parsefunc(s):
    return tuple(int(k) for k in s.split(','))

def distance(p1, p2):
    return (abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2]) + abs(p2[3] - p1[3]))

def part1(seq):
    immediate = [set() for _ in range(len(seq))]
    for i, ic in enumerate(seq):
        for j, jc in enumerate(seq):
            if distance(jc, ic) <= 3:
                immediate[i].add(j)
    check = set()
    ans = 0
    for i in range(len(seq)):
        if i in check:
            continue
        ans += 1
        t = deque()
        t.append(i)
        while t:
            x = t.popleft()
            if x in check:
                continue
            check.add(x)
            for y in immediate[x]:
                t.append(y)
    return ans

def part2():
    return True

seq = get_data(25, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
