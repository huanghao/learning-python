Exceptions
==========

- try/expect/else/finally
- raise Exc/raise
- assert
- with/as, contextmanager
- Built-in exceptions
- traceback

Basics
------

Default exception handler::

  >>> def fetcher(obj, index):
  ...   return obj[index]
  ...
  >>> x = 'spam'
  >>> fetcher(x, 3)
  m

  >>> fetcher(x, 4)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in fetcher
  IndexError: string index out of range

Catching exception::

  >>> try:
  ...   fetcher(x, 4)
  ... except IndexError:
  ...   print('got exception')
  ... print('continue')
  ...
  got exception
  continue

Raising exceptions::

  >>> raise IndexError('cross the line')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  IndexError: cross the line

  >>> assert False, 'Nobody like it'
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AssertionError: Nobody like it

User-defined exceptions::

  >>> class AlreadyGotOne(Exception): pass
  ...
  >>> def grail():
  ...   raise AlreadyGotOne()
  ...
  >>> try:
  ...   grail()
  ... except AlreadyGotOne:
  ...   print('got exception')
  ...
  got exception

Termination actions::

  >>> try:
  ...   fetcher(x, 3)
  ... finally:
  ...   print('after fetch')
  ...
  'm'
  after fetch

  >>> def after():
  ...   try:
  ...     fetcher(x, 4)
  ...   finally:
  ...     print('after fetch')
  ...   print('after try?')
  ...
  >>> after()
  after fetch
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in after
    File "<stdin>", line 2, in fetcher
  IndexError: string index out of range

Context manager::

  with threading.Lock() as lock:
    do_something()

  # is equivalent to

  lock = threading.Lock()
  lock.acquire()
  try:
    do_something()
  finally:
    lock.release()

  # If we don't use context manager or finally clause

  lock.acquire()
  some_something()    # if exception happens here
  lock.release()      # then this line won't be called

Exception coding detail
-----------------------

try/except/else/finally::

  try:
    some_actions()
  excpet Exception1:
    handler1
  except Exception2:
    handler2
  ...
  except:
    handler all exceptions
  else:
    no_exception_occurs
  finally:
    termination

The raise statement

To trigger exceptions explicitly, you can use the following three forms of raise statements:

- raise instance

  It's the most common way to raise an instance of some exception.

- raise class

  If we pass a class instead, python calls constructor without arguments, to create an instance to raise.

- raise

  This form reraises the most recently raised exception. It's commonly used in exception handlers to
  propagate exceptions that have been caught.

::

  >>> try:
        ..   1/0
  ... except ZeroDivisionError:
  ...   print('oops')
  ...   raise
  ...
  oops
  Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
  ZeroDivisionError: division by zero

Scopes and try except variables

::

  >>> try:     # py3
  ...   1/0
  ... except Exception as x:
  ...   print(x)
  ...
  division by zero
  >>> x
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'x' is not defined

::

  >>> try:     # py2
  ...   1/0
  ... except Exception as x:
  ...   print x
  ...
  integer division or modulo by zero
  >>> x
  ZeroDivisionError('integer division or modulo by zero',)

  >>> try:     # the old py2 way to assign exception variable
  ...   1/0    # which already abandoned in py3
  ... except Exception, x:
  ...   print x
  ...
  integer division or modulo by zero

See `PEP 3110 <http://www.python.org/dev/peps/pep-3110>`_: Catching exceptions.


Catching multiple exceptions in single except::

  >>> import random
  >>> def random_error():
  ...   if random.random() < 0.5:
  ...     1/0
  ...   else:
  ...     [][1]
  ...
  >>> random_error()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 5, in random_error
  IndexError: list index out of range
  >>> random_error()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in random_error
  ZeroDivisionError: integer division or modulo by zero

  >>> def run():
  ...   try:
  ...     random_error()
  ...   except (IndexError, ZeroDivisionError):
  ...     print('got')
  ...
  >>> run()
  got

Careful in py2: the () is essential::

  >>> try:
  ...   random_error()
  ... except IndexError, ZeroDivisionError:   # valid syntax in py2
  ...   print 'got'
  ...
  got
  >>> ZeroDivisionError
  IndexError('list index out of range',)

The 3.x exception chaining: raise from

Exceptions can sometimes be triggered in resonpse to other exceptions - both delibrately and by new program errors.
To support full disclosure in such cases, 3.x support a new raise from syntax:

  raise newexception from otherexception

- If the form clause is used explicitly, the other exception will be attached to __cause__ attribute
  of the new exception being raised. If the raised exception is not caught, python prints out the
  whole exception chain.

::

  >>> try:
  ...   try:
  ...     1/0
  ...   except Exception as e:
  ...     raise TypeError('Bad') from e
  ... except Exception as e:
  ...   raise ValueError('Worse') from e
  ...
  Traceback (most recent call last):
    File "<stdin>", line 3, in <module>
  ZeroDivisionError: division by zero

  The above exception was the direct cause of the following exception:

  Traceback (most recent call last):
    File "<stdin>", line 5, in <module>
  TypeError: Bad

  The above exception was the direct cause of the following exception:

  Traceback (most recent call last):
    File "<stdin>", line 7, in <module>
  ValueError: Worse

