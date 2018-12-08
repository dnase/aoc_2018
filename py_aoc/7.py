from sets import Set
from util import parse_file
from collections import defaultdict

def parsefunc(s):
    buff = s.split()
    return(buff[1], buff[7])

def collapse_edges(seq, edges):
    buff = sorted(seq)
    traversed = set()
    order = ''
    while buff:
      for i, c in enumerate(buff):
        if not (edges[c] - traversed):
          order += c
          traversed.add(c)
          del buff[i]
          break
    return order

def get_edges(seq):
    edges = defaultdict(set)
    for m in seq:
        edges[m[1]].add(m[0])
    return edges

def thread_scheduler(order, seq):
    edges = get_edges(seq)
    buff = sorted(order)
    done = {}
    threads = [0, 0, 0, 0, 0]
    time = 0
    while buff:
        if all([t > time for t in threads]):
            time = min(threads)
        for i, c in enumerate(buff):
            if all(d in done and done[d] <= time for d in edges[c]):
                for j, d in enumerate(threads):
                    if d <= time:
                        threads[j] = time + ord(c) - 4
                        done[c] = threads[j]
                        break
                del buff[i]
                break
        else:
            time = min([t for t in threads if t > time])
    return max(threads)

def part1(seq):
    edges = get_edges(seq)
    buff = sorted(set(zip(*seq)[0] + zip(*seq)[1]))
    return collapse_edges(buff, edges)

def part2(seq):
    return thread_scheduler(part1(seq), seq)

seq = set(parse_file("../data/input_7", parsefunc))

print("Q1: %s" % part1(seq))
print(part2(seq))
