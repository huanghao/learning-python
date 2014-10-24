Concurrenct execution
=====================

`Multiple threading <https://docs.python.org/3.4/library/threading.html>`_
--------------------------------------------------------------------------

Creating threads
~~~~~~~~~~~~~~~~

- start()
- join()
- ident
- is_alive()

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

Dead lock

Reentrant Lock:



- multiprocessing
- subprocess
- python-daemon
- supervisor
- envoy