- When an exception is raised implicitly by a program error inside an exception handler, a
  similar procedure is followed automatically: the previous exception is attached to the new
  exception's __context__ attribute and is again displayed if uncaught.

::

  >>> try:
  ...   1/0
  ... except:
  ...   badname
  ...
  Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
  ZeroDivisionError: division by zero

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
  NameError: name 'badname' is not defined

See `PEP 3134 <http://www.python.org/dev/peps/pep-3134>`_: Exception chaining.

Suppressing exception context

3.3 introduces a new syntax to disable display of chained exception context.
No debugging capability is lost, as the original exception context remains available if needed.

::

  >>> try:
  ...   1/0
  ... except ZeroDivisionError:
  ...   raise ValueError("zero can't be used as demoninator")
  ...
  Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
  ZeroDivisionError: division by zero

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
  ValueError: zero can't be used as demoninator

::

  >>> def test():
  ...   try:
  ...     1/0
  ...   except ZeroDivisionError:
  ...     raise ValueError("zero can't be used as demoinator") from None
  ...
  >>> test()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 5, in test
  ValueError: zero can't be used as demoinator

  >>> try:
  ...   test()
  ... except Exception as e:
  ...   print(e.__context__)
  ...
  division by zero

See `PEP 409 <http://www.python.org/dev/peps/pep-0409>`_: Suppressing exception context


The assert statement

Just for somewhat debugging and testing purposes.

  assert test, msg    # msg is optional

=>

::

  if __debug__:
    if not test:
      raise AssertError(msg)


Built-in exceptions
-------------------

In Python, all exceptions must be instances of a class that derives from *BaseException*.

Programmers are encouraged to derive new exceptions from the *Exception* class or one of its subclass, and not from *BaseException*.

::

  BaseException
   +-- SystemExit
   +-- KeyboardInterrupt
   +-- GeneratorExit
   +-- Exception
        +-- StopIteration
        +-- ArithmeticError
        |    +-- FloatingPointError
        |    +-- OverflowError
        |    +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        +-- LookupError
        |    +-- IndexError
        |    +-- KeyError
        +-- MemoryError
        +-- NameError
        |    +-- UnboundLocalError
        +-- OSError
        |    +-- BlockingIOError
        |    +-- ChildProcessError
        |    +-- ConnectionError
        |    |    +-- BrokenPipeError
        |    |    +-- ConnectionAbortedError
        |    |    +-- ConnectionRefusedError
        |    |    +-- ConnectionResetError
        |    +-- FileExistsError
        |    +-- FileNotFoundError
        |    +-- InterruptedError
        |    +-- IsADirectoryError
        |    +-- NotADirectoryError
        |    +-- PermissionError
        |    +-- ProcessLookupError
        |    +-- TimeoutError
        +-- ReferenceError
        +-- RuntimeError
        |    +-- NotImplementedError
        +-- SyntaxError
        |    +-- IndentationError
        |         +-- TabError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        |    +-- UnicodeError
        |         +-- UnicodeDecodeError
        |         +-- UnicodeEncodeError
        |         +-- UnicodeTranslateError
        +-- Warning
             +-- DeprecationWarning
             +-- PendingDeprecationWarning
             +-- RuntimeWarning
             +-- SyntaxWarning
             +-- UserWarning
             +-- FutureWarning
             +-- ImportWarning
             +-- UnicodeWarning
             +-- BytesWarning
             +-- ResourceWarning

BaseException
  The base class for all built-in exceptions.

  args: The tuple of arguments given to the exception constructor. If str() is called on an instance of this class, the representation of the argument(s) to the instance are returned, or the empty string when there were no arguments.

  with_traceback(tb)::

    try:
        ...
    except SomeException:
        tb = sys.exc_info()[2]
        raise OtherException(...).with_traceback(tb)

Exception
  All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.

SystemExit
  This exception is raised by the sys.exit() function. When it is not handled, the Python interpreter exits; no stack traceback is printed. If the associated value is an integer, it specifies the system exit status (passed to C’s exit() function); if it is None, the exit status is zero; if it has another type (such as a string), the object’s value is printed and the exit status is one.

::

  >>> try:
  ...   sys.exit(5)
  ... except:
  ...   print(sys.exc_info())
  ...   print("system didn't exit")
  ...
  (<class 'SystemExit'>, SystemExit(5,), <traceback object at 0x103d67648>)
  system didn't exit

KeyboardInterrupt
  Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.

GeneratorExit
  Raised when a generator‘s close() method is called. It directly inherits from BaseException instead of Exception since it is technically not an error.


See `Built-in Exceptions <https://docs.python.org/3.4/library/exceptions.html>`_
