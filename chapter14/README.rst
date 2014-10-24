Concurrenct execution
=====================

`threading <https://docs.python.org/3.4/library/threading.html>`_
--------------------------------------------------------------------------

Creating threads
~~~~~~~~~~~~~~~~

- start()
- join()
- ident
- is_alive()
- daemon # TODO

mthreads.py

gui.py

CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use multiprocessing or concurrent.futures.ProcessPoolExecutor. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.

Thread-local data
~~~~~~~~~~~~~~~~~

localdata.py

::

  $ python localdata.py
  Child(Thread-1): x =  [0] mydata.x =  33
  Child(Thread-1): x =  [33] mydata.x =  33
  Main: x =  [33] mydata.x =  0

  Child(Thread-2): x =  [33] mydata.x =  88
  Child(Thread-2): x =  [88] mydata.x =  88
  Main: x =  [88] mydata.x =  0

  Child(Thread-3): x =  [88] mydata.x =  91
  Child(Thread-3): x =  [91] mydata.x =  91
  Main: x =  [91] mydata.x =  0

Locks
~~~~~

Primitive Lock: lock.py

::

  $ python lock.py
  -------------------- mess
  abcdefghijkabclmnodefgpqrhijklstuvwmnoxyzApqrabcdefstuBCDvabcdwxyzAefghiEFGHIJKLMNOPQRSTUVWXYZ
  gBChijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghDEFijklmnopqrstuvwxyzGHjklmnopqrstuvIJKLMNABCwxyzDEFGHABCDOPQRIJKLSTUVWEFGHMNOPXYZ
  QRSTUVWXYZ
  IJKLMNOPQRSTUVWXYZ
  -------------------- neat
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Dead lock: deadlock.py

::

  $ python deadlock.py
  thread1 got the lock1. It will try to get lock2 one second later.
  thread2 got the lock2. It will try to get lock1 one second later.
  2 children are dead locked
  ^C


Reentrant Lock: reentrant_lock.py

::

  $ python reentrant_lock.py
  -------------------- Lock
  23:41:24 Got a lock for the first time.
  23:41:24 It will block self if acquire the same lock again.
  23:41:27 False
  23:41:27 Fail to acquire the same lock in 3 seconds, so thisline will appear 3 seconds later.
  -------------------- RLock
  23:41:27 Got a lock for the first time.
  23:41:27 Got the same lock for the second time.

Condition
~~~~~~~~~

Semaphore
~~~~~~~~~

P and V: acquire and release

producers_and_customers.py

::

  $ python producers_and_customers.py
  producer1 + : 01 .
  producer1 + : 02 ..
  producer1 + : 03 ...
  producer1 + : 04 ....
  producer1 + : 05 .....
  producer1 + : 06 ......
  producer7 + : 07 .......
  producer8 + : 08 ........
  producer2 + : 09 .........
  customer1 - : 08 ........
  customer1 - : 07 .......
  customer1 - : 06 ......
  customer1 - : 05 .....
  customer1 - : 04 ....
  producer5 + : 05 .....
  producer5 + : 06 ......
  producer6 + : 07 .......
  customer5 - : 06 ......
  customer5 - : 05 .....


Event
~~~~~

Timer
~~~~~

Barrier
~~~~~~~

Queue
~~~~~


multiprocessing
---------------


subprocess
----------

concurrent
----------

python-daemon
-------------

supervisor
----------

envoy
-----

