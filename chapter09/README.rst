A tour of std libs
==================

:Text processing:
  string, re, difflib, textwrap, unicodedata, stringprep, readline, rlcompleter

:Binary data services:
  struct, codecs

:Dat types:
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
  **platform**, **errno**, **ctypes**

:Concurrent:
  threading, multiprocessing, concurrent.futures, subprocess, sched, queue, dummy_threading

:Networking:
  socket, ssl, select, selectors, asyncio, asyncore, asynchat, signal, mmap

:Internet:
  email, json, mailcap, mailbox, mimetypes, base64, binhex, binascii, quopri, uu

:Structured markup:
  html, xml.etree, xml.dom, xml.sax

:Internet protocols:
  webbrowser, cgi, wsgiref, urllib.request, urllib.response, urllib.parse, urllib.error, urllib.robotparser, http, fptlib, poplib, imaplib, nntplib, smtplib, smtpd, telnetlib, uuid, socketserver, http.server, http.cookies, http.cookiejar, xmlrpc, **ipaddress**

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

Deque: double-ended queue
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


`heapq <https://docs.python.org/3.4/library/heapq.html>` - Heap queue algorithm

This module provides an implementation of the min heap queue algorithm, also known as the priority queue algorithm.

