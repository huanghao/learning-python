Introduction
============

Q&A
---

What is Python ?
  A interpreted, interactive, OO programming language.

What is Python good for ?
  high-level, a large standard library, a wide variety of 3rd-party packages

Why is it called Python ?
  `Monty Python's Flying Circus <http://www.imdb.com/title/tt0063929/>`_

Why do people use Python ?

What can I do with Python ?

Which Python should I choose ?
- version: 2 or 3
- `Alternate Implementations`_: cpython, pypy, Jython, IronPython, stackless

Features
--------

- Open source
- Dynamic scripting language
- OO and functional
- Free
- Portable
- Powerful
- Easy to learn and to use

Design and History
------------------

- `History <https://docs.python.org/3/license.html>`_
- indentation
- explicit *self*
- no *case* statement
- *lambda* only allows expressions
- The Zen of Python(`PEP 20 <http://legacy.python.org/dev/peps/pep-0020/>`_)
- `Guido <http://en.wikipedia.org/wiki/Guido_van_Rossum>`_

Run programs
------------

Try interpreter

::

  >>> 1 + 1
  2
  >>> ^D or exit() or quit()

$ python hello.py

.pyc

- compiled .py
- After 3.2: *__pycache__*

Python's Arsenal
----------------

numeric, bool, sequence, dict, text, set, binary sequence, exception, object

~250 `libs <https://docs.python.org/3/library/index.html>`_:

1. Text processing: string, re, difflib, textwrap, unicodedata, stringprep, readline, rlcompleter
2. Binary data services: struct, codecs
3. Dat types: datetime, calendar, collections, collections.abc, heapq, bisect, array, weakref, types, copy, pprint, reprlib, enum
4. Numeric and Math: numbers, math, cmath, decimal, fractions, random, statistics
5. Functional programming: itertools, functools, perator
6. File and directory access: pathlib, os.path, fileinput, stat, filecmp, tempfile, glob, fnmatch, linecache, shutil, macpath
7. Data peristence: pickle, copyreg, shelve, marshal, dbm, sqlite3
8. Data compression: zlib, gzip, bz2, lzma, zipfile, tarfile
9. File formats: csv, configparser, netrc, xdrlib, plistlib
10. Cryptographic: hashlib, hmac
11. OS: os, io, time, argparse, getopt, logging, getpass, curses, platform, errno, ctypes
12. Concurrent: threading, multiprocessing, concurrent.futures, subprocess, sched, queue, dummy_threading
13. Networking: socket, ssl, select, selectors, asyncio, asyncore, asynchat, signal, mmap
14. Internet: email, json, mailcap, mailbox, mimetypes, base64, binhex, binascii, quopri, uu
15. Structured markup: html, xml.etree, xml.dom, xml.sax
16. Internet protocols: webbrowser, cgi, wsgiref, urllib.request, urllib.response, urllib.parse, urllib.error, urllib.robotparser, http, fptlib, poplib, imaplib, nntplib, smtplib, smtpd, telnetlib, uuid, socketserver, http.server, http.cookies, http.cookiejar, xmlrpc, ipaddress
17. Multimedia: audioop, aifc, sunau, wave, chunk, colorsys, imghdr, sndhdr, ossaudiodev
18. I18n: gettext, locale
19. Porgram frameworks: turtle, cmd, shlex
20. GUI: tkinter
21. Development tools: pydoc, doctest, unittest, unittest.mock, test
22. Debugging and profiling: bdb, faulthandler, pdb, profile, timeit, trace, tracemalloc
23. Packaing and distribution: distutils, ensurepip, venv
24. Runtime: sys, sysconfig, builtins, __main__, warnings, contextlib, abc, atexit, traceback, __future__, gc, inspect, site, fpectl
25. Custom python interpreters: code, codeop
26. Importing: zipimport, pkgutil, modulefinder, runpy, importlib
27. Language: parser, ast, symtable, symbol, token, keyword, tokenize, tabnanny, pyclbr, py_compile, compileall, dis, pickletools
28. Misc: formatter
29. MS: msilib, msvcrt, winreg, winsound
30. Unix: posix, pwd, spwd, grp, crypt, termios, tty, pty, fcntl, pipes, resource, nis, syslog
31. Superseded: optparse, imp

Where you can find those standard libs ?

  sys.path

  /usr/lib/python2.7
  /usr/lib/python3.4

.. _Alternate Implementations: https://docs.python.org/3/reference/introduction.html#alternate-implementations
