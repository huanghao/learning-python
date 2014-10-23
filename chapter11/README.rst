Text processing
===============

String lib
----------

Note: Only available in py2

Safely eval
-----------

::

  def convert_string_into_dict(dictstring):
    return eval(dictstring)     # bad idea

ast.literal_eval(node_or_string)
  Safely evaluate an expression node or a string containing a Python expression. The string or node provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.

This can be used for safely evaluating strings containing Python expressions from untrusted sources without the need to parse the values oneself.

`Regular expression <https://docs.python.org/3.4/library/re.html>`_
-------------------------------------------------------------------

Baisc usage::

  >>> import re
  >>> string = 'abc1234def'
  >>> pattern = r'[0-9]+'
  >>> re.search(pattern, string)
  <_sre.SRE_Match object; span=(3, 7), match='1234'>

`Syntax <https://docs.python.org/3.4/library/re.html#regular-expression-syntax>`_

Quiz: explain these meta chars: ``. ^ $ * + ? { } [ ] \ | ( )``

`Flags <https://docs.python.org/3.4/library/re.html#re.A>`_

search vs. match



See also `Regular Expression HOWTO <https://docs.python.org/3.4/howto/regex.html#regex-howto>`_

Structed text
-------------

XML & JSON & YAML, lxml, untangle, xmltodict, json, pyyaml

HTML text
---------

PyQuery & BeautifulSoup

Templates system
----------------

Templates, Jinja2, Mako

Logging
-------

Logging

Lexical and syntax parser
-------------------------

- shlex
- Lex & Yacc, ply


