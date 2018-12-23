import networkx as nx
from util import get_data

def parsefunc(s):
    parts = s.split(', ')
    pos = tuple(int(c) for c in parts[0][len("pos=<"):-1].split(','))
    return s.strip()

def get_graph(seq):
    pos = {0}
    stack = []
    starts, ends = {0}, set()
    graph = nx.Graph()
    for c in seq:
        if c == '|':
            ends.update(pos)
            pos = starts
        elif c in 'NESW':
            direction = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[c]
            graph.add_edges_from((p, p + direction) for p in pos)
            pos = {p + direction for p in pos}
        elif c == '(':
            stack.append((starts, ends))
            starts, ends = pos, set()
        elif c == ')':
            pos.update(ends)
            starts, ends = stack.pop()
    return graph

def part1(seq):
    g = get_graph(seq)
    return max(nx.algorithms.shortest_path_length(g, 0).values())

def part2(seq):
    g = get_graph(seq)
    return sum([1 for l in nx.algorithms.shortest_path_length(g, 0).values() if l >= 1000])

seq = get_data(20, parsefunc)[0][1:-1]

print("P1: ", part1(seq))
print("P2: ", part2(seq))
