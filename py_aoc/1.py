from util import parse_file
from sets import Set

def parsefunc(s):
    return int(s)

seq = parse_file("../data/input_1", parsefunc)

# question 1
print("Question 1: %d" % sum(seq))

# question 2 - naive solution, but it works
previous_freqs = Set([0])
current_freq = 0
while 1:
    for delta in seq:
        current_freq += delta
        if current_freq in previous_freqs:
            print("Question 2: %d" % current_freq)
            quit()
        previous_freqs.add(current_freq)
