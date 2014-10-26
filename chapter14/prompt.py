from threading import Timer, current_thread

def timeout():
    """
    Callback will be called in another thread
    """
    print(current_thread(), 'Time is out')

Timer(3, timeout).start()
data = input('%s: Input some thing in 3 seconds: ' % current_thread())
print(data)
