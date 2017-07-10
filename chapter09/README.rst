A tour of std libs
==================

:Text processing:
  string, re, difflib, textwrap, unicodedata, stringprep, readline, rlcompleter

:Binary data services:
  struct, codecs

:Data types:
  **datetime**, calendar, **collections**, collections.abc, **heapq**, **bisect**,
  **array**, **weakref**, **types**, **copy**, pprint, reprlib, enum

:Numeric and Math:
  numbers, math, cmath, decimal, fractions, random, statistics

:Functional programming:
  itertools, functools, operator

:File and directory access:
  pathlib, **os.path**, fileinput, stat, filecmp, **tempfile**, **glob**, fnmatch,
  linecache, **shutil**, macpath

:Data peristence:
  pickle, copyreg, shelve, marshal, dbm, sqlite3

:Data compression:
  zlib, gzip, bz2, lzma, zipfile, tarfile

:File formats:
  csv, configparser, **netrc**, xdrlib, plistlib

:Cryptographic:
  **hashlib**, hmac

:OS:
  **os**, **io**, **time**, **argparse**, getopt, **logging**, getpass, curses,
  **platform**, **errno**, ctypes

:Concurrent:
  threading, multiprocessing, concurrent.futures, subprocess, sched, queue, dummy_threading

:Networking:
  socket, ssl, select, selectors, asyncio, asyncore, asynchat, signal, mmap

:Internet:
  email, json, mailcap, mailbox, mimetypes, base64, binhex, binascii, quopri, uu

:Structured markup:
  html, xml.etree, xml.dom, xml.sax

:Internet protocols:
  webbrowser, cgi, wsgiref, urllib.request, urllib.response, urllib.parse, urllib.error, urllib.robotparser, http, fptlib, poplib, imaplib, nntplib, smtplib, smtpd, telnetlib, uuid, socketserver, http.server, http.cookies, http.cookiejar, xmlrpc, ipaddress

:Multimedia:
  audioop, aifc, sunau, wave, chunk, colorsys, imghdr, sndhdr, ossaudiodev

:I18n:
  gettext, locale

:Porgram frameworks:
  turtle, cmd, shlex

:GUI:
  tkinter

:Development tools:
  pydoc, doctest, unittest, unittest.mock, test

:Debugging and profiling:
  bdb, faulthandler, pdb, profile, timeit, trace, tracemalloc

:Packaing and distribution:
  distutils, ensurepip, venv

:Runtime:
  **sys**, sysconfig, **builtins**, __main__, warnings, **contextlib**, **abc**,
  **atexit**, **traceback**, __future__, gc, inspect, site, fpectl

:Custom python interpreters:
  code, codeop

:Importing:
  zipimport, pkgutil, modulefinder, runpy, **importlib**

:Language:
  parser, ast, symtable, symbol, token, keyword, tokenize, tabnanny, pyclbr, py_compile, compileall, dis, pickletools

:Misc:
  formatter

:MS:
  msilib, msvcrt, winreg, winsound

:Unix:
  posix, pwd, spwd, grp, crypt, termios, tty, pty, fcntl, pipes, resource, nis, syslog

:Superseded:
  optparse, imp

Where you can find those standard libs ?

  sys.path

  /usr/lib/python2.7
  /usr/lib/python3.4

`datetime <https://docs.python.org/3/library/datetime.html>`_ - Basic date and time types
-----------------------------------------------------------------------------------------

There are two kinds of date and time objects: "naive" and "aware".

An aware object has sufficient knownledge of applicable algorithmic and political
time adjustments, such as time zone and daylight saving time information, to locate
oitself relative to other aware objects.

Availabe types

- datetime.date
- datetime.time
- datetime.dateteime
- datetime.timedelta
- datetime.tzinfo: An abstract base class for time zone information objects.
- datetime.timezone: A class that implements the tzinfo abc as a fixed offset from the UTC.

Objects of these types are immutable.

Objects of the date type are always naive.

