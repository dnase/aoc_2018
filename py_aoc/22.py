import networkx as nx
from util import get_data

def parsefunc(s):
    if 'depth' in s:
        return int(s[7:].strip())
    elif 'target' in s:
        return tuple([int(c) for c in s[8:].strip().split(',')])

def generate_graph_grid(depth, corner):
    return {c: v[2] for c, v in (generate_grid(depth, corner)).items()}

def generate_grid(depth, corner):
    grid = {}
    for y in range(0, corner[1] + 1):
        for x in range(0, corner[0] + 1):
            if (x, y) in [(0, 0), corner]:
                geo = 0
            elif x == 0:
                geo = y * 48271
            elif y == 0:
                geo = x * 16807
            else:
                geo = grid[(x-1, y)][1] * grid[(x, y-1)][1]
            ero = (geo + depth) % 20183
            risk = ero % 3
            grid[(x, y)] = (geo, ero, risk)
    return grid

def dijkstra(grid, corner, target):
    rocky, wet, narrow = 0, 1, 2
    torch, gear, neither = 0, 1, 2
    valid_items = {rocky: (torch, gear), wet: (gear, neither), neither: (torch, neither)}
    valid_regions = {torch: (rocky, narrow), gear: (rocky, wet), neither: (wet, narrow)}
    graph = nx.Graph()
    for y in range(0, corner[1] + 1):
        for x in range(0, corner[0] + 1):
            items = valid_items[grid[(x, y)]]
            graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x <= corner[0] and 0 <= new_y <= corner[1]:
                    new_items = valid_items[grid[(new_x, new_y)]]
                    for item in set(items).intersection(set(new_items)):
                        graph.add_edge((x, y, item), (new_x, new_y, item), weight=1)
    return nx.dijkstra_path_length(graph, (0, 0, torch), (target[0], target[1], torch))

def part1(seq):
    depth, target = seq[0], seq[1]
    g = generate_grid(depth, target)
    return sum([v[2] for v in g.values()])

def part2(seq):
    depth, target = seq[0], seq[1]
    corner = (target[0] + 100, target[1] + 100)
    g = generate_graph_grid(depth, corner)
    return dijkstra(g, corner, target)

seq = get_data(22, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2(seq))
