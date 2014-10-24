import random
from threading import Thread, current_thread


class IOThread(Thread):
    def run(self):
        input("Press enter to continue ...")
        print(self.name, 'exit')


def computing_thread(times):
    name = current_thread().name
    for i in range(times):
        print(name, 'working...')
        working()
    print(name, 'exit')


def working():
    i = 0
    while i < 10000000:
        i += 1


threads = [IOThread()] + [
    Thread(target=computing_thread, args=(random.randint(2, 4),))
        for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print('Main finish')
