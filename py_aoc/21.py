from util import get_data

def parsefunc(s):
    return s.strip()

def activationfunc(m, p1=True):
    seen = set()
    c = 0
    last_unique_c = -1
    while True:
        a = c | 65536
        c = m
        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if p1:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256

def part1(m):
    return activationfunc(m)

def part2(m):
    return activationfunc(m, False)

m = int(get_data(21, parsefunc)[8].split(' ')[1])

print("P1: ", part1(m))
print("P2: ", part2(m))
