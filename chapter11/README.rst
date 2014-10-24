Text processing
===============

string — Common string operations
---------------------------------

`3.4 <https://docs.python.org/3.4/library/string.html>`_

`2.7 <https://docs.python.org/2/library/string.html>`_

Constants::

  >>> string.ascii_letters
  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  >>> string.ascii_lowercase
  'abcdefghijklmnopqrstuvwxyz'
  >>> string.ascii_uppercase
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  >>> string.digits
  '0123456789'
  >>> string.hexdigits
  '0123456789abcdefABCDEF'
  >>> string.octdigits
  '01234567'
  >>> string.punctuation
  '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
  >>> string.printable
  '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
  >>> string.whitespace
  ' \t\n\r\x0b\x0c'


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

Quiz: explain these meta characters: ``. ^ $ * + ? { } [ ] \ | ( )``

`Flags <https://docs.python.org/3.4/library/re.html#re.A>`_

Raw string

Regex methods

- search
- match: ^ + search
- fullmatch: ^ + search + $
- split: general form of str.split
- findall: returns groups
- finditer: returns iteration of match objects
- sub: general form of str.replace
- escape: match meta chars

Match object

- expand
- group: 0(the whole)
- groups: groups from 1
- groupdict
- start
- end
- span

Example: router.py

See also `Regular Expression HOWTO <https://docs.python.org/3.4/howto/regex.html#regex-howto>`_

Structed text
-------------

JSON & YAML & XML

`JSON <https://docs.python.org/3.4/library/json.html>`_: JavaScript Object Notation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Encoding basic Python object hierarchies::

  >>> import json
  >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
  '["foo", {"bar": ["baz", null, 1.0, 2]}]'
  >>> print(json.dumps("\"foo\bar"))
  "\"foo\bar"
  >>> print(json.dumps('\u1234'))
  "\u1234"
  >>> print(json.dumps('\\'))
  "\\"
  >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
  {"a": 0, "b": 0, "c": 0}
  >>> from io import StringIO
  >>> io = StringIO()
  >>> json.dump(['streaming API'], io)
  >>> io.getvalue()
  '["streaming API"]'

Compact encoding::

  >>> json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':'))
  '[1,2,3,{"4":5,"6":7}]'
  Pretty printing:

  >>>
  >>> import json
  >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
  {
      "4": 5,
      "6": 7
  }

Decoding JSON::

  >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
  ['foo', {'bar': ['baz', None, 1.0, 2]}]
  >>> json.loads('"\\"foo\\bar"')
  '"foo\x08ar'
  >>> from io import StringIO
  >>> io = StringIO('["streaming API"]')
  >>> json.load(io)
  ['streaming API']

Specializing JSON object decoding::

  >>> def as_complex(dct):
  ...     if '__complex__' in dct:
  ...         return complex(dct['real'], dct['imag'])
  ...     return dct
  ...
  >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
  ...     object_hook=as_complex)
  (1+2j)
  >>> import decimal
  >>> json.loads('1.1', parse_float=decimal.Decimal)
  Decimal('1.1')

Extending JSONEncoder::

  >>> class ComplexEncoder(json.JSONEncoder):
  ...     def default(self, obj):
  ...         if isinstance(obj, complex):
  ...             return [obj.real, obj.imag]
  ...         # Let the base class default method raise the TypeError
  ...         return json.JSONEncoder.default(self, obj)
  ...
  >>> json.dumps(2 + 1j, cls=ComplexEncoder)
  '[2.0, 1.0]'
  >>> ComplexEncoder().encode(2 + 1j)
  '[2.0, 1.0]'
  >>> list(ComplexEncoder().iterencode(2 + 1j))
  ['[2.0', ', 1.0', ']']

Using json.tool from the shell to validate and pretty-print::

  $ echo '{"json":"obj"}' | python -mjson.tool
  {
      "json": "obj"
  }
  $ echo '{1.2:3.4}' | python -mjson.tool
  Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

See `json.org <http://json.org/>`_

YAML: YAML Ain't Markup Language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PyYAML <https://pypi.python.org/pypi/PyYAML/3.11>`_

::

  >>> import yaml

  >>> print yaml.load("""
  ... name: Vorlin Laruknuzum
  ... sex: Male
  ... class: Priest
  ... title: Acolyte
  ... hp: [32, 71]
  ... sp: [1, 13]
  ... gold: 423
  ... inventory:
  ... - a Holy Book of Prayers (Words of Wisdom)
  ... - an Azure Potion of Cure Light Wounds
  ... - a Silver Wand of Wonder
  ... """)

  {'name': 'Vorlin Laruknuzum', 'gold': 423, 'title': 'Acolyte', 'hp': [32, 71],
  'sp': [1, 13], 'sex': 'Male', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)',
  'an Azure Potion of Cure Light Wounds', 'a Siver Wand of Wonder'], 'class': 'Priest'}

  >>> print yaml.dump({'name': "The Cloak 'Colluin'", 'depth': 5, 'rarity': 45,
  ... 'weight': 10, 'cost': 50000, 'flags': ['INT', 'WIS', 'SPEED', 'STEALTH']})

  name: The Cloak 'Colluin'
  rarity: 45
  flags: [INT, WIS, SPEED, STEALTH]
  weight: 10
  cost: 50000
  depth: 5

