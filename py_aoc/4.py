import operator
from util import parse_file
from datetime import datetime
from collections import defaultdict

guards = defaultdict(lambda: defaultdict(int))
minutes = defaultdict(int)
def get_data(s):
    ts = datetime.strptime(s[1:17], "%Y-%m-%d %H:%M")
    act = s[19:]
    return [ts, act]

def get_top_minute(guard_id, seq):
    guard_id
    for i, s in enumerate(seq):
        [ts, act] = get_data(s)
        if str(guard_id) in act:
            [ts1, _] = get_data(seq[i+1])
            [ts2, _] = get_data(seq[i+2])
            for i in range(ts1.minute, ts2.minute):
                minutes[i] += 1
            pass
            pass

def parsefunc(s):
    return s.strip()

seq = sorted(parse_file("../data/input_4", parsefunc), key=lambda x: datetime.strptime(x[1:17], "%Y-%m-%d %H:%M"))

for i, s in enumerate(seq):
    [ts, act] = get_data(s)
    if "begins shift" in act:
        guard_id = int(act.split()[1][1:])
        [ts1, _] = get_data(seq[i+1])
        [ts2, _] = get_data(seq[i+2])
        for i in range(ts1.minute, ts2.minute):
            guards[guard_id][i] += 1

        pass
        pass

outarr = []
for g in guards.values():
    for t in g.values():
        outarr.append(t)

print(sorted(outarr))

#guards = sorted(guards.keys(), key=lambda x: guards[x][1])
print(guards)
#sorted_guards = sorted(guards.items(), key=operator.itemgetter())

'''
sorted_guards = sorted(guards.items(), key=operator.itemgetter(1))
get_top_minute(sorted_guards[-1][0], seq)
print(sorted_guards[-1])
sorted_minutes = sorted(minutes.items(), key=operator.itemgetter(1))
print(sorted_minutes)
'''
