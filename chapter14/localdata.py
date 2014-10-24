import random
import threading

x = [0]

mydata = threading.local()
mydata.x = 0

def mythread():
    mydata.x = random.randint(1, 100)
    print('Child(%s):' % threading.current_thread().name,
        "x = ", x, 
        "mydata.x = ", mydata.x,
        )
    x[0] = mydata.x
    print('Child(%s):' % threading.current_thread().name,
        "x = ", x, 
        "mydata.x = ", mydata.x,
        )

for i in range(3):
    t = threading.Thread(target=mythread)
    t.start()
    t.join()
    print("Main: x = ", x, "mydata.x = ", mydata.x)
    print()
