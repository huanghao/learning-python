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
  expression **coding[=:]\s*([-\w.]+)**. The recommended forms of this expression are::

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

Statements
----------

=========
Statement
Assignment
Calls and other expressions
print calls

.. _The Python Language Reference: https://docs.python.org/3/reference/index.html
.. _Special method names: https://docs.python.org/3/reference/datamodel.html#specialnames
.. _string_and_bytes_literal: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
.. _integer_literal: https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
.. _float_literal: https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals
.. _imaginary_literal: https://docs.python.org/3/reference/lexical_analysis.html#imaginary-literals
