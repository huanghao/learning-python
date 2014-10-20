Introduction
============

Q&A
---

What's the frist programming language you learned ?

How many programming languages you are using for daily work ?

What's your favorite programming language ?

What is Python ?
  A interpreted, interactive, OO programming language.

Why do people use Python ?

Why is it called Python ?
  `Monty Python's Flying Circus <http://www.imdb.com/title/tt0063929/>`_

What is Python good for ?
  high-level, a large standard library, a wide variety of 3rd-party packages

What can I do with Python ?

Which Python should I choose ?
- Version: 2.7 or 3.4
- `Alternate Implementations`_: cpython, pypy, Jython, IronPython, stackless

Notes: this tutorial restrict on 2.7 and latest 3.x of cpython

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

  >>> dir()

  >>> l = [1, 2, 3]
  >>> dir(l)

  >>> help(l)
  >>> help(l.extend)

$ python hello.py

.pyc

- compiled .py
- After 3.2: *__pycache__*

Built-in document

  $ pydoc with

  $ pydoc -p 8080       # then open http://localhost:8080


Python's Arsenal
----------------

numeric, bool, sequence, dict, text, set, binary sequence, exception, object

~250 `libs <https://docs.python.org/3/library/index.html>`_:

.. _Alternate Implementations: https://docs.python.org/3/reference/introduction.html#alternate-implementations