XML
~~~

`xml.etree.ElementTree <https://docs.python.org/3.4/library/xml.etree.elementtree.html>`_: xmltest.py

XPath syntax:

================= ==========================================================================================================================================================================================================================================
Syntax            Meaning
================= ==========================================================================================================================================================================================================================================
tag               Selects all child elements with the given tag. For example: spam, spam/egg
\*                Selects all child elements. For example, \*/egg
\.                Selects the current node.
//                Selects all subelements, on all levels beneath the current element. For example, .//egg
\.\.              Selects the parent element.
[@attrib]         Selects all elements that have the given attribute.
[@attrib='value'] Selects all elements for which the given attribute has the given value. The value cannot contain quotes.
[tag]             Selects all elements that have a child named tag. Only immediate children are supported.
[position]        Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1).
================= ==========================================================================================================================================================================================================================================

::

  # Top-level elements
  root.findall(".")

  # All 'neighbor' grand-children of 'country' children of the top-level
  # elements
  root.findall("./country/neighbor")

  # Nodes with name='Singapore' that have a 'year' child
  root.findall(".//year/..[@name='Singapore']")

  # 'year' nodes that are children of nodes with name='Singapore'
  root.findall(".//*[@name='Singapore']/year")

  # All 'neighbor' nodes that are the second child of their parent
  root.findall(".//neighbor[2]")

Building xml documents::

  >>> data = ET.Element('data')
  >>> jm = ET.SubElement(data, 'artist')
  >>> jm.attrib['name'] = 'John Mayer'
  >>> j5 = ET.SubElement(data, 'artist')
  >>> j5.attrib['name'] = 'John 5'
  >>> rock = ET.SubElement(j5, 'genre')
  >>> rock.text = 'Instrumental Rock'
  >>> ET.dump(data)
  <data><artist name="John Mayer" /><artist name="John 5"><genre>Instrumental Rock</genre></artist></data>

Also see: lxml


HTML text
---------

See `html <https://docs.python.org/3.4/library/html.html>`_ - HyperText Markup Language support

`PyQuery <https://pythonhosted.org/pyquery/>`_ - a jquery-like lib for python

::

  >>> from pyquery import PyQuery as pq
  >>> from lxml import etree
  >>> d = pq("<html></html>")
  >>> d = pq(etree.fromstring("<html></html>"))
  >>> d = pq(url='http://google.com/')
  >>> d = pq(filename=path_to_html_file)

Now d is like the \$ in jquery::

  >>> d("#hello")
  [<p#hello.hello>]
  >>> p = d("#hello")
  >>> print(p.html())
  Hello world !
  >>> p.html("you know <a href='http://python.org/'>Python</a> rocks")
  [<p#hello.hello>]
  >>> print(p.html())
  you know <a href="http://python.org/">Python</a> rocks
  >>> print(p.text())
  you know Python rocks
  >>> d('p:first')
  [<p#hello.hello>]

Also see: BeautifulSoup


Template system
---------------

`Format <https://docs.python.org/3.4/library/string.html#formatspec>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

Jinja2
~~~~~~

::

  >>> from jinja2 import Template
  >>> template = Template('Hello {{ name }}!')
  >>> template.render(name='John Doe')
  'Hello John Doe!'

Variables::

  {{ foo.bar }}
  {{ foo['bar'] }}

`Filters <http://jinja.pocoo.org/docs/dev/templates/#builtin-filters>`_::

  {{ name|striptags|title }}
  {{ list|join(', ') }}

Loop::

  <ul>
  {% for item in seq %}
      <li>{{ item }}</li>
  {% endfor %}
  </ul>

Tests::

  {% if loop.index is divisibleby 3 %}
  {% if loop.index is divisibleby(3) %}

Comments::

  {# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
  #}

Template Inheritance::

  # Base template

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
  <html lang="en">
  <html xmlns="http://www.w3.org/1999/xhtml">
  <head>
      {% block head %}
      <link rel="stylesheet" href="style.css" />
      <title>{% block title %}{% endblock %} - My Webpage</title>
      {% endblock %}
  </head>
  <body>
      <div id="content">{% block content %}{% endblock %}</div>
      <div id="footer">
          {% block footer %}
          &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
          {% endblock %}
      </div>
  </body>

  # Child template

  {% extends "base.html" %}
  {% block title %}Index{% endblock %}
  {% block head %}
      {{ super() }}
      <style type="text/css">
          .important { color: #336699; }
      </style>
  {% endblock %}
  {% block content %}
      <h1>Index</h1>
      <p class="important">
        Welcome on my awesome homepage.
      </p>
  {% endblock %}

Include::

  {% include 'header.html' %}
    Body
  {% include 'footer.html' %}

See `Template Designer Documentation <http://jinja.pocoo.org/docs/dev/templates/>`_

web.py

Also see: Mako

Lexical and syntax parser
-------------------------

`Python Lex-Yacc <http://www.dabeaz.com/ply/>`_

navie_lisp.py
