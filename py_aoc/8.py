from sys import setrecursionlimit
from sets import Set
from util import parse_file
from collections import defaultdict

def total_metadata(seq, i, metadata):
    num_children = seq[i]
    num_meta_ent = seq[i + 1]
    i += 2
    for j in range(num_children):
        (i, _) = total_metadata(seq, i, metadata)
    for j in range(num_meta_ent):
        metadata.append(int(seq[i + j]))
    return (i + num_meta_ent, sum(metadata))

def root_node_value(seq):
    [num_children, num_meta_ent] = seq[:2]
    seq = seq[2:]
    buff = []
    for i in range(num_children):
        s, seq = root_node_value(seq)
        buff.append(s)
    if num_children == 0:
        return (sum(seq[:num_meta_ent]), seq[:num_meta_ent])
    else:
        return (sum(buff[x - 1] for x in seq[:num_meta_ent] if x > 0 and x <= len(buff)), seq[num_meta_ent:])

def parsefunc(s):
    return s.strip()

def part1(seq):
    return total_metadata(seq, 0, [])[1]

def part2(seq):
    return root_node_value(seq)[0]

seq = [int(c) for c in parse_file("../data/input_8", parsefunc)[0].split()]

print("P1: ", part1(seq))
print("P2: ", part2(seq))
