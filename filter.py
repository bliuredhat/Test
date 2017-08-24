#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# 这是filter函数

def odd(n):
    return n % 2

def filter(bool_func, seq):
    filtered_seq = []
    for eachItem in seq:
        if bool_func(eachItem):
            filtered_seq.append(eachItem)
    return filtered_seq

if __name__ == '__main__':
    arr = range(1, 10)
    print "The oring value: %s" % arr
    res = filter(odd, arr)

    print "The filter values: %s" % res