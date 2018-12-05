from util import parse_file

def parsefunc(s):
    return s.strip()

print(parse_file("../data/input_5", parsefunc))
