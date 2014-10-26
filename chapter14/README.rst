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

TODO

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

wait4parent.py

::

  $ python wait4parent.py
  10:17:48 Child: wait for the event
  10:17:48 Parent: wait a moment
  10:17:51 Parent: now child can go on
  10:17:51 Child: start my job

Timer
~~~~~

prompt.py

::

  def hello():
      print("hello, world")

  t = Timer(30.0, hello)
  t.start() # after 30 seconds, "hello, world" will be printed


Barrier
~~~~~~~

::

  b = Barrier(2, timeout=5)

  def server():
      start_server()
      b.wait()
      while True:
          connection = accept_connection()
          process_server_connection(connection)

  def client():
      b.wait()
      while True:
          connection = make_connection()
          process_client_connection(connection)


Queue
~~~~~

- Queue: FIFO
- LifoQueue: LIFO
- PriorityQueue: The lowest valued entries are retrieved first

worker.py: a simpler solution of producers and customers question

multiprocessing
---------------

`Global Interpreter Lock <https://docs.python.org/3.4/glossary.html#term-global-interpreter-lock>`_

Process(target, args)

- start()
- run()
- join()
- name
- is_alive()
- daemon
- pid
- exitcode
- terminate()

`Programming guidelines <https://docs.python.org/3.4/library/multiprocessing.html#programming-guidelines>`_


Contexts and start methods
~~~~~~~~~~~~~~~~~~~~~~~~~~

- spawn
- fork
- forkserver

Exchanging objects
~~~~~~~~~~~~~~~~~~

Queue

Pipe

SimpleQueue

Connection

Listeners and Clients

Authentication keys

Synchronization
~~~~~~~~~~~~~~~

Lock

Barrier

BoundedSemaphore

Condition

Event

Semaphore

Sharing states
~~~~~~~~~~~~~~

Shared memory

Server process

Shared ctypes Objects

Managers

Proxy

Cleanup

Pool of workers
~~~~~~~~~~~~~~~



subprocess
----------

This module intends to replace several older modules and functions:

  os.system
  os.spawn*

Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())

- poll()
- wait()
- communicate()
- send_signal()
- terminate()
- kill()
- args
- stdin
- stdout
- stderr
- pid
- returncode

- call(args, \*, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
- check_call
- check_output

`Replace older functions with subprocess <https://docs.python.org/3.4/library/subprocess.html#replacing-older-functions-with-the-subprocess-module>`_

shlex

concurrent
----------

ThreadPoolExecutor

ProcessPoolExecutor

Future

future/promise

sched
-----

`python-daemon <https://pypi.python.org/pypi/python-daemon/>`_
--------------------------------------------------------------

Correct daemon behaviour

According to Stevens in [stevens]_ §2.6, a program should perform the following steps to become a Unix daemon process.

- Close all open file descriptors.
- Change current working directory.
- Reset the file access creation mask.
- Run in the background.
- Disassociate from process group.
- Ignore terminal I/O signals.
- Disassociate from control terminal.
- Don't reacquire a control terminal.
- Correctly handle the following circumstances:
- Started by System V init process.
- Daemon termination by SIGTERM signal.
- Children generate SIGCLD signal.


See: `PEP 3143 <http://legacy.python.org/dev/peps/pep-3143/>`_ - Standard daemon process library

supervisor
----------

http://supervisord.org/


.. [stevens] Unix Network Programming, W. Richard Stevens, 1994 Prentice Hall.
