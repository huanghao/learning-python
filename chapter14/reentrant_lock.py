import time
import threading


def log(*args):
    print(time.strftime('%H:%M:%S'), *args)


def lock_again():
    lock = threading.Lock()
    with lock:
        log('Got a lock for the first time.')
        log('It will block self if acquire the same lock again.')
        log(lock.acquire(timeout=3))
        log('Fail to acquire the same lock in 3 seconds, so this'
            'line will appear 3 seconds later.')


def reentrant_lock():
    lock = threading.RLock()
    with lock:
        log('Got a lock for the first time.')
        with lock:
            log('Got the same lock for the second time.')


print('-'*20, 'Lock')
lock_again()
print('-'*20, 'RLock')
reentrant_lock()
