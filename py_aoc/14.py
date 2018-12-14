from util import get_data

def parsefunc(s):
    return s.strip()

def move_elves(e, r):
    buff = {}
    for elf, pos in e.items():
        buff[elf] = (pos + 1 + int(r[pos])) % len(r)
    return buff

def solve(r, v, p):
    n = 10
    elves = {1: 0, 2: 1}
    recipes = r
    if p == 1:
        while len(recipes) < int(v) + n:
            recipes += str(int(recipes[elves[1]]) + int(recipes[elves[2]]))
            elves = move_elves(elves, recipes)
        return recipes[-10:]
    elif p == 2:
        while v not in recipes:
            recipes += str(int(recipes[elves[1]]) + int(recipes[elves[2]]))
            elves = move_elves(elves, recipes)
        return recipes.find(v)

def part1(s):
    return solve("37", s, 1)


def part2(s):
    return solve("37", s, 2)

seq = get_data(14, parsefunc)[0]

print("P1: ", part1(seq))
print("P2: ", part2(seq))
