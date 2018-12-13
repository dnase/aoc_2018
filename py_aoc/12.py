import re
from util import get_data
from collections import defaultdict

def parsefunc(s):
    return s.strip()

def score(state):
    total = 0
    for i, s in state.items():
        if s == "#":
            total += i
    return total

def get_initial_state(seq):
    state = defaultdict(lambda: '.')
    rules = {}
    for line in seq:
        if "initial state" in line:
            for i, c in enumerate(line):
                if c == '#':
                    state[i] = '#'
                else:
                    state[i] = '.'
            for i in range(-100,0):
                state[i] = '.'
        elif "=>" in line:
            rules[line[:4]] = line[9]
    return (state, rules)

def mutate(state, rules):
    minval = min(state.keys())
    maxval = max(state.keys())
    for i in range(minval, maxval):
        for rule, res in rules.items():
            v = True
            for j, k in enumerate(rule):
                if not (k == state[i + j]):
                    v = False
                    break
            if v:
                state[i + 2] = res
    return state

def generation(state, rules, n):
    buff = state
    for i in range(1, n + 1):
        buff = mutate(buff, rules)
        #print ''.join(buff.values())
    return buff

def part1(seq):
    (state, rules) = get_initial_state(seq)
    buff = generation(state, rules, 20)
    return score(buff)

def part2(seq):
    (state, rules) = get_initial_state(seq)
    buff = generation(state, rules, 2000)
    return score(buff)

seq = get_data(12, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2(seq))
