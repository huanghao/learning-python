from time import sleep, time
from random import random, seed
from threading import Thread
from queue import Queue


class Product: pass

def producer(pid):
    while 1:
        sleep(random())
        q.put(Product())
        # qsize ?
        print('producer%d + : %02d %s' % (
            pid, q.qsize(), '.'*q.qsize()))


def customer(cid):
    while 1:
        p = q.get()
        del p
        sleep(random())
        print('customer%d - : %02d %s' % (
            cid, q.qsize(), '.'*q.qsize()))


seed(time())

q = Queue(13)


for i in range(5):
    Thread(target=producer, args=(i+1,)).start()
for i in range(5):
    Thread(target=customer, args=(i+1,)).start()
