"""
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used the names P() and V() instead of acquire() and release()).
"""
import time
import random
import threading


random.seed(time.time())

def P(semaphore):
    return semaphore.acquire()

def V(semaphore):
    return semaphore.release()


class Product: pass


def producer(pid):
    while 1:
        P(vacancy)
        P(mutex)

        time.sleep(random.random() / 3)
        buf.append(Product)
        print('producer{} + : {:02d} {}'.format(pid, len(buf), '.'*len(buf)))

        V(mutex)
        V(full)


def customer(cid):
    while 1:
        P(full)
        P(mutex)

        product = buf.pop()
        del product
        time.sleep(random.random() / 3)
        print('customer{} - : {:02d} {}'.format(cid, len(buf), '.'*len(buf)))

        V(mutex)
        V(vacancy)



buf_sz = 13
buf = []

mutex = threading.Semaphore(1)
full = threading.Semaphore(0)
vacancy = threading.Semaphore(buf_sz)

number_of_producers = 8
number_of_customers = 5


for i in range(number_of_producers):
    t = threading.Thread(target=producer, args=(i+1,))
    t.start()

for i in range(number_of_customers):
    t = threading.Thread(target=customer, args=(i+1,))
    t.start()

