from util import parse_file

def parsefunc(s):
    return s.strip()

seq = parse_file("../data/input_2", parsefunc)
count2 = 0
count3 = 0

def check2(instr):
    for s in instr:
        if instr.count(s) == 2:
            return 1
    return 0

def check3(instr):
    for s in instr:
        if instr.count(s) == 3:
            return 1
    return 0

def levenshtein(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    d = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        d_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                d_.append(d[i1])
            else:
                d_.append(1 + min((d[i1], d[i1 + 1], d_[-1])))
        d = d_
    return d[-1]

def intersection(s1, s2):
    if len(s1) == len(s2):
        outbuff = ""
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                outbuff += s1[i]
        return outbuff
    return false

for s in seq:
    count2 += check2(s)
    count3 += check3(s)

print("Q1: %d" % (count2 * count3))

for s in seq:
    for subs in seq:
        if levenshtein(s, subs) == 1:
            res = intersection(s, subs)
            print("Q2: %s" % res)
            quit()
