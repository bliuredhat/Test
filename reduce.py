#! /usr/bin/env python
# -*- encoding: utf-8 -*-

#from functools import reduce
#from collections import *
    

def add(a, b):
    return a + b

def reduce(bin_func, seq, init=None):
    lseq = list(seq)
    if init is None:
        res = lseq.pop(0)
    else:
        res = init
    for item in lseq:
        res =bin_func(res, item)

    return res

if __name__ == '__main__':
    arr = range(1,100)
    print arr
    res = reduce(add, arr)
    print "The result is %s"%res
