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
