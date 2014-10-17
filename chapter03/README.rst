Core Types
==========

=============  ============================================
Built-in type  Example
=============  ============================================
None           None
Booleans       True,False
Numbers        123,3.14,3+4j,0xef,Decimal,Fraction
Strings        'spam',"Bob's",b'a\x01c',u'sp\xc4m'
Lists          [1,[2,'Three'],4.5], list(range(10))
Tuples         (1,'spam',4,'U'),tuple('spam'),namedtuple
Dicts          {'food':'spam','taste':'yum'},dict(hours=10)
Sets           {1,'a','bc'},set('abc')
Files          open('eggs.txt')
functions      def,lambda
modules        import,`__module__`
classes        object,types,metaclasses
=============  ============================================

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

Literals::

  1234, -24, 0, 9999999999999999
  1.23, 1., 3.14e-10, 4E210, 4.0e+210
  0o177, 0x9ff, 0b10101011, 0177
  3+4j, 3.0+4.0j, 3j
  set('spam'), {1, 2, 3, 4}
  Decimal('1.0'), Decimal('-Inf'), Fraction(1, 3)
  bool(x), True, False

Example::

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
  >>> ({1, 2, 3} & { 3, 5, 7} | {3, 4}) - {Decimal('3')}
  set([4])
  >>> Decimal('3') == 3
  True

  >>> True = False    # 2.x
  >>> True == False
  True

`Operator precedence`_

::

  +, -, *, /, //, >>, <<, **, &, |, ^, %, ~
  <, >, !=, ==, <=, >=, in, not in, not, and, or


`Built-in functions`_

  abs, bin, bool, divmod, float, hex, int, oct, pow, round

::
 
  >>> bool(3) and True or False
  True
  >>> ' '.join([bin(13),  hex(13), oct(13)])
  '0b1101 0xd 015'
  >>> divmod(7, 3)
  (2, 1)
  >>> abs(-3)
  3
  >>> pow(2, 8) == 2 ** 8
  True
  >>> round(3.14)
  3.0
  >>> int('3') + float('.5')
  5.5
  >>> int('10', base=16) - int('10') - int('10', base=8) - int('10', base=2)
  -4

Built-in modules

  numbers, math, cmath, decimal, fractions, random, statistics

::

  >>> type(3)        # 2.x
  <type 'int'>
  >>> type(2**100)
  <type 'long'>
  >>> 2**100
  1267650600228229401496703205376L
  >>> type(3L)
  <type 'long'>

  >>> from numbers import Number, Complex, Real, Rational, Integral
  >>> issubclass(Integral, Complex)
  True
  >>> isinstance(1, Complex)
  True

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

New in 2.6

- `PEP 3141`_: A Type Hierarchy for Numbers

New in 3.0

- `PEP 0237`_: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.
- `PEP 0238`_: An expression like 1/2 returns a float. Use 1//2 to get the truncating behavior. (The latter syntax has existed for years, at least since Python 2.2.)
- The sys.maxint constant was removed, since there is no longer a limit to the value of integers. However, sys.maxsize can be used as an integer larger than any practical list or string index. It conforms to the implementation’s “natural” integer size and is typically the same as sys.maxint in previous releases on the same platform (assuming the same build options).
- The repr() of a long integer doesn’t include the trailing L anymore, so code that unconditionally strips that character will chop off the last digit instead. (Use str() instead.)
- Octal literals are no longer of the form 0720; use 0o720 instead.
- `PEP 3141`_ -- A Type Hierarchy for Numbers
- `Ordering Comparisions`_: The ordering comparison operators (<, <=, >=, >) raise a TypeError exception when the operands don’t have a meaningful natural ordering. Thus, expressions like 1 < '', 0 > None or len <= len are no longer valid, and e.g. None < None raises TypeError instead of returning False. A corollary is that sorting a heterogeneous list no longer makes sense – all the elements must be comparable to each other. Note that this does not apply to the == and != operators: objects of different incomparable types always compare unequal to each other.
- `Changed Syntax`_: True, False, and None are reserved words. (2.6 partially enforced the restrictions on None already.)


Strings
-------

Literals

- Single quotes: 'spa"m'
- Double quotes: "spa'm"
- Triple quotes: '''... spam ...''', """... spam ...""""
- Escape sequences: "s\tp\na\0m"
- Raw strings: r"C:\new\test.spm"
- Bytes literals in 3.x and 2.6+: b'sp\x01am'
- Unicode literals in 2.x and 3.3+: u'eggs\u0020spam'

Single- and double-quoted strings are the same

Implicit concatenation::

  >>> title = "Meaning " 'of' " Life"
  >>> title
  'Meaning of Life'

Escape characters

============== ==============================================
Escape         Meaning
============== ==============================================
``\newline``   Ignored(continuation line)
``\\``         Backslash (stores one ``\``)
``\'``         Single quote(stores ')
``\"``         Double quote(stores ")
``\a``         Bell
``\b``         Backspace
``\f``         Formfeed
``\n``         Newline(linefeed)
``\r``         Carriage return
``\t``         Horizontal tab
``\v``         Vertical tab
``\xhh``       Character with hex value hh(exactly 2 digits)
``\ooo``       Character with octal value ooo(up to 3 digits)
``\0``         Null: binary 0 character(doesn't end string)
``\N{id}``     Unicode database ID
``\uhhhh``     Unicode character with 16bit hex value
``\Uhhhhhhhh`` Unicode character with 32bit hex value
``\other``     Not an escape(keeps both ``\`` and other)
============== ==============================================

Raw strings suppress escapes::

  >>> path = r'C:\new\text.dat'
  >>> path              # Show as Python code
  'C:\\new\\text.dat'
  >>> print(path)       # User-friendly format
  C:\new\text.dat
  >>> len(path)         # String length
  15

Triple quotes code multiline block strings::

  >>> mantra = """Always look
  ...   on the bright
  ... side of life."""
  >>>
  >>> mantra
  'Always look\n on the bright\nside of life.'
  >>> print(mantra)
  Always look
    on the bright
  side of life.

Basic operations::

  >>> len('abc')
  3
  >>> 'abc' + 'def'
  'abcdef'
  >>> 'Ni!' * 4
  'Ni!Ni!Ni!Ni!'

  >>> myjob = "hacker"
  >>> for c in myjob: print(c, end=' ')
  ...
  h a c k e r
  >>> "k" in myjob
  True
  >>> "z" in myjob
  False
  >>> 'spam' in 'abcspamdef'
  True

Indexing and slicing::

  >>> S = 'spam'
  >>> S[0], S[−2]
  ('s', 'a')
  >>> S[1:3], S[1:], S[:−1]
  ('pa', 'pam', 'spa')

  >>> S = 'abcdefghijklmnop'
  >>> S[1:10:2]
  'bdfhj'
  >>> S[::2]
  'acegikmo'
  >>> S = 'hello'
  >>> S[::−1]            # Reversing items
  'olleh'
  >>> S = 'abcedfg'
  >>> S[5:1:−1]
  'fdec'

  >>> 'spam'[1:3]
  'pa'
  >>> 'spam'[slice(1, 3)]
  'pa'
  >>> 'spam'[::-1]
  'maps'
  >>> 'spam'[slice(None, None, −1)]
  'maps'

String conversion::

  >>> int("42"), str(42)
  (42, '42')
  >>> repr(42)
  '42'
  >>> str('spam'), repr('spam')
  ('spam', "'spam'")

  >>> str(3.1415), float("1.5")
  ('3.1415', 1.5)
  >>> text = "1.234E-10"
  >>> float(text)
  1.234e-10

  >>> ord('s')
  115
  >>> chr(115)
  's'

**Changing** string::

  >>> S = 'spam'      # Immutable objects
  >>> S[0] = 'x'      # Raises an error!
  TypeError: 'str' object does not support item assignment

  >>> S = S + 'SPAM!'  # To change a string, make a new one
  >>> S
  'spamSPAM!'
  >>> S = S[:4] + 'Burger' + S[−1]
  >>> S
  'spamBurger!'

  >>> S = 'splot'
  >>> id(S)
  18598192
  >>> S = S.replace('pl', 'pamal')
  >>> id(S)
  18598096
  >>> S
  'spamalot'
  >>> id('spam')
  18597136
  >>> id('spamalot')
  18597760

  >>> 'That is %d %s bird!' % (1, 'dead')
  That is 1 dead bird!
  >>> 'That is {0} {1} bird!'.format(1, 'dead')
  'That is 1 dead bird!'

*str*, the *bytes* type is immutable. There is a separate mutable type to hold buffered binary data, *bytearray*.

`String methods`_ in 3.4

- str.capitalize
- str.casefold
- str.center
- str.count
- **str.encode(encoding="utf-8",-errors="strict")**
- **str.endswith(suffix[,-start[,-end]])**

::

  >>> [name for name in os.listdir('/etc/') if name.endswith('.conf')][:5]
  ['asl.conf', 'autofs.conf', 'dnsextd.conf', 'ftpd.conf', 'ip6addrctl.conf']

- str.expendtabs
- **str.find(sub[,-start[,-end]])**

::

  >>> 'abcd'.find('a')
  0
  >>> 'abcd'.find('1')
  -1
  >>> 'abcd'.find('d', 2)
  3
  >>> 'abcd'.find('d')
  3

- **str.format(*args, **kwargs)**
- str.format_map
- **str.index(sub[, start[, end]])**

::

  >>> 'abcd'.find('e')
  -1
  >>> 'abcd'.index('e')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: substring not found

- str.isalnum
- **str.isalpha()**

::

  >>> 'abd'.isalpha()
  True
  >>> 'abd1'.isalpha()
  False
  >>> '1234'.isdigit()
  True
  >>> '123a'.isdigit()
  False
  >>> '12ab'.isalnum()
  True
  >>> '\n\t '.isspace()
  True

- str.isdecimal
- str.isdigit
- str.isidentifier
- str.islower
- str.isnumeric
- str.isprintable
- str.isspace
- str.istitle
- str.isupper
- **str.join(iterable)**

::

  >>> ','.join(['ab', 'c', 'd'])
  'ab,c,d'
  >>> ','.join('abcd')
  'a,b,c,d'

- str.ljust
- **str.lower()**

::

  >>> 'PyTHon'.lower()
  'python'
  >>> 'PyTHon'.upper()
  'PYTHON'

- str.lstrip
- str.maketrans
- str.partition
- **str.replace(old, new[, count])**

::

  >>> 'PyTHon'.replace('TH', 'C')
  'PyCon'

- str.rfind
- str.rindex
- str.rjust
- str.rpartition
- str.rsplit
- str.rstrip
- **str.split(sep=None, maxsplit=-1)**

::

  >>> 'a b  \t\t c\nd'.split()
  ['a', 'b', 'c', 'd']
  >>> 'a,b,c,d'.split(',')
  ['a', 'b', 'c', 'd']
  >>> 'a b  \t\t c\nd'.split(None, 2)
  ['a', 'b', 'c\nd']

- **str.splitlines([keepends])**
- **str.startswith(prefix[, start[, end]])**
- **str.strip([chars])**

::

  >>> '   line\n'.strip()
  'line'
  >>> '   line\n'.lstrip()
  'line\n'
  >>> '   line\n'.rstrip()
  '   line'

- str.swapcase
- str.title
- str.translate
- **str.upper()**
- str.zfill

`printf-style String Formatting`_

  %s, %d, %f, %g, %x

`Text vs. data instead of unicode vs. 8-bit`_

In 2.x::

  >>> type('hello'), repr('hello')
  (<type 'str'>, "'hello'")
  >>> type(u'你好'), repr(u'你好')
  (<type 'unicode'>, "u'\\u4f60\\u597d'")
  >>> type('你好'), type(u'hello')
  (<type 'str'>, <type 'unicode'>)

  >>> issubclass(str, basestring)
  True
  >>> issubclass(unicode, basestring)
  True

  >>> u'hello' + ' world'
  u'hello world'

- *str* is 8-bit, it represents ascii string and binary data.
- *unicode* represents text.
- unicode.encode => str
- str.decode => unicode
- Keep text in unicode inside your system. Encode and decode at the bournday(incoming/outgoing) of your system. 
- open().read() returns *str*

In 3.x::

  >>> type('hello'), type(u'hello'), type(b'hello')
  (<class 'str'>, <class 'str'>, <class 'bytes'>)

  >>> type('你好'), type(u'你好')
  (<class 'str'>, <class 'str'>)
  >>> type(b'你好')
    File "<stdin>", line 1
  SyntaxError: bytes can only contain ASCII literal characters.
  >>> type('你好'.encode()), repr('你好'.encode())
  (<class 'bytes'>, "b'\\xe4\\xbd\\xa0\\xe5\\xa5\\xbd'")

  >>> 'hello' + b' world'
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: Can't convert 'bytes' object to str implicitly

  >>> type(open('name.txt').read())
  <class 'str'>
  >>> type(open('name.txt', 'br').read())
  <class 'bytes'>
  >>> type(os.listdir()[0])
  <class 'str'>
  >>> type(sys.argv[0])
  <class 'str'>

- All text are unicode. The type used to hold text is *str*.
- Encoded unicode is represented as binary data. The type used to hold binary data is *bytes*.
- Mixing text and binary data raises TypeError.
- *basestring* was removed. *str* and *bytes* don't share a base class.
- open().read() returns *str*; open(, 'b').read() returns *bytes*.
- sys.stdin, sys.stdout and sys.stderr are unicode-only text files.
- Filenames are passed to and returned from APIs as (Unicode) strings.

See `Unicode HOWTO`_

Lists
-----

- Ordered collections of arbitrary objects
- Accessed by offset
- Variable-length, heterogeneous, and arbitrarily nestable
- Of the category “mutable sequence”
- Arrays of object references

================================= ========================================================
Operation                         Interpretation
================================= ========================================================
L = []                            An empty list
L = [123, 'abc', 1.23, {}]        Four items: indexes 0..3
L = ['Bob', 40.0, ['dev', 'mgr']] Nested sublists
L = list('spam')                  List of an iterable’s items, list of successive integers
L = list(range(-4, 4))
L[i]                              Index, index of index, slice, length
L[i][j]
L[i:j]
len(L)
L1 + L2                           Concatenate, repeat
L* 3
for x in L: print(x)              Iteration, membership
3 in L
L.append(4)                       Methods: growing
L.extend([5,6,7])
L.insert(i, X)
L.index(X)                        Methods: searching
L.count(X)
L.sort()                          Methods: sorting, reversing,
L.reverse()
L.copy()                          copying (3.3+), clearing (3.3+)
L.clear()
L.pop(i)                          Methods, statements: shrinking
L.remove(X)
del L[i]
del L[i:j]
L[i:j] = []                       Index assignment, slice assignment
L[i] = 3
L[i:j] = [4,5,6]
L = [x**2 for x in range(5)]      List comprehensions and maps
list(map(ord, 'spam'))
================================= ========================================================

Built-in functions range() and xrange()::

  >>> range(5)          # 2.x
  [0, 1, 2, 3, 4]
  >>> xrange(5)
  xrange(5)
  >>> type(range(5)), type(xrange(5))
  (<type 'list'>, <type 'xrange'>)

  >>> range(5)          # 3.x
  range(0, 5)
  >>> type(range(5))
  <class 'range'>

Change in 3.0: range() now behaves like xrange() used to behave, except it works with
  values of arbitrary size. The latter no longer exists.


Dictionaries
------------

- Accessed by key, not offset position
- Unordered collections of arbitrary objects
- Variable-length, heterogeneous, and arbitrarily nestable
- Of the category “mutable mapping”
- Tables of object references (hash tables)

========================================= ============================================================
Operation                                 Interpretation
========================================= ============================================================
 D = {}                                   Empty dict
 D = {'name': 'Bob', 'age': 40}           Two items
 E = {'cto': {'name': 'Bob', 'age': 40}}  Nesting
 D = dict(name='Bob', age=40)             Alternative construction techniques:
 D = dict([('name', 'Bob'), ('age', 40)]) keywords, key/value pairs, zipped key/value pairs, key lists
 D = dict(zip(keyslist, valueslist))
 D = dict.fromkeys(['name', 'age'])
 D['name']                                Indexing by key
 E['cto']['age']
 'age' in D                               Membership: key present test
 D.keys()                                 Methods: all keys,
 D.values()                               all values,
 D.items()                                all key+value tuples,
 D.copy()                                 copy (top-level),
 D.clear()                                clear (remove all items),
 D.update(D2)                             merge by keys,
 D.get(key, default?)                     fetch by key, if absent default (or None),
 D.pop(key, default?)                     remove by key, if absent default (or error)
 D.setdefault(key, default?)              fetch by key, if absent set default (or None),
 D.popitem()                              remove/return any (key, value) pair; etc.
 len(D)                                   Length: number of stored entries
 D[key] = 42                              Adding/changing keys
 del D[key]                               Deleting entries by key
list(D.keys())                            Dictionary views (Python 3.X)
 D1.keys() & D2.keys()
 D.viewkeys(), D.viewvalues()             Dictionary views (Python 2.7)
 D = {x: x*2 for x in range(10)}          Dictionary comprehensions (Python 3.X, 2.7)
========================================= ============================================================

Built-in function zip()::

  >>> zip(range(5), 'abc')
  [(0, 'a'), (1, 'b'), (2, 'c')]

Change in 3.0:
  zip() now returns an iterator.

Tuples
------

- Ordered collections of arbitrary objects
- Accessed by offset
- Of the category “immutable sequence”
- Fixed-length, heterogeneous, and arbitrarily nestable
- Arrays of object references

=================================== ===========================================
Operation                           Interpretation
=================================== ===========================================
()                                  An empty tuple
T = (0,)                            A one-item tuple (not an expression)
T = (0, 'Ni', 1.2, 3)               A four-item tuple
T = 0, 'Ni', 1.2, 3                 Another four-item tuple (same as prior line)
T = ('Bob', ('dev', 'mgr'))         Nested tuples
T = tuple('spam')                   Tuple of items in an iterable
T[i]                                Index, index of index, slice, length
T[i][j]
T[i:j]
len(T)
T1 + T2                             Concatenate, repeat
T* 3
for x in T: print(x)                Iteration, membership
'spam' in T
[x ** 2 for x in T]
T.index('Ni')                       Methods in 2.6, 2.7, and 3.X: search, count
T.count('Ni')
namedtuple('Emp', ['name', 'jobs']) Named tuple extension type
=================================== ===========================================

`Named tuple <https://docs.python.org/3.4/library/collections.html#collections.namedtuple>`_
  Immutable records

Sets
----

- Unordered collections of arbitrary objects
- Accessed by iteration, membership test, not offset position
- Variable-length, heterogeneous, and arbitrarily nestable
- Of the category “mutable mapping”
- Collections of object references

Notes: largely because of their implementation, sets can only contain immutable
  (a.k.a. "hashable", __hash__) object types. Hence, lists and dictionaries
  cannot be embedded in sets, but tuples can if you need to store compound values.

::

  >>> x = set('abcde')
  >>> y = set('bdxyz')

  >>> x
  set(['a', 'c', 'b', 'e', 'd'])

  >>> x − y                                         # Difference
  set(['a', 'c', 'e'])

  >>> x | y                                         # Uninon
  set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])

  >>> x & y                                         # Intersection
  set(['b', 'd'])

  >>> x ^ y                                         # Symmetric difference (XOR)
  set(['a', 'c', 'e', 'y', 'x', 'z'])

  >>> x > y, x < y                                  # Superset, subset
  (False, False)

  >>> 'e' in x                                      # Membership
  True

  >>> z = x.intersection(y)                         # Same as x & y
  >>> z
  set(['b', 'd'])

  >>> z.add('SPAM')                                 # Insert one item
  >>> z
  set(['b', 'd', 'SPAM'])

  >>> z.update(set(['X', 'Y']))                     # Merge: in-place union
  >>> z
  set(['Y', 'X', 'b', 'd', 'SPAM'])

  >>> z.remove('b')                                 # Delete one item
  >>> z
  set(['Y', 'X', 'd', 'SPAM'])

  >>> for item in set('abc'): print(item * 3)       # Iterable, unordered
  aaa
  ccc
  bbb

  >>> {i for i in 'abc'}                            # Set compression
  set(['a', 'c', 'b'])

`fronzenset <https://docs.python.org/3.4/library/stdtypes.html#set-types-set-frozenset>`_
  The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.


:Immutables:
  numbers, strings, tuples, frozensets

:Mutables:
  lists, dicts, sets, bytearray

See `Scala's mutable and immutable collections <http://docs.scala-lang.org/overviews/collections/overview.html>`_

Files
-----


===================================== =====================================================
Operation                             Interpretation
===================================== =====================================================
output = open(r'C:\spam', 'w')        Create output file ('w' means write)
input = open('data', 'r')             Create input file ('r' means read)
input = open('data')                  Same as prior line ('r' is the default)
aString = input.read()                Read entire file into a single string
aString = input.read(N)               Read up to next N characters (or bytes) into a string
aString = input.readline()            Read next line (including \n newline) into a string
aList = input.readlines()             Read entire file into list of line strings (with \n)
output.write(aString)                 Write a string of characters (or bytes) into file
output.writelines(aList)              Write all line strings in a list into file
output.close()                        Manual close (done for you when file is collected)
output.flush()                        Flush output buffer to disk without closing
anyFile.seek(N)                       Change file position to offset N for next operation
for line in open('data'): use line    File iterators read line by line
open('f.txt', encoding='latin-1')     Python 3.X Unicode text files (str strings)
open('f.bin', 'rb')                   Python 3.X bytes files (bytes strings)
codecs.open('f.txt', encoding='utf8') Python 2.X Unicode text files (unicode strings)
open('f.bin', 'rb')                   Python 2.X bytes files (str strings)
===================================== =====================================================

Storing Native Python Objects: pickle

::

  >>> D = {'a': 1, 'b': 2}
  >>> F = open('datafile.pkl', 'wb')
  >>> import pickle
  >>> pickle.dump(D, F)                   # Pickle any object to file
  >>> F.close()

  >>> F = open('datafile.pkl', 'rb')
  >>> E = pickle.load(F)                  # Load any object from file
  >>> E
  {'a': 1, 'b': 2}

  >>> open('datafile.pkl', 'rb').read()   # Format is prone to change!
  b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\x02X\x01\x00\x00\x00aq\x02K\x01u.'


Storing Python Objects in JSON Format

::

  >>> name = dict(first='Bob', last='Smith')
  >>> rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
  >>> rec
  {'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}

  >>> import json
  >>> S = json.dumps(rec)
  >>> S
  '{"job": ["dev", "mgr"], "name": {"last": "Smith", "first": "Bob"}, "age": 40.5}'

  >>> O = json.loads(S)
  >>> O
  {'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
  >>> O == rec
  True

  >>> json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
  >>> print(open('testjson.txt').read())
  {
      "job": [
          "dev",
          "mgr" ],
      "name": {
          "last": "Smith",
          "first": "Bob"
      },
      "age": 40.5
  }
  >>> P = json.load(open('testjson.txt'))
  >>> P
  {'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}


Storing Packed Binary Data: struct

  `Format characters <https://docs.python.org/3.4/library/struct.html#format-characters>`_

::

  >>> F = open('data.bin', 'wb')                    # Open binary output file
  >>> import struct
  >>> data = struct.pack('>i4sh', 7, b'spam', 8)    # Make packed binary data
  >>> data
  b'\x00\x00\x00\x07spam\x00\x08'
  >>> F.write(data)                                 # Write byte string
  >>> F.close()

  >>> F = open('data.bin', 'rb')                    # Get packed binary data
  >>> data = F.read()
  >>> data
  b'\x00\x00\x00\x07spam\x00\x08'
  >>> values = struct.unpack('>i4sh', data)         # Convert to Python objects
  >>> values
  (7, b'spam', 8)


File Context Managers

::

  with open(r'C:\code\data.txt') as myfile:
    for line in myfile:
      ...use line here...

  =>

  myfile = open(r'C:\code\data.txt')
  try:
    for line in myfile:
      ...use line here...
  finally:
    myfile.close()


.. _PEP 0237: http://legacy.python.org/dev/peps/pep-0237/
.. _PEP 0238: http://legacy.python.org/dev/peps/pep-0238/
.. _PEP 3141: http://legacy.python.org/dev/peps/pep-3141/
.. _Operator precedence: https://docs.python.org/3.4/reference/expressions.html#operator-precedence
.. _Built-in functions: https://docs.python.org/3.4/library/functions.html#built-in-functions
.. _Ordering Comparisions: https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons
.. _Changed syntax: https://docs.python.org/3/whatsnew/3.0.html#changed-syntax
.. _String methods: https://docs.python.org/3/library/stdtypes.html#string-methods
.. _printf-style String Formatting: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
.. _Text vs. data instead of unicode vs. 8-bit: https://docs.python.org/3/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit
.. _Unicode HOWTO: https://docs.python.org/3/howto/unicode.html#unicode-howto
