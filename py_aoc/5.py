import operator
from util import get_data

global CHARSET
CHARSET = "abcdefghijklmnopqrstuvwxyz"

def parsefunc(s):
    return s.strip()

seq = get_data(5, parsefunc)[0]

def reduce_sequence(seq):
    check_len = len(seq)
    for c in CHARSET:
		seq = seq.replace(c+c.upper(),"").replace(c.upper()+c,"")
    seq_len = len(seq)
    return ((seq_len != check_len), seq)

# part 1
def part1(seq):
    buff = seq
    recur = True
    while recur:
        (recur, buff) = reduce_sequence(buff)
    return len(buff)

# part 2
def part2(seq):
    lengths = {}
    for c in CHARSET:
        buff = seq.replace(c,"").replace(c.upper(),"")
        recur = True
        while recur:
            (recur, buff) = reduce_sequence(buff)
        lengths[c] = len(buff)
    lengths_sorted = sorted(lengths.items(), key=operator.itemgetter(1))
    return lengths_sorted[0][1]



print("Q1: %d" % part1(seq))
print("Q2: %d" % part2(seq))
