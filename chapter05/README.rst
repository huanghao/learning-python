Functions
=========

def
---

Format::

  def name(arg1, arg2, ..., argN):
    ...
    [return value]

Executes at runtime::

  if test:
    def func():
      print 'Define func this way'
  else:
    def func():
      print 'Or else this way'
  ...
  func()    # Call the func defined

Scopes
------

- If a variable is assigned inside a def, it is *local* to that function.
- If a variable is assigned in an enclosing def, it is *nonlocal* to nested functions.
- If a variable is assigned outside all defs, it is *global* to the entire file.

::

  x = 99          # Global(module)

  def func():
    x = 88        # Local(func): a different variable

    def inner():
      print(x)    # Nonlocal(inner)

Name Resolution: The LEGB Rule

- Name assignments create or change local names by default.
- Name references search at most four scopes: local(L), then enclosing(E) functions (if any), then global(G), then built-in(B).
- Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes, respectively.

The built-in scope::

  >>> import builtins
  >>> dir(builtins)
  ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
  >>> zip
  <class 'zip'>
  >>> zip is builtins.zip
  True

Use *global* and *nonlocal* for changes::

  >>> x = 99
  >>> def func():
  ...   global x
  ...   x = 88
  ...
  >>> print(x)
  99
  >>> func()
  >>> print(x)
  88

  >>> def func():
  ...   x = 88
  ...   def inner():
  ...     nonlocal x
  ...     x = 77
  ...   print(x)
  ...   inner()
  ...   print(x)
  ...
  >>> func()
  88
  77

  >>> x = 99
  >>> def func():
  ...   nonlocal x
  ...   x = 88
  ...
    File "<stdin>", line 2
  SyntaxError: no binding for nonlocal 'x' found

See `PEP 3104 <http://www.python.org/dev/peps/pep-3104>`_: nonlocal statement. Using nonlocal x you can now assign directly to a variable in an outer (but non-global) scope. nonlocal is a new reserved word

Arguments
---------

Argument Matching Basics

- Positionals: matched from left to right
- Keywords: matched by argument name
- Defaults: specify values for optional arguments that aren’t passed
- Varargs collecting: collect arbitrarily many positional or keyword arguments
- Varargs unpacking: pass arbitrarily many positional or keyword arguments
- Keyword-only arguments: arguments that must be passed by name

======================== ================================================================
Syntax                   Interpretation
======================== ================================================================
func(value)              Normal argument: matched by position
func(name=value)         Keyword argument: matched by name
func(\*iterable)         Pass all objects in iterable as individual positional arguments
func(\*\*dict)           Pass all key/value pairs in dict as individual keyword arguments
def func(name)           Normal argument: matches any passed value by position or name
def func(name=value)     Default argument value, if not passed in the call
def func(\*name)         Matches and collects remaining positional arguments in a tuple
def func(\*\*name)       Matches and collects remaining keyword arguments in a dictionary
def func(\*other, name)  Arguments that must be passed by keyword only in calls (3.X)
def func(\*, name=value) Arguments that must be passed by keyword only in calls (3.X)
======================== ================================================================

::

  >>> def f(a, *pargs, **kargs): print(a, pargs, kargs)
  >>> f(1, 2, 3, x=1, y=2)
  1 (2, 3) {'y': 2, 'x': 1}

  >>> def func(a, b, c, d): print(a, b, c, d)
  >>> args = (1, 2)
  >>> args += (3, 4)
  >>> func(*args)     # Same as func(1, 2, 3, 4)
  1 2 3 4

  >>> args = {'a': 1, 'b': 2, 'c': 3}
  >>> args['d'] = 4
  >>> func(**args)    # Same as func(a=1, b=2, c=3, d=4)
  1 2 3 4

  >>> func(*(1, 2), **{'d': 4, 'c': 3})   # Same as func(1, 2, d=4, c=3)
  1 2 3 4
  >>> func(1, *(2, 3), **{'d': 4})        # Same as func(1, 2, 3, d=4)
  1 2 3 4
  >>> func(1, c=3, *(2,), **{'d': 4})     # Same as func(1, 2, c=3, d=4)
  1 2 3 4
  >>> func(1, *(2, 3), d=4)               # Same as func(1, 2, 3, d=4)
  1 2 3 4
  >>> func(1, *(2,), c=3, **{'d':4})      # Same as func(1, 2, c=3, d=4)
  1 2 3 4

Quiz: Write a function max accepts any number of arguments and returns the bigest of them.

3.x keyword-only arguments::

  >>> def kwonly(a, *b, c, **d): print(a, b, c, d)
  >>> kwonly(1, 2, c=3)
  1 (2,) 3 {}
  >>> kwonly(a=1, c=3)
  1 () 3 {}
  >>> kwonly(1, 2, 3)
  TypeError: kwonly() missing 1 required keyword-only argument: 'c'
  >>> kwonly(1, 2, c=3, d=4, e=5)
  1 (2,) 3 {'d':4, 'e': 5}

Keyword-only arguments must be specified after a single star, not two.
  Named arguments cannot appear after the \*\*args arbitrary keywords form,
  and a \*\* can’t appear by itself in the arguments list. 

::

  >>> def kwonly(a, **pargs, b, c):
  SyntaxError: invalid syntax
  >>> def kwonly(a, **, b, c):
  SyntaxError: invalid syntax

Why keyword-only arguments ?

::

  def process(*args, notify=False): ...

  process(X, Y, Z)            # Use flag's default
  process(X, Y, notify=True)  # Override flag default

Without keyword-only arguments we have to use both \*args and \*\*args and manually inspect the keywords, but with keyword-only arguments less code is required.

Quiz: try to implement the same feature above without using keyword-only arguments.

Function design principles
--------------------------

- use arguments for inputs and return for outputs.
- use global variables only when truly necessary.
- don’t change mutable arguments unless the caller expects it.
- each function should have a single, unified purpose.
- each function should be relatively small.
- avoid changing variables in another module file directly.

"First Class" Objects
---------------------

Python functions are full-blown objects::

  >>> schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]
  >>> for (func, arg) in schedule:
  func(arg)

Function Introspection
----------------------

::

  >>> def mul(a, b):
  ...   """Multiple a by b times"""
  ...   return a * b
  ...
  >>> mul('spam', 8)
  'spamspamspamspamspamspamspamspam'

  >>> mul.__name__
  'mul'
  >>> mul.__doc__
  'Multiple a by b times'

  >>> mul.__code__
  <code object func at 0x104f24c90, file "<stdin>", line 1>
  >>> func.__code__.co_varnames
  ('a', 'b')
  >>> func.__code__.co_argcount
  2

Function Annotations in 3.x
---------------------------


Annotations are completely optional, and when present are simply attached to the function object’s __annotations__ attribute for use by other tools.

::

  >>> def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
  ...     ...
  ...
  >>> foo.__annotations__
  {'a': 'x', 'return': 9, 'c': <class 'list'>, 'b': 11}

See `PEP 3107 <http://www.python.org/dev/peps/pep-3107>`_: Function argument and return value annotations.

Anonymous Functions: lambda
---------------------------

  lambda argument1, argument2,... argumentN : expression using arguments

- lambda is an expression, not a statement.
- lambda’s body is a single expression, not a block of statements.
- annotations are not supported in lambda

Functional programming tools
----------------------------

map, filter, reduce

Generator functions
-------------------

yield vs. return::

  >>> def gensquares(N):
  ...   for i in range(N):
  ...   yield i ** 2
  ...
  >>> for i in gensquares(5): # Resume the function
  ...   print(i, end=' : ')
  ...
  0 : 1 : 4 : 9 : 16 :

  >>> x = gensquares(2)
  >>> x
  <generator object gensquares at 0x000000000292CA68>
  >>> next(x)
  0
  >>> next(x)
  1
  >>> next(x)
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module> StopIteration

  >>> y = gensquares(5)
  >>> iter(y) is y
  True

Why using generators ?

send vs. next::

  >>> def gen():
  ...   for i in range(10):
  ...     x = yield i
  ...     print('x=', x)
  ...
  >>> g = gen()
  >>> next(g)
  0
  >>> g.send(77)
  x= 77
  1
  >>> g.send(88)
  x= 88
  2
  >>> next(g)
  x= None
  3

See `PEP 342 <http://legacy.python.org/dev/peps/pep-0342/>`_ -- Coroutines via Enhanced Generators 

`yield from <https://docs.python.org/3/whatsnew/3.3.html#pep-380-syntax-for-delegating-to-a-subgenerator>`_
  allows a generator to delegate part of its operations to another generator.


For simple iterators, yield from iterable is essentially just a shortened form of *for item in iterable: yield item*::

  >>> def g(x):
  ...     yield from range(x, 0, -1)
  ...     yield from range(x)
  ...
  >>> list(g(5))
  [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]

However, unlike an ordinary loop, yield from allows subgenerators to receive sent and thrown values directly from the calling scope, and return a final value to the outer generator::

  >>> def accumulate():
  ...     tally = 0
  ...     while 1:
  ...         next = yield
  ...         if next is None:
  ...             return tally
  ...         tally += next
  ...
  >>> def gather_tallies(tallies):
  ...     while 1:
  ...         tally = yield from accumulate()
  ...         tallies.append(tally)
  ...
  >>> tallies = []
  >>> acc = gather_tallies(tallies)
  >>> next(acc) # Ensure the accumulator is ready to accept values
  >>> for i in range(4):
  ...     acc.send(i)
  ...
  >>> acc.send(None) # Finish the first tally
  >>> for i in range(5):
  ...     acc.send(i)
  ...
  >>> acc.send(None) # Finish the second tally
  >>> tallies
  [6, 10]

See `PEP 380 <http://www.python.org/dev/peps/pep-0380>`_: Syntax for Delegating to a Subgenerator

`itertools <https://docs.python.org/3.5/library/itertools.html>`_: Functions creating iterators for efficient looping

::

  >>> from itertools import *
  >>> def take(n, iterable):
  ...     "Return first n items of the iterable as a list"
  ...     return list(islice(iterable, n))
  ...
  >>>

  >>> take(10, count(2))
  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  >>> take(10, cycle('abcd'))
  ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
  >>> take(5, repeat(6))
  [6, 6, 6, 6, 6]

  >>> list(accumulate([1,2,3,4,5]))
  [1, 3, 6, 10, 15]
  >>> list(chain('abc', 'ABC'))
  ['a', 'b', 'c', 'A', 'B', 'C']
  >>> list(takewhile(lambda x: x<5, [1,4,6,4,1]))
  [1, 4]

  >>> list(permutations('ABCD', 2))
  [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
  >>> list(combinations('ABCD', 2))
  [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


Function Decorators
-------------------

Decorator is just a function returning another function.
It is merely syntactic sugar, the following two function definitions are semantically equivalent::

  @f1(arg)
  @f2
  def func(): pass

  def func(): pass
  func = f1(arg)(f2(func))

Common examples for decorators are classmethod() and staticmethod()::

  def f(...):
      ...
  f = staticmethod(f)

  @staticmethod
  def f(...):
      ...

`functools <https://docs.python.org/3.5/library/functools.html>`_

::

  >>> def bar(func):
  ...   def inner():
  ...     print('New function')
  ...     return func()
  ...   return inner
  ...
  >>> @bar
  ... def foo():
  ...   print('I am foo')
  ...
  >>> foo()
  New function
  I am foo
  >>> foo.__name__    # It's bad!
  'inner'

  >>> from functools import wraps
  >>> def my_decorator(f):
  ...     @wraps(f)
  ...     def wrapper(*args, **kwds):
  ...         print('Calling decorated function')
  ...         return f(*args, **kwds)
  ...     return wrapper
  ...
  >>> @my_decorator
  ... def example():
  ...     """Docstring"""
  ...     print('Called example function')
  ...
  >>> example()
  Calling decorated function
  Called example function
  >>> example.__name__
  'example'
  >>> example.__doc__
  'Docstring'
