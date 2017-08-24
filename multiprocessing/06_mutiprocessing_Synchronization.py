from multiprocessing import Process, Lock
from time import ctime, sleep

def f(l, i):
    l.acquire()
    print 'hello world', i, ctime()
    sleep(1)
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()