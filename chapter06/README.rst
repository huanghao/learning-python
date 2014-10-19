Modules and Packages
====================

Modules are processed with two statemets and one important function:

import
  Lets a client fetch a module as a whole

from
  Allows clients to fetch particular names from a module

imp.reload (reload in 2.x)
  Provides a way to reload a module's code without stopping Python

At a base level, a Python program consists of text files containing Python statements, with one main top-level file, and zero or more supplemental files known as modules.

::

  def spam(text):           # File b.py
    print(text, 'spam')

  import b                  # File a.py
  b.spam('gumby')           # Prints 'gumby spam'

Import statements are executed at runtime, their net effect is to assign module names—simple variables like b—to loaded module objects.
Objects defined by a module are also created at runtime, as the import is executing: every name assigned at the top-level of the file becomes an attribute of the module, accessible to importers. 

How imports work
----------------

1. Find the module's file.
2. Compile it to byte code (if needed).
3. Run the module's code to build the objects it defines.

Module search path:

1. the home directory of the program
2. PYTHONPATH (if set)
3. Standard lib directories
4. The content of any .pth files (if present)
5. The site-packages home of third-party extensions

Ultimately, the concatenation of these four components becomes sys.path, a mutable list of directory name.

Byte code files: .pyc, __pycache__(3.2+)

Because module names become variable names inside a Python program (without the .py), they should also follow the normal variable name rules.

Imports happen only once

::

  print('Hello')    # simple.py
  spam = 1

  >>> import simple
  Hello
  >>> import simple
  >>> simple.spam
  1
  >>> simple.spam = 2
  >>> import simple
  >>> simple.spam
  2

`sys.modules <https://docs.python.org/3.5/library/sys.html#sys.modules>`_
  This is a dictionary that maps module names to modules which have already been loaded.

::

  >>> 'simple' in sys.modules.keys()
  True
  >>> sys.modules['simple']
  <module 'simple' from '/Users/huanghao/workspace/learning-python/chapter06/simple.py'>

Import and from are assignments

  Just like def, import and from are executable statements, not compile-time declarations. They may be nested in if tests, to select among options; appear in function defs, to be loaded only on calls (subject to the preceding note); be used in try statements, to pro- vide defaults; and so on. They are not resolved or run until Python reaches them while executing your program. In other words, imported modules and names are not available until their associated import or from statements run.

Reloading modules

::

  >>> simple.spam
  2
  >>> import imp
  >>> imp.reload(simple)
  Hello
  <module 'simple' from '/Users/huanghao/workspace/learning-python/chapter06/simple.py'>
  >>> simple.spam
  1

Module usage
------------

The import statement::

  >>> import module1                    # Get module as a whole (one or more)
  >>> module1.printer('Hello world!')   # Qualify to get names
  Hello world!

  >>> import module1 as module2

The from statement::

  >>> from module1 import printer       # Copy out a variable (one or more)
  >>> printer('Hello world!')           # No need to qualify name
  Hello world!

  >>> from module1 import printer as display

The from \* statement::

  >>> from module1 import *             # Copy out _all_ variables
  >>> printer('Hello world!')
  Hello world!

Packages
--------

A directory of Python code is said to be a package, so such imports are known as package imports.

::

  import dir1.dir2.mod

::

  dir0 $ tree dir1
  dir1
  |-- __init__.py
  |-- __pycache__
  |   `-- __init__.cpython-34.pyc
  `-- dir2
      |-- __init__.py
      |-- __pycache__
      |   |-- __init__.cpython-34.pyc
      |   `-- mod.cpython-34.pyc
      `-- mod.py

  3 directories, 6 files

Package __init__.py file

dir0/dir1/dir2/mod.py

- dir1 and dir2 both must contain an __init__.py file.
- dir0, the container, does not require an __init__.py file; this file will simply be ignored if present.
- dir0, not dir0/dir1, must be listed on the module search path sys.path.

Package initialization file roles