Naive::

  >>> import datetime
  >>> now = datetime.datetime.now()                   # Date and Time
  >>> now
  datetime.datetime(2014, 10, 21, 7, 32, 44, 964045)
  >>> now.date()
  datetime.date(2014, 10, 21)
  >>> now.time()
  datetime.time(7, 32, 44, 964045)

  >>> day = datetime.date(2012, 12, 12)               # Date
  >>> day.year, day.month, day.day, day.isoweekday(), day.isoformat()
  (2012, 12, 12, 3, '2012-12-12')
  >>> tm = datetime.time(19, 30, 00)                  # Time
  >>> tm.hour, tm.minute, tm.second, tm.isoformat()
  (19, 30, 0, '19:30:00')

  >>> past = dateteime.datetime.now() - now           # Time delta
  >>> past, str(past), past.total_seconds()
  (datetime.timedelta(0, 615, 431954), '0:10:15.431954', 615.431954)

  >>> day.strftime('%b %d %Y %a')                     # Format
  'Dec 12 2012 Wed'
  >>> timestr = '[Sun Oct 19 08:10:01 2014]'          # Parse
  >>> datetime.datetime.strptime(timestr, '[%a %b %d %H:%M:%S %Y]')
  datetime.datetime(2014, 10, 19, 8, 10, 1)

Aware::

  >>> beijing = timezone(timedelta(hours=8), 'Asia/Shanghai')
  >>> finland = timezone(timedelta(hours=2), 'Europe/Helsinki')

  >>> t1 = datetime.datetime(2014, 10, 6, 15, 0, 0, tzinfo=beijing)
  >>> str(t1), t1.tzname()
  ('2014-10-06 15:00:00+08:00', 'Asia/Shanghai')

  >>> t2 = t1.astimezone(finland)
  >>> str(t2), t2.tzname()
  ('2014-10-06 09:00:00+02:00', 'Europe/Helsinki')

`collections <https://docs.python.org/3/library/collections.html>`_ - Container datetypes
-----------------------------------------------------------------------------------------

============ ====================================================================
namedtuple() factory function for creating tuple subclasses with named fields
deque        list-like container with fast appends and pops on either end
ChainMap     dict-like class for creating a single view of multiple mappings
Counter      dict subclass for counting hashable objects
OrderedDict  dict subclass that remembers the order entries were added
defaultdict  dict subclass that class a factory function to supply missing values
============ ====================================================================

namedtuple()::

  >>> from collections import namedtuple
  >>> Person = namedtuple('Person', ['name', 'age', 'gender'])
  >>> bob = Person('Bob', 30, 'male')
  >>> jane = Person(name='Jane', gender='female', age=29)
  >>> bob, bob[2]
  (Persion(name='Bob', age=30, gender='male'), 'male')
  >>> type(jane), jane.age
  (<class '__main__.Persion'>, 29)

  >>> bob._asdict()
  OrderedDict([('name', 'Bob'), ('age', 30), ('gender', 'male')])
  >>> bob._replace(name='Tom', age=52)
  Persion(name='Tom', age=52, gender='male')

::

  >>> class Person(namedtuple('Person', ['name', 'age', 'gender'])):
  ...   __slots__ = ()
  ...   @property
  ...   def lastname(self):
  ...     return self.name.split()[-1]
  ... 
  >>> john = Person('John Lennon', 75, 'male')
  >>> john.lastname
  'Lennon'

deque: double-ended queue
-------------------------

Deques support thread-safe, memory efficient appends and pops from either side
of the deque with approximately the same O(1) performance in either direction.

=============== =========== ===== ============ =====
Operation       list        Big O deque        Big O
=============== =========== ===== ============ =====
Add in the head l.insert(0) O(n)  d.appendleft O(1)
Add in the tail l.append()  O(1)  d.append     O(1)
Del in the head l.pop(0)    O(n)  d.popleft    O(1)
Del in the tail l.pop()     O(1)  d.pop        O(1)
=============== =========== ===== ============ =====

::

  def timing(initial, setup, testing, times=3):
      print('Testing the following code for {} times ...\n{}'.format(times, testing.strip()))
      namespace = {}
      exec(initial, namespace)

      av = 0
      for i in range(times):
          exec(setup, namespace)

          begin = time.time()
          exec(testing, namespace)
          cost = time.time() - begin

          print('{}: {}'.format(i + 1, cost))
          av += cost
      print('av: {}\n'.format(av / times))

::

  >>> timing('data = list(range(10**5))', 'l = []', '''
  ... for i in data:
  ...   l.insert(0, i)    # O(n)
  ... ''')
  Testing the following code for 3 times ...
  for i in data:
    l.insert(0, i)
  1: 3.9300358295440674
  2: 4.109051704406738
  3: 4.1024134159088135
  av: 4.04716698328654

::

  $ python timing.py
  Testing the following code for 3 times ...
  for i in data:
    l.insert(0, i)        # O(N)
  av: 4.171613295873006

  Testing the following code for 3 times ...
  for i in data:
    l.append(i)           # O(1)
  av: 0.012801011403401693

  Testing the following code for 3 times ...
  for i in data:
    d.appendleft(i)       # O(1)
  av: 0.014629840850830078

  Testing the following code for 3 times ...
  for i in data:
    d.append(i)           # O(1)
  av: 0.014315048853556315

  Testing the following code for 3 times ...
  for _ in data:
    l.pop(0)              # O(n)
  av: 1.6093259652455647

  Testing the following code for 3 times ...
  for _ in data:
    l.pop()               # O(1)
  av: 0.014542102813720703

  Testing the following code for 3 times ...
  for _ in data:
    d.popleft()           # O(1)
  av: 0.011040687561035156

  Testing the following code for 3 times ...
  for _ in data:
    d.pop()               # O(1)
  av: 0.011482477188110352

See `Time complexity <https://wiki.python.org/moin/TimeComplexity>`_

`Chainmap <https://docs.python.org/3.4/library/collections.html#chainmap-objects>`_

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. 

Example of simulating Python’s internal lookup chain::

  import builtins
  pylookup = ChainMap(locals(), globals(), vars(builtins))


`Counter <https://docs.python.org/3.4/library/collections.html#counter-objects>`_

A counter tool is provided to support convenient and rapid tallies. For example::

  >>> from collections import Counter
  >>> words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
  >>> cnt = Counter(words)
  >>> cnt
  Counter({'blue': 3, 'red': 2, 'green': 1})
  >>> cnt.most_common(2)
  [('blue', 3), ('red', 2)]


`OrderedDict <https://docs.python.org/3.4/library/collections.html#ordereddict-objects>`_

Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.
When iterating over an ordered dictionary, the items are returned in the order their keys were first added.

::

  >>> # regular unsorted dictionary
  >>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

  >>> # dictionary sorted by key
  >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
  OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

  >>> assert list(o.keys()) == sorted(d.keys())

`defaultdict <https://docs.python.org/3.4/library/collections.html#defaultdict-objects>`_

Dictionary with default value::

  >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
  >>> d = defaultdict(list)
  >>> for k, v in s:
  ...     d[k].append(v)
  ...
  >>> list(d.items())
  [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

This technique is simpler and faster than an equivalent technique using dict.setdefault()::

  >>> d = {}
  >>> for k, v in s:
  ...     d.setdefault(k, []).append(v)
  ...
  >>> list(d.items())
  [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


`heapq <https://docs.python.org/3.4/library/heapq.html>`_ - Heap queue algorithm
--------------------------------------------------------------------------------

::

  >>> def heapsort(iterable):
  ...     'Equivalent to sorted(iterable)'
  ...     h = []
  ...     for value in iterable:
  ...         heappush(h, value)
  ...     return [heappop(h) for i in range(len(h))]
  ...
  >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

This module provides an implementation of the min heap queue algorithm, also known as the priority queue algorithm.

`bisect <https://docs.python.org/3.4/library/bisect.html>`_ - Array bisection algorithm
---------------------------------------------------------------------------------------

::

  import bisect
  import random

  # Use a constant see to ensure that we see
  # the same pseudo-random numbers each time
  # we run the loop.
  random.seed(1)

  # Generate 20 random numbers and
  # insert them into a list in sorted
  # order.
  l = []
  for i in range(1, 20):
      r = random.randint(1, 100)
      position = bisect.bisect(l, r)
      bisect.insort(l, r)
      print('{:=2} {:=2} {}'.format(r, position, l))

`array <https://docs.python.org/3.4/library/array.html>`_ - Efficient arrays of numeric values
----------------------------------------------------------------------------------------------

array.array is useful when you need a homogeneous C array of data for reasons other than doing math.

::

  array('l')
  array('u', 'hello \u2641')
  array('l', [1, 2, 3, 4, 5])
  array('d', [1.0, 2.0, 3.14])

See also: `bytearray vs array <http://stackoverflow.com/questions/11882988/python-bytearray-vs-array>`_

`weakref <https://docs.python.org/3.4/library/weakref.html>`_ - Weak references
-------------------------------------------------------------------------------

A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.

A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.

Not all objects can be weakly referenced; those objects which can include class instances, functions written in Python (but not in C), instance methods, sets, frozensets, some file objects, generators, type objects, sockets, arrays, deques, regular expression pattern objects, and code objects.

Several built-in types such as list and dict do not directly support weak references but can add support through subclassing::

  class Dict(dict):
      pass

  obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable

Other built-in types such as tuple and int do not support weak references even when subclassed (This is an implementation detail and may be different across various Python implementations.).

Extension types can easily be made to support weak references;
see `Weak Reference Support <https://docs.python.org/3.4/extending/newtypes.html#weakref-support>`_.

weakref.ref

::

  import weakref

  class BigObject:
      def __del__(self):
          print('Deleting {}'.format(self))

  o = BigObject()
  r = weakref.ref(o)

  print('obj: {}'.format(o))
  print('ref: {}'.format(r))
  print('r(): {}'.format(r()))

  del o
  print('r(): {}'.format(r()))

::

  obj: <__main__.BigObject instance at 0x1036f43f8>
  ref: <weakref at 0x1036e5c58; to 'instance' at 0x1036f43f8>
  r(): <__main__.BigObject instance at 0x1036f43f8>
  Deleting <__main__.BigObject instance at 0x1036f43f8>
  r(): None

::

  ...
  def callback(ref):
      print('Callback {}'.format(ref))
  ...
  r = weakref.ref(o, callback)
  ...

::

  obj: <__main__.BigObject instance at 0x10237a4d0>
  ref: <weakref at 0x10236bc58; to 'instance' at 0x10237a4d0>
  r(): <__main__.BigObject instance at 0x10237a4d0>
  Callback <weakref at 0x10236bc58; dead>
  Deleting <__main__.BigObject instance at 0x10237a4d0>
  r(): None

weakref.proxy

  ::

    p = weakref.proxy(o)
    try:
      p.attr
    except ReferenceError:
      ...

weakref.WeakValueDictionary #TODO

`types <https://docs.python.org/3.4/library/types.html>`_ - Dynamic type creation and names for built-in types
--------------------------------------------------------------------------------------------------------------

::

  >>> import types
  >>> type(lambda : ...) is types.FunctionType
  True

`copy <https://docs.python.org/3.4/library/copy.html>`_ - Shallow and deep copy operations
------------------------------------------------------------------------------------------

::

  >>> import copy
  >>> class Object: pass
  ...
  >>> l1 = [1, [2, Object()]]
  >>> l2 = l1
  >>> l3 = copy.copy(l1)
  >>> l4 = copy.deepcopy(l1)

  >>> l3[0] = 3
  >>> l3[1][0] = 4

  >>> l1
  [1, [4, <__main__.Object object at 0x107d2a278>]]
  >>> l2
  [1, [4, <__main__.Object object at 0x107d2a278>]]
  >>> l3
  [3, [4, <__main__.Object object at 0x107d2a278>]]
  >>> l4
  [1, [2, <__main__.Object object at 0x107d2a978>]]

`os.path <https://docs.python.org/3.4/library/os.path.html>`_ - Common pathname manipulations
---------------------------------------------------------------------------------------------

::

  >>> import os.path
  >>> os.path.sep, os.path.extsep, os.path.pardir, os.path.curdir
  ('/', '.', '..', '.')

  >>> os.path.dirname('/one/two/three'), os.path.basename('/one/two/three')
  ('/one/two', 'three')
  >>> os.path.join('one', 'two', 'three')
  'one/two/three'
  >>> os.path.splitext('/path/file.ext')
  ('/path/file', '.ext')

  >>> os.path.expanduser('~/file.txt')
  '/Users/huanghao/file.txt'            # Mac

  >>> os.getcwd()
  '/tmp'
  >>> os.path.abspath('file.txt')
  '/tmp/file.txt'
  >>> os.path.realpath('file.txt')
  '/tmp/file.txt'

  >>> os.path.isdir('/tmp'), os.path.isfile('/etc/hosts'), os.path.islink('/var'), os.path.exists('/dev'), os.path.ismount('/dev')
  (True, True, True, True, True)

`tempfile <https://docs.python.org/3.4/library/tempfile.html>`_ - Generate temporary files and directories
----------------------------------------------------------------------------------------------------------

::

  >>> import tempfile

  # create a temporary file and write some data to it
  >>> fp = tempfile.TemporaryFile()
  >>> fp.write(b'Hello world!')
  # read data from file
  >>> fp.seek(0)
  >>> fp.read()
  b'Hello world!'
  # close the file, it will be removed
  >>> fp.close()

  # create a temporary file using a context manager
  >>> with tempfile.TemporaryFile() as fp:
  ...     fp.write(b'Hello world!')
  ...     fp.seek(0)
  ...     fp.read()
  b'Hello world!'
  >>>
  # file is now closed and removed

  # create a temporary directory using the context manager
  >>> with tempfile.TemporaryDirectory() as tmpdirname:
  ...     print('created temporary directory', tmpdirname)
  >>>
  # directory and contents have been removed

`glob <https://docs.python.org/3.4/library/glob.html>`_ - Unix style pathname pattern expansion
-----------------------------------------------------------------------------------------------

::

  >>> import glob
  >>> glob.glob('./[0-9].*')
  ['./1.gif', './2.txt']
  >>> glob.glob('*.gif')
  ['1.gif', 'card.gif']
  >>> glob.glob('?.gif')
  ['1.gif']

  >>> glob.glob('*.gif')
  ['card.gif']
  >>> glob.glob('.c*')
  ['.card.gif']


`shutil <https://docs.python.org/3.4/library/shutil.html>`_ - High-level file operations
----------------------------------------------------------------------------------------

- copyfileobj
- copyfile
- copymode
- copystat
- copy
- copy2: Identical to copy() except that copy2() also attempts to preserve all file metadata.
- copytree
- rmtree
- move
- disk_usage
- chown
- which
- make_archive
- unpack_archive
- get_terminal_size

::

  >>> shutil.disk_usage(os.path.expanduser('~'))
  usage(total=120473067520, used=51554127872, free=68656795648)

  >>> shutil.get_terminal_size()
  os.terminal_size(columns=130, lines=34)

  >>> shutil.which('python3')
  '/usr/local/bin/python3'

  >>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
  >>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
  >>> shutil.make_archive(archive_name, 'gztar', root_dir)
  '/Users/tarek/myarchive.tar.gz'

The resulting archive contains::

  $ tar -tzvf /Users/tarek/myarchive.tar.gz
  drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
  -rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
  -rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
  -rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
  -rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
  -rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
  -rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
  -rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts


`netrc <https://docs.python.org/3.4/library/netrc.html>`_ - netrc file processing
---------------------------------------------------------------------------------

::
  $ cat ~/.netrc
  default login huanghao password 123456
  machine company.com login hh password xxx

::

  >>> import netrc
  >>> import os
  >>> rc = netrc.netrc(os.path.expanduser('~/.netrc'))

  >>> rc.hosts
  {'default': ('huanghao', None, '123456'), 'company.com': ('hh', None, 'xxx')}

  >>> rc.authenticators('company.com')
  ('hh', None, 'xxx')

  >>> rc.authenticators('home.me')
  ('huanghao', None, '123456')

See also `Manual netrc <http://linux.about.com/library/cmd/blcmdl5_netrc.htm>`_


`hashlib <https://docs.python.org/3.4/library/hashlib.html>`_ - Secure hashes and message digests
-------------------------------------------------------------------------------------------------

::

  >>> import hashlib
  >>> m = hashlib.md5()
  >>> m.update(b"Nobody inspects")
  >>> m.update(b" the spammish repetition")
  >>> m.digest()
  b'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'
  >>> m.digest_size
  16
  >>> m.block_size
  64

  >>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
  'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'


`os <https://docs.python.org/3.4/library/os.html>`_ - Miscellaneous operating system interfaces
-----------------------------------------------------------------------------------------------

Environments

- name
- uname
- umask
- environ

Process parameters

- getpid: current process id
- getppid: parent's process id
- getpgrp: current process group id
- getpgid(pid): process group id with process id pid

- getuid: real user id of current process
- getgid: real group id of current process
- geteuid: effective user id of current process
- getegid: effective group id of current process
- getgroups: list of supplemental group ids associated with the current process

- getresuid: real, effective, saved
- getresgid:

- getsid: process session id

- getlogin: name of the user logged in

- set\*

File descriptor operations

- open
- close
- lseek
- read
- write
- sendfile
- dup
- dup2
- fchmod
- fchown
- fstat
- fsync
- ftruncate
- lockf
- isatty
- openpty
- pipe
- pipe2

Files and directories

- access
- chdir
- chflags
- chmod
- chown
- chroot
- getcwd
- link
- listdir
- mkdir
- makedirs
- mkfifo
- makedev
- major
- minor
- readlink
- remove
- removedirs
- rename
- rmdir
- stat
- symlink
- sync
- truncate
- unlink
- utime
- walk

Process management

- abort
- exec\*
- _exit
- forkpty
- kill
- nice
- popen
- spawn\*
- system
- times
- wait
- waitpid
- wait3
- wait4

Misc system information

- sep
- linesep
- pathsep
- devnull


`io <https://docs.python.org/3.4/library/io.html>`_ - Core tools for working with streams
-----------------------------------------------------------------------------------------

Text and Binary I/O

::

  f = io.StringIO("some initial text data")

  f = io.BytesIO(b"some initial binary data: \x00\x01")


`time <https://docs.python.org/3.4/library/time.html>`_ - Time access and conversions
-------------------------------------------------------------------------------------

::

  >>> import time
  >>> time.time()
  1413910801.16108
  >>> time.ctime()
  'Wed Oct 22 01:00:03 2014'

  >>> time.sleep(.1)

  >>> time.clock()
  0.194521


`argparse <https://docs.python.org/3.4/library/argparse.html>`_ - Parser for command-line options, arguments and sub-commands
-----------------------------------------------------------------------------------------------------------------------------

::

  parser = argparse.ArgumentParser()
  parser.add_argument('pattern')
  parser.add_argument('files', nargs='*')
  parser.add_argument('-n', '--line-numerber', action='store_true')
  ...
  namespace = parser.parse_args()

`logging <https://docs.python.org/3.4/library/logging.html>`_ - logging — Logging facility for Python
-----------------------------------------------------------------------------------------------------

The standard API learned from log4j.

::

  import logging

  logfile = 'log.out'

  logging.basicConfig(filename=logfile, level=logging.DEBUG)

  logging.debug("this message should go to the log file")

  logger = logging.getLogger(__name__)
  logger.info("this message too")

::

  $ cat log.out
  DEBUG:root:this message should go to the log file
  INFO:__main__:this message too


`platform <https://docs.python.org/3.4/library/platform.html>`_ - Access to underlying platform’s identifying data
------------------------------------------------------------------------------------------------------------------

::

  >>> import platform
  >>> platform.python_version_tuple()
  ('3', '4', '1')
  >>> platform.platform()
  'Darwin-13.2.0-x86_64-i386-64bit'
  >>> platform.uname()
  uname_result(system='Darwin', node='huanghao-mpa', release='13.2.0', version='Darwin Kernel Version 13.2.0: Thu Apr 17 23:03:13 PDT 2014; root:xnu-2422.100.13~1/RELEASE_X86_64', machine='x86_64', processor='i386')

`errno <https://docs.python.org/3.4/library/errno.html>`_ - Standard errno system symbols
-----------------------------------------------------------------------------------------

::

  >>> os.mkdir('/tmp')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  FileExistsError: [Errno 17] File exists: '/tmp'

  >>> errno.EEXIST
  17

  >>> try:
  ...   os.mkdir('/tmp')
  ... except OSError as err:
  ...   if err.errno == errno.EEXIST:
  ...      print('File exists')
  ...   else:
  ...      raise
  ...
  File exists
