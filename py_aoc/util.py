# common utilities for Advent of Code
def parse_file(filepath, parsefunc):
    return [parsefunc(s) for s in open(filepath).readlines()]