- Package initialization
- Module usability declarations
- Module namespace initialization
- from \* statmenet behavior

::

  print('dir1 init')    # dir1/__init__.py
  x = 1

  print('dir2 init')    # dir1/dir2/__init__.py
  y = 2

  print('in mod.py')    # dir1/dir2/mod.py
  z = 3

::

  >>> import dir1.dir2.mod
  dir1 init
  dir2 init
  in mod
  >>> import dir1.dir2.mod

  >>> from imp import reload
  >>> reload(dir1)
  dir1 init
  <module 'dir1' from './dir1/__init__.py'>
  >>> reload(dir1.dir2)
  dir2 init
  <module 'dir1.dir2' from './dir1/dir2/__init__.py'>
  >>> reload(dir1.dir2.mod)
  in mod
  <module 'dir1.dir2.mod' from './dir1/dir2/mod.py'>

  >>> dir1.x
  1
  >>> dir1.dir2.y
  2
  >>> dir1.dir2.mod.z
  3

::

  >>> dir2.y
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'dir2' is not defined
  >>> from dir1 import dir2
  >>> dir2.y
  2

Relative imports
----------------

- Imports with dots: both 3.x and 2.x, it's relative-only and will not look sys.path
- Imports without dots: in 2.x, relative-then-absolute; in 3.x, it's absolute-only

::

  from . import spam                        # Relative to this package
  from .spam import name

  from .string import name1, name2          # Imports names from mypkg.string 
  from . import string                      # Imports mypkg.string
  from .. import string                     # Imports string sibling of mypkg

  from __future__ import absolute_import    # Use 3.X relative import model in 2.X


See `PEP 0328 <http://legacy.python.org/dev/peps/pep-0328/>`_ - Imports: Multi-Line and Absolute/Relative

Python3.3 namespace packages
----------------------------

Allows packages to span multiple directories, and requires no initialization file.

`Specification <http://legacy.python.org/dev/peps/pep-0420/#specification>`_

  Regular packages will continue to have an __init__.py and will reside in a single directory.

  Namespace packages cannot contain an __init__.py. As a consequence, pkgutil.extend_path and pkg_resources.declare_namespace become obsolete for purposes of namespace package creation. There will be no marker file or directory for specifying a namespace package.

  During import processing, the import machinery will continue to iterate over each directory in the parent path as it does in Python 3.2. While looking for a module or package named "foo", for each directory in the parent path:

  - If <directory>/foo/__init__.py is found, a regular package is imported and returned.
  - If not, but <directory>/foo.{py,pyc,so,pyd} is found, a module is imported and returned. The exact list of extension varies by platform and whether the -O flag is specified. The list here is representative.
  - If not, but <directory>/foo is found and is a directory, it is recorded and the scan continues with the next directory in the parent path.
  - Otherwise the scan continues with the next directory in the parent path.

  If the scan completes without returning a module or package, and at least one directory was recorded, then a namespace package is created. The new namespace package:

  - Has a __path__ attribute set to an iterable of the path strings that were found and recorded during the scan.
  - Does not have a __file__ attribute.

  Note that if "import foo" is executed and "foo" is found as a namespace package (using the above rules), then "foo" is immediately created as a package. The creation of the namespace package is not deferred until a sub-level import occurs.

  A namespace package is not fundamentally different from a regular package. It is just a different way of creating packages. Once a namespace package is created, there is no functional difference between it and a regular package.


