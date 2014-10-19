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
