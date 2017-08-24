#! /usr/bin/env python

import itertools

def map(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq

def add(n):
    return n + 1

if __name__ == '__main__':
    arr = range(1,10)
    
    arr_res = map(add, arr)
    print "The result arr: %s" % arr_res