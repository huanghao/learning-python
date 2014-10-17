Syntax
======

Python program structure

1. *Programs* are composed of modules.
2. *Modules* contain statements.
3. *Statements* contain expressions.
4. *Expressions* create and process objects.

Lexical analysis
----------------

Line structure
  A Python program is divided into a number of logical lines.

Logical lines
  The end of a logical line is represented by the token NEWLINE.

Physical lines
  A physical line is a sequence of characters terminated by an end-of-line sequence(CR/LF).

Comments
  A comment starts with a hash character (#) that is not part of a string literal, and ends
  at the end of the physical line.

Encoding declarations
  If a comment in the first or second line of the Python script matches the regular
  expression **coding[=:]\s*([-\w.]+)**.

The recommended forms of this expression are::

  # -*- coding: <encoding-name> -*-
  which is recognized also by GNU Emacs, and

  # vim:fileencoding=<encoding-name>
  which is recognized by Bram Moolenaar’s VIM.

If no encoding declaration is found, the default encoding is UTF-8.

Explicit line joining
  Two or more physical lines may be joined into logical lines using backslash characters

::

  if 1900 < year < 2100 and 1 <= month <= 12 \
    and 1 <= day <= 31 and 0 <= hour < 24 \
    and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
      return 1

Implicit line joining
  Expressions in parentheses, square brackets or curly braces can be split over more
  than one physical line without using backslashes.

::

  month_names = ['Januari', 'Februari', 'Maart',      # These are the
                 'April',   'Mei',      'Juni',       # Dutch names
                 'Juli',    'Augustus', 'September',  # for the months
                 'Oktober', 'November', 'December']   # of the year

Blank lines
  A logical line that contains only spaces, tabs, formfeeds and possibly a comment,
  is ignored.

Indentation
  Leading whitespace (spaces and tabs) at the beginning of a logical line is used
  to compute the indentation level of the line, which in turn is used to determine
  the grouping of statements.

Identifiers

Keywords

::

  False      class      finally    is         return
  None       continue   for        lambda     try
  True       def        from       nonlocal   while
  and        del        global     not        with
  as         elif       if         or         yield
  assert     else       import     pass
  break      except     in         raise

Reserved classes of identifiers
  Certain classes of identifiers (besides keywords) have special meanings.

:_*:
  Not imported by from module import \*.

  The special identifier _ is used in the interactive interpreter to store the
  result of the last evaluation; it is stored in the builtins module.

  When not in interactive mode, _ has no special meaning and is not defined.

:__*__:
  System-defined names. See `Special method names`_.

:__*:
  Class-private names.

Literals
  `string <string_and_bytes_literal>`_,
  `bytes <string_and_bytes_literal_>`_,
  numeric(`interger <integer_literal_>`_,
  `float <float_literal_>`_,
  `imaginary <imaginary_literal_>`_)

Operators::

  +       -       *       **      /       //      %
  <<      >>      &       |       ^       ~
  <       >       <=      >=      ==      !=

Delimiters::

  (       )       [       ]       {       }
  ,       :       .       ;       @       =       ->
  +=      -=      *=      /=      //=     %=
  &=      |=      ^=      >>=     <<=     **=

Expressions
-----------

Identifiers(names), Literals, lists, dicts, sets, Attributes, subscriptions,
slices, calls, arithmetic and bitwise operations, shifting operations, comparisions,
boolean operations, Expression lists

Condition expressions::

  x if C else y

Lambda expressions::

  lambda (x, y): x + y
  =>
  def <lambda>(x, y):
    return x + y

Generator expressions::

  (x*y for x in range(10) for y in bar(x))

Yield expressions::

  def foo(n):
    for i in range(n):
      yield i

Assignment
----------

::

  i = 1
  i += 2

  a, b = 2, 3.14
  a, b = b, a     # swap

  first, second, _ = (1, 2, 3)          # pattern match
  a, (b, c), d = [1, [2, 3], 4]
  first, second, *others = range(10)    # py3.

============================ =======================================================
Operation   Interpretation
============================ =======================================================
spam = 'Spam'                Basic form
spam, ham = 'yum', 'YUM'     Tuple assignment (positional)
[spam, ham] = ['yum', 'YUM'] List assignment (positional)
a, b, c, d = 'spam'          Sequence assignment, generalized
a, \*b = 'spam'              Extended sequence unpacking (Python 3.X)
spam = ham = 'lunch'         Multiple-target assignment
spams += 42                  Augmented assignment (equivalent to spams = spams + 42)
============================ =======================================================

`PEP 3132 <https://www.python.org/dev/peps/pep-3132>`_ - Extended Iterable Unpacking. The specification for the \*target feature.

Pass
----

when it is excuted, nothing happens. It's useful as a placeholder

If
--

::

  if x > 0
    print 'Positive'
  elif x < 0:
    print 'Nagtive'
  else:
    print 'Zero'

Loop
---------------------------------

for, while, break, continue

::

  x = 7
  while x > 0:
    print x * 2
    x -= 1
  else:
    print 'End'

  for i in range(10):
    print i
    i = 5

Notes: *break* terminates the nearest enclosing loop, skipping the optional *else* clause if the loop has one.

Try/Raise
---------

::

  def foo():
    if random.random() < .1:
      raise SomeException("BOOM!")

  try:
    foo()
  except SomeException as err1:
    print err1
  except AnotherException as err2:
    raise
  except (AException, BException) as err3:
    pass
  else:
    print 'No exception occurs'
  finally:
    print "This block is always evaluated"

With
----

::

  # this file will be closed automatically
  # even exception is raised within this block

  with open('somefile', 'w') as writer:
    write_content_to(writer)

Context Manager
  __enter__()
  __exit__()

::

  # py3.1, 2.7
  with A() as a, B() as b:
    do some thing
  =>
  # py2.6
  with A() as a:
    with B() as b:
      do some thing

Yield
-----

::

  def start_from(n):
    while True:
      yield n
      n += 1

Return
------

::

  def foo(n):
    return 'Even' if n % 2 == 0 else 'Odd'

  # If no explicit return value is given,
  # return value is None

  def foo(n):
    pass

Import
------

::

  import sys
  import os.path

  from random import *
  from os.path import (join, exist)
  from math import pi

  import numpy as np
  from pyquery import PyQuery as pq

Future #TODO
------------

`PEP 236 <http://legacy.python.org/dev/peps/pep-0236/>`_ - Back to the __future__


Global, local and nonlocal
--------------------------

::

  a = 1

  def foo():
    global a
    a = 2

  def bar():
    a = 2   # local

  print(a)  # => 1
  bar()
  print(a)  # => 1
  foo()
  print(a)  # => 2

built-in functions: locals(), globals()

::

  def create_account(initial):
    balance = initial

    def query():
      return balance

    def dec(n):
      nonlocal balance
      if balance < n:
        raise ValueError('Not enough money')
      balance -= n
      
    return {
      'query': query,
      'dec': dec,
      }

  a1 = make_account(100)
  a2 = make_account(100)
  a1['dec'](50)
  print(a1['query'])    # => 50
  print(a2['query'])    # => 100

`PEP 3104 <http://legacy.python.org/dev/peps/pep-3104/>`_ - Access to Names in Outer Scopes. The specification for the nonlocal statement.

Assert
------

::

  def factorial(n):
    assert n >= 0 and isinstance(n, numbers.Integral), \
      "Factorial of negative and non-integral is undefined"

  assert expression1 [, expression2]
  =>
  if __debug__:
    if not expression1:
      raise AssertError(expression2):

In the current implementation, the built-in variable __debug__ is True
under normal circumstances, False when optimization is requested (command
line option -O). Assignments to __debug__ are illegal.

Del
---

::

  >>> a = 1
  >>> del a
  >>> a
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'a' is not defined

  >>> class Foo:
  ...   def __init__(self, a):
  ...     self.a = a
  ...
  >>> foo = Foo(3)
  >>> foo.a
  3
  >>> del foo.a
  >>> foo.a
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: Foo instance has no attribute 'a'

`Print <https://docs.python.org/2/reference/simple_stmts.html#the-print-statement>`_
------------------------------------------------------------------------------------

`Print is a Function <https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function>`_

`PEP 3105 <http://legacy.python.org/dev/peps/pep-3105/>`_ -- Make print a function

`Exec <https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement>`_
----------------------------------------------------------------------------------

`Removed keyword <https://docs.python.org/3/whatsnew/3.0.html#removed-syntax>`_:
  exec() is no longer a keyword; it remains as a function.  (Fortunately the function
  syntax was also accepted in 2.x.) Also note that exec() no longer takes a stream
  argument; instead of exec(f) you can use exec(f.read()).

Iterations and Comprehensions
-----------------------------


.. _The Python Language Reference: https://docs.python.org/3/reference/index.html
.. _Special method names: https://docs.python.org/3/reference/datamodel.html#specialnames
.. _string_and_bytes_literal: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
.. _integer_literal: https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
.. _float_literal: https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals
.. _imaginary_literal: https://docs.python.org/3/reference/lexical_analysis.html#imaginary-literals
