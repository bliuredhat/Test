#! /usr/bin/evn python
#--encoding:utf-8--

import gevent
import random

def task(pid):
    """
    Some non-deterministic task
    :param pid:
    :return:
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done'%pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task,i) for i in xrange(10)]
    gevent.joinall(threads)

if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()