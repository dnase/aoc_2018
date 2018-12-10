import os.path
import requests
# common utilities for Advent of Code
def get_data(exnum, parsefunc):
    filepath = "../data/input_%d" % exnum
    if not os.path.isfile(filepath):
        token = open("../data/token").read().strip()
        cookies = {'session': token}
        urlpath = "https://adventofcode.com/2018/day/%d/input" % exnum
        fh = open(filepath, 'w')
        fh.write(requests.get(urlpath, cookies=cookies).text)
    return [parsefunc(s) for s in open(filepath).readlines()]