::

  $ tree ns
  ns
  |-- dir1
  |   `-- sub
  |       `-- mod1.py
  `-- dir2
      `-- sub
          `-- mod2.py

  $ cat ns/dir1/sub/mod1.py
  print('dir1/sub.mod1')

  $ cat ns/dir2/sub/mod2.py
  print('dir2/sub.mod2')

  $ PYTHONPATH=./ns/dir1:./ns/dir2 python3

::

  >>> import sub
  >>> sub
  <module 'sub' (namespace)>
  >>> sub.__path__
  _NamespacePath(['./ns/dir1/sub', './ns/dir2/sub'])

  >>> from sub import mod1
  dir1/sub.mod1
  >>> import sub.mod2
  dir2/sub.mod2

  >>> mod1
  <module 'sub.mod1' from './ns/dir1/sub/mod1.py'>
  >>> sub.mod2
  <module 'sub.mod2' from './ns/dir2/sub/mod2.py'>


Namespace package nesting

::

  $ mkdir ns/dir2/sub/lower
  $ echo "print('dir2/sub.lower.mod3')" > ns/dir2/sub/lower/mod3.py

::

  >>> import sub.lower.mod3
  dir2/sub.lower.mod3
  >>> sub.lower
  <module 'sub.lower' (namespace)>
  >>> sub.lower.__path__
  _NamespacePath(['./ns/dir2/sub/lower'])


Mix regular packages with namespace packages

::

  $ tree ns
  ns
  |-- dir1
  |   |-- empty
  |   `-- sub
  |       `-- mod1.py
  `-- dir2
      `-- sub
          |-- lower
          |   `-- mod3.py
          |-- mod2.py
          `-- pkg
              `-- __init__.py

::

    >>> import empty
    >>> empty
    <module 'empty' (namespace)>
    >>> empty.__path__
    _NamespacePath(['./ns/dir1/empty'])

    >>> import sub.pkg
    dir2/sub2.pkg.__init__
    >>> sub.pkg.__file__
    './ns/dir2/sub/pkg/__init__.py'


See `PEP 420 <http://legacy.python.org/dev/peps/pep-0420/>`_: Implicit Namespace Packages

Data hiding in modules
----------------------

_X

::

  $ cat unders.py
  a, _b, c, _d = 1, 2, 3, 4

::

  >>> from unders import *
  >>> a, c
  (1, 3)
  >>> _b
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name '_b' is not defined

  >>> from unders import _b, _d
  >>> _b, _d
  (2, 4)


__all__

::

  $ cat alls.py
  __all__ = ['a', '_c']       # __all__ has precedence over _X
  a, b, _c, _d = 1, 2, 3, 4

::

  >>> from alls import *
  >>> a, _c
  (1, 3)
  >>> b
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'b' is not defined

  >>> from alls import b, _d
  >>> b, _d
  (2, 4)

Enable future language features: __future__
-------------------------------------------

::

  from __future__ import featurename

When used in a script, this statement must appear as the first executable statement in the file (possibly following a docstring or comment), because it enables special compilation of code on a per-module basis. 

::

  >>> import __future__
  >>> dir(__future__)
  ['CO_FUTURE_ABSOLUTE_IMPORT', 'CO_FUTURE_BARRY_AS_BDFL', 'CO_FUTURE_DIVISION', 'CO_FUTURE_PRINT_FUNCTION', 'CO_FUTURE_UNICODE_LITERALS', 'CO_FUTURE_WITH_STATEMENT', 'CO_GENERATOR_ALLOWED', 'CO_NESTED', '_Feature', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'absolute_import', 'all_feature_names', 'barry_as_FLUFL', 'division', 'generators', 'nested_scopes', 'print_function', 'unicode_literals', 'with_statement']

__name__ and __main__
---------------------

- If the file is being run as a top-level program file, __name__ is set to the string "__main__" when it starts.
- If the file is being imported instead, __name__ is set to the module’s name as known by its clients.

::

  def test():
    print(":)")

  if __name__ == '__main__':
    test()

::

  $ python runme.py
  :)
  $ python -m runme
  :)

Docstrings
----------

Just like docstring of function, the first string in a python file works as docstring of that module.

::

  >>> import socket
  >>> help(socket)
  Help on module socket:

  NAME
      socket

  MODULE REFERENCE
      http://docs.python.org/3.4/library/socket

      The following documentation is automatically generated from the Python
      source files.  It may be incomplete, incorrect or include features that
      are considered implementation detail and may vary between Python
      implementations.  When in doubt, consult the module reference at the
      location listed above.
  ...
