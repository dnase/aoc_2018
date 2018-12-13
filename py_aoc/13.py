from util import get_data
from collections import defaultdict
from sets import Set

class cart:
    def __init__(self, c, pos):
        self.char = c
        self.x = pos[0]
        self.y = pos[1]
        self.turns = 1

    def turn(self, c):
        if c == '+':
            if self.turns % 3 == 0:
                # right
                self.turnright()
            elif self.turns % 2 == 0:
                # straight
                pass
                self.turns += 1
            else:
                # left
                self.turnleft()

        elif c == '/':
            if self.char == '<':
                self.char = 'v'
            elif self.char == '^':
                self.char = '>'
        elif c == '\\':
            if self.char == '>':
                self.char = 'v'
            elif self.char == '^':
                self.char = '<'



    def turnleft(self):
        if self.char == '^':
            self.char = '<'
        elif self.char == '<':
            self.char = 'v'
        elif self.char == 'v':
            self.char = '>'
        elif self.char == '>':
            self.char = '^'
        self.turns += 1

    def turnright(self):
        if self.char == '^':
            self.char = '>'
        elif self.char == '>':
            self.char = 'v'
        elif self.char == 'v':
            self.char = '<'
        elif self.char == '<':
            self.char = '^'
        self.turns += 1

def parsefunc(s):
    return s

def build_grid(s):
    ret = defaultdict(lambda: " ")
    for y, line in enumerate(s):
        for x, c in enumerate(line):
            ret[(x, y)] = c
    return ret

def get_carts(g):
    buff = g
    carts = []
    rep = { '^': '|', 'v': '|', '<': '-', '>': '-'}
    for k, v in buff.items():
        if v in rep.keys():
            carts.append(cart(v, k))
            buff[k] = rep[v]
    return (carts, buff)

def tick(c, g):
    xys = set()
    for idx, cart in enumerate(c):
        if cart.char == '^':
            nx = cart.x
            ny = cart.y - 1
        elif cart.char == 'v':
            nx = cart.x
            ny = cart.y + 1
        elif cart.char == '<':
            nx = cart.x - 1
            ny = cart.y
        elif cart.char == '>':
            nx = cart.x + 1
            ny = cart.y
        rail = g[(nx, ny)]
        cart.x = nx
        cart.y = ny
        cart.turn(rail)
        if (nx, ny) in xys:
            # uncomment for part 1
            #return (nx, ny)
            del(c[idx])
            delme = [j for j, mc in enumerate(c) if mc.x == nx and mc.y == ny][0]
            del(c[delme])
        else:
            xys.add((nx, ny))
        if len(c) == 1:
            return (c[0].x, c[0].y)
    #xys = [(cart.x, cart.y) for cart in c]
    return 0

def game_loop(c, g):
    v = 0
    while True:
        v = tick(c, g)
        if v != 0:
            return v

def max_x(g):
    return max(zip(*g.keys())[0])

def max_y(g):
    return max(zip(*g.keys())[1])

def printstate(g):
    outstr = ''
    for y in range(150):
        for x in range(150):
            outstr += (g[(x, y)])
        outstr += "\n"
    print(outstr)

def part1(seq):
    g = build_grid(seq)
    (c, g) = get_carts(g)
    return game_loop(c, g)

def part2():
    return True

seq = get_data(13, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
