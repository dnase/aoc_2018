import operator
from util import parse_file

def parsefunc(s):
    return s.strip()

seq = parse_file("../data/input_5", parsefunc)[0]

# part 1
def reduce_sequence(seq):
    check_len = len(seq)
    for c in "abcdefghijklmnopqrstuvwxyz":
		seq = seq.replace(c+c.upper(),"").replace(c.upper()+c,"")
    seq_len = len(seq)
    return ((seq_len != check_len), seq)

# part 2
def part2(seq):
    lengths = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        buff = seq.replace(c,"").replace(c.upper(),"")
        recur = True
        while recur:
            (recur, buff) = reduce_sequence(buff)
        lengths[c] = len(buff)
    return lengths

buff1 = seq
recur = True
while recur:
    (recur, buff1) = reduce_sequence(buff1)

print(len(buff1))

p2 = part2(seq)
sorted_p2 = sorted(p2.items(), key=operator.itemgetter(1))
print(sorted_p2[0][1])
