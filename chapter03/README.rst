Core Types
==========

+---------------+----------------------------------------------+
| Built-in type | Example                                      |
+===============+==============================================+
| None          | None                                         |
| Booleans      | True,False                                   |
| Numbers       | 123,3.14,3+4j,0xef,Decimal,Fraction          |
| Strings       | 'spam',"Bob's",b'a\x01c',u'sp\xc4m'          |
| Lists         | [1,[2,'Three'],4.5], list(range(10))         |
| Tuples        | (1,'spam',4,'U'),tuple('spam'),namedtuple    |
| Dicts         | {'food':'spam','taste':'yum'},dict(hours=10) |
| Sets          | {1,'a','bc'},set('abc')                      |
| Files         | open('eggs.txt')                             |
| functions     | def,lambda                                   |
| modules       | import,`__module__`                          |
| classes       | object,types,metaclasses                     |
+---------------+----------------------------------------------+

Numeric types
-------------

A complete inventory of Python's numeric toolbox includes:

- Integer and float-point
- Complex number
- Decimal: fixed-precision
- Fraction: rational number
- Sets: collections with numeric operations
- Booleans: true and false
- Built-in functions and modules: round, math, random, etc.
- Expressions; unlimited integer precision; bitwise operations;
  hex, otctal, and binary formats
- Third-party extensions: vectors, libraries, visulization, plotting, etc.

Literals

  1234, -24, 0, 9999999999999999
  1.23, 1., 3.14e-10, 4E210, 4.0e+210
  0o177, 0x9ff, 0b10101011, 0177
  3+4j, 3.0+4.0j, 3j
  set('spam'), {1, 2, 3, 4}
  Decimal('1.0'), Fraction(1, 3)
  bool(x), True, False

`Operations <Precedence_>`_

::

  +, -, *, /, //, >>, <<, **, &, |, ^, %, ~
  <, >, !=, ==, <=, >=, in, not in, not, and, or

`Built-in functions`_

  pow, abs, round, floor, int, hex, bin


::
  >>> 3 ** 2 / (4 + 1)
  1
  >>> 3 ^ 9
  10
  >> 3 | 9
  11
  >>> 1 << 3
  8
  >>> 0xf - 0b1000 + 010
  15


  >>> type(3)
  <type 'int'>
  >>> type(2**100)
  <type 'long'>
  >>> 2**100
  1267650600228229401496703205376L
  >>> type(3L)
  <type 'long'>
 
Changes in 3.0

- `PEP 0237`_: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.
- `PEP 0238`_: An expression like 1/2 returns a float. Use 1//2 to get the truncating behavior. (The latter syntax has existed for years, at least since Python 2.2.)
- The sys.maxint constant was removed, since there is no longer a limit to the value of integers. However, sys.maxsize can be used as an integer larger than any practical list or string index. It conforms to the implementation’s “natural” integer size and is typically the same as sys.maxint in previous releases on the same platform (assuming the same build options).
- The repr() of a long integer doesn’t include the trailing L anymore, so code that unconditionally strips that character will chop off the last digit instead. (Use str() instead.)
- Octal literals are no longer of the form 0720; use 0o720 instead.


.. _PEP 0237: http://legacy.python.org/dev/peps/pep-0237/
.. _PEP 0238: http://legacy.python.org/dev/peps/pep-0238/
.. _Operator precedence: https://docs.python.org/3.4/reference/expressions.html#operator-precedence
.. _Built-in functions: https://docs.python.org/3.4/library/functions.html#built-in-functions
