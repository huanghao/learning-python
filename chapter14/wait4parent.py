import time
import threading


def log(*msg):
    print(time.strftime('%H:%M:%S'), *msg)


def child():
    log('Child: wait for the event')
    event.wait()
    log('Child: start my job')


event = threading.Event()
t = threading.Thread(target=child)
t.start()

log('Parent: wait a moment')
time.sleep(3)
log('Parent: now child can go on')
event.set()

t.join()
