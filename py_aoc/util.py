import urllib2
import os.path
import requests
# common utilities for Advent of Code
def get_data(exnum, parsefunc):
    filepath = "../data/input_%d" % exnum
    if not os.path.isfile(filepath):
        cookies = {'session': '53616c7465645f5f937a9f5b169013c44a6d4217565e2d9cbdb67ea279ae9dcbe2c84bd90a96e85174a35c257b6a4b94'}
        urlpath = "https://adventofcode.com/2018/day/%d/input" % exnum
        fh = open(filepath, 'w')
        fh.write(requests.get(urlpath, cookies=cookies).text)
    return [parsefunc(s) for s in open(filepath).readlines()]
