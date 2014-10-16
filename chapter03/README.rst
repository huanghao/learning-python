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
  Decimal('1.0'), Decimal('-Inf'), Fraction(1, 3)
  bool(x), True, False

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
  >>> (2 + 1j) * -1j
  (1-2j)

  >>> type(3)
  <type 'int'>
  >>> type(2**100)
  <type 'long'>
  >>> 2**100
  1267650600228229401496703205376L
  >>> type(3L)
  <type 'long'>

  >>> math.factorial(3) + math.log(math.e) + math.sqrt(9) + math.sin(math.pi/2) + math.ceil(0.1)  # 6+1+3+1+1
  12.0
  >>> math.sqrt(-1)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: math domain error
  >>> cmath.sqrt(-1)
  1j

  >>> from random import *
  >>> random()
  0.06091254441752425
  >>> sample(range(10), 3)
  [0, 1, 4]
  >>> choice(range(10))
  5
  >>> l = list(range(10))
  >>> shuffle(l)
  >>> l
  [5, 7, 0, 1, 2, 3, 9, 6, 4, 8]
  >>> gauss(0, 1)
  -0.8042047260239109

  >>> from decimal import *
  >>> .1 * 3 - .3
  5.551115123125783e-17
  >>> Decimal('.1') * Decimal('3') - Decimal('.3')
  Decimal('0.0')
  >>> 1.20 * 1.30
  1.56
  >>> Decimal('1.20') * Decimal('1.30')
  Decimal('1.5600')
  >>> getcontext().prec = 6
  >>> Decimal(1) / Decimal(7)
  Decimal('0.142857')
  >>> getcontext().prec = 28
  >>> Decimal(1) / Decimal(7)
  Decimal('0.1428571428571428571428571429')

  >>> from fractions import Fraction
  >>> (6/5) * (7/3) - 2.8
  4.440892098500626e-16
  >>> Fraction(6, 5) * Fraction(7, 3) - Fraction('2.8')
  Fraction(0, 1)
  >>> gcd(15, 6)
  >>> 3

  >>> from numbers import Number, Complex, Real, Rational, Integral
  >>> issubclass(Integral, Complex)
  True
  >>> isinstance(1, Complex)
  True

  >>> from statistics import *
  >>> mean([1, 2, 3, 4, 4])
  >>> 2.8
  >>> median([1, 3, 5])
  >>> 3
  >>> mod([1, 1, 2, 3, 3, 3, 3, 4])
  >>> 3
  >>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
  1.0810874155219827
  >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
  >>> variance(data)
  1.3720238095238095

`Operations <Precedence_>`_

::

  +, -, *, /, //, >>, <<, **, &, |, ^, %, ~
  <, >, !=, ==, <=, >=, in, not in, not, and, or

`Built-in functions`_

  abs, bin, bool, divmod, float, hex, int, oct, pow, round

Built-in modules

  numbers, math, cmath, decimal, fractions, random, statistics

 
New in 2.6
- `PEP 3141`_: A Type Hierarchy for Numbers

New in 3.0

- `PEP 0237`_: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.
- `PEP 0238`_: An expression like 1/2 returns a float. Use 1//2 to get the truncating behavior. (The latter syntax has existed for years, at least since Python 2.2.)
- The sys.maxint constant was removed, since there is no longer a limit to the value of integers. However, sys.maxsize can be used as an integer larger than any practical list or string index. It conforms to the implementation’s “natural” integer size and is typically the same as sys.maxint in previous releases on the same platform (assuming the same build options).
- The repr() of a long integer doesn’t include the trailing L anymore, so code that unconditionally strips that character will chop off the last digit instead. (Use str() instead.)
- Octal literals are no longer of the form 0720; use 0o720 instead.
PEP 3141 -- A Type Hierarchy for Numbers
- `Ordering Comparisions`_: The ordering comparison operators (<, <=, >=, >) raise a TypeError exception when the operands don’t have a meaningful natural ordering. Thus, expressions like 1 < '', 0 > None or len <= len are no longer valid, and e.g. None < None raises TypeError instead of returning False. A corollary is that sorting a heterogeneous list no longer makes sense – all the elements must be comparable to each other. Note that this does not apply to the == and != operators: objects of different incomparable types always compare unequal to each other.


.. _PEP 0237: http://legacy.python.org/dev/peps/pep-0237/
.. _PEP 0238: http://legacy.python.org/dev/peps/pep-0238/
.. _PEP 3141: http://legacy.python.org/dev/peps/pep-3141/
.. _Operator precedence: https://docs.python.org/3.4/reference/expressions.html#operator-precedence
.. _Built-in functions: https://docs.python.org/3.4/library/functions.html#built-in-functions
.. _Ordering Comparisions: https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons

