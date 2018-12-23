from util import get_data
import math

class Goblin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
    def attack(self, elf):
        # do attack stuff here
        return True

class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
    def attack(self, gob):
        # do attack stuff here
        return True

def euclidean_distance(p1, p2):
    return (math.sqrt(abs(p2[0] - p1[0])**2 + abs(p2[1] - p1[1])**2), p1, p2)

def find_nearest(npc, npcs):
    if isinstance(npc, Goblin):
        mm = min(map(euclidean_distance, [(k.x, k.y) for k in npcs if isinstance(k, Elf)], [(npc.x, npc.y) for k in npcs if isinstance(k, Elf)]))
    elif isinstance(npc, Elf):
        mm = min(map(euclidean_distance, [(k.x, k.y) for k in npcs if isinstance(k, Goblin)], [(npc.x, npc.y) for k in npcs if isinstance(k, Goblin)]))
    else:
        mm = False
    tx = mm[1][0]
    ty = mm[1][1]
    tnpc = [t for t in npcs if t.x == tx and t.y == ty][0]

def get_target_location(tnpc, grid):
    if grid[(tnpc.x, tnpc.y - 1)] == '.':

def get_grid(seq):
    grid = {}
    npcs = []
    for y, line in enumerate(seq):
        for x, c in enumerate(line):
            if c == 'G':
                grid[(x, y)] = '.'
                npcs.append(Goblin(x, y))
            elif c == 'E':
                grid[(x, y)] = '.'
                npcs.append(Elf(x, y))
            else:
                grid[(x, y)] = c
    return (grid, npcs)

def move(g, n):
    for npc in n:
        target = find_nearest(npc, n)


    return True

def parsefunc(s):
    return s.strip()

def part1(seq):
    (g, n) = get_grid(seq)
    return move(g, n)

def part2():
    return True

seq = get_data(15, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
