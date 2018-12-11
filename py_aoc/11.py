from util import get_data
import numpy

def parsefunc(s):
    return s.strip()

gridsn = int(get_data(11, parsefunc)[0])

def power(x, y):
    p = ((((x + 1) + 10) * (y + 1)) + gridsn) * ((x + 1) + 10)
    return (p // 100 % 10) - 5

def max_score(grid, width):
    w = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
    m = int(w.max())
    l = numpy.where(w == m)
    return ((l[0][0] + 1, l[1][0] + 1), m)

def part1(grid):
    return max_score(grid, 3)

def part2(grid):
    maxes = {}
    for width in range(3, 30):
        buff = max_score(grid, width)
        maxes[width] = ((buff[0][0], buff[0][1]), buff[1])
    return sorted(maxes.items(), key=lambda i: i[1][1])[-1]

grid = numpy.fromfunction(power, (300, 300))

print("P1: ", part1(grid))
print("P2: ", part2(grid))
