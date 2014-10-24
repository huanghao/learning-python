import sys
import time
import string
import threading


def synchronize(lock):
    def decorator(thread_func):
        def synced_thread(*args, **kw):
            with lock:
                return thread_func(*args, **kw)
        return synced_thread
    return decorator


def mythread():
    for c in string.ascii_letters:
        sys.stdout.write(c)
        time.sleep(0)
    sys.stdout.write('\n')


def run(target):
    pool = [threading.Thread(target=target) for _ in range(5)]
    for t in pool:
        t.start()
    for t in pool:
        t.join()


def mess():
    run(mythread)


def neat():
    lock = threading.Lock()
    run(synchronize(lock)(mythread))


print('-'*20, 'mess')
mess()
print('-'*20, 'neat')
neat()
