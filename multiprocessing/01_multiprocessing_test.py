#! /etc/bin/env python

from multiprocessing import Pool
from time import sleep, ctime

def f(x):
    print "start time :", ctime()
    sleep(1)
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    #import ipdb; ipdb.set_trace()
    print(p.map(f, [1, 2, 3]))
