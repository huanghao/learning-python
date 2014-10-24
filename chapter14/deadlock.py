import time
import threading


def thread1():
    with lock1:
        print('thread1 got the lock1. '
            'It will try to get lock2 one second later.')
        time.sleep(1)
        with lock2:
            assert False, "Code won't get here"


def thread2():
    with lock2:
        print('thread2 got the lock2. '
            'It will try to get lock1 one second later.')
        time.sleep(1)
        with lock1:
            assert False, "Code won't get here"


lock1 = threading.Lock()
lock2 = threading.Lock()

threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()
print('2 children are dead locked')
