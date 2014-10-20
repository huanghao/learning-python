Classes and OOP
===============


OOP(Object Oriented Programming) concepts
-----------------------------------------

- Classes

  - Inner classes

- Instances
- Methods

  - Instance methods
  - Static methods
  - Class methods
  - Operator overloading

- Attributes

  - Instance attributes
  - Class attributes
  - Properties
  - Special Attributes

- Inheritance

  - Super

- Advanced topics

  - Extending builtin types
  - Classic and New styles
  - Multi-inheritance (MRO)
  - Metaclass

Basic usage
-----------

::

  class Person:
      """
      Class represents a person
      """

      def __init__(self, name, job=None, pay=0):
          """
          Constructor method
          """
          self.name = name
          self.job = job
          self.pay = pay

      def __del__(self):
          """
          Deconstructor: it will be called when gc recycle this object, or *del* called.
          """

      def last_name(self):
          """
          The first argument of instance methods is *self*.
          It's the reference to current instance, just like *this* in C++ and Java.
          """
          return self.name.split()[-1]

      def give_raise(self, percent):
          self.pay = int(self.pay * (1 + percent))


  if __name__ == '__main__':
      bob = Person('Bob Smith')
      sue = Person('Sue Jones', 'engineer', 8000)

      print(bob.last_name(), bob.pay)     # ('Smith', 0)
      sue.give_raise(.1)
      print(sue.last_name(), sue.pay)     # ('Jones', 8800)

Provding print displays::

  >>> print(bob)
  <__main__.Person instance at 0x1031634d0>

  class Person:
    ...

    def __str__(self):
      return self.name

    def __repr__(self):
      return '[%s: %s, %s]' % (self.__class__.__name__, self.name, self.pay)

  >>> bob
  [Person: Bob Smith, 0]
  >>> print(bob)
  Bob Smith

  >>> str(sue)
  'Sue Jones'
  >>> repr(sue)
  '[Person: Sue Jones, 8800]'

Subclasses::

  class Manager(Person):

    def __init__(self, name, pay):
      super().__init__(name, 'manager', pay)

    def give_raise(percent, bouns=.1)
      Person.give_raise(self, percent + bouns)

  >>> tom = Manager('Tom Jones', 'manager', 5000)
  >>> tom.give_raise(.1)
  >>> repr(tom)
  [Manager: Tom Jones, 6000]

Special class attributes::

  >>> tom.__class__
  <class 'person.Manager'>
  >>> tom.__class__.__bases__
  (<class 'person.Person'>,)
  >>> tom.__dict__
  {'job': 'manager', 'name': 'Tom Jones', 'pay': 6000}

Class methods and static methods

Properties #TODO


__dict__ and __weakref__ #TODO

Operator overloadding
---------------------

`Emulating numeric types <https://docs.python.org/3.4/reference/datamodel.html#emulating-numeric-types>`_

::

  class Number:

    def __eq__(self, right):
      ...

    def __add__(self, right):
      ...

    def __sub__(self, right):
      ...

    def __mul__(self, right):
      ...

  ten = two * five
  six - one = ten - five


Full methods list for numeric types

================ ================
Method           Operator
================ ================
__add__          \+
__sub__          \-
__mul__          \*
__truediv__      /
__floordiv__     //
__mod__          %
__divmod__       divmod
__pow__          \*\*, pwer
__lshift__       <<
__rshift__       >>
__and__          &
__xor__          ^
__or__           \|
**__radd__**     \+
**__iadd__**     \+=
__neg__          \-
__pos__          \+
__abs__          abs
__invert__       ~
__complex__      complex
__int__          int
__float__        float
__round__        round
__index__        operator.index()
================ ================

Comparisons

====== ========
Method Operator
====== ========
__lt__ <
__le__ <=
__eq__ ==
__ne__ !=
__gt__ >
__ge__ >=
====== ========

To automatically generate ordering operations from a single root operation,
see `functools.total_ordering() <https://docs.python.org/3.4/library/functools.html#functools.total_ordering>`_.

String related

========== ========
Method     Operator
========== ========
__str__    str
__repr__   repr
__bytes__  bytes
__format__ format
========== ========

Emulating callable objects

======== ========
Method   Operator
======== ========
__call__ ()
======== ========

::

  >>> class Foo:
  ...   def __call__(self):
  ...     print("Callable")
  ...
  >>> foo = Foo()
  >>> foo()
  Callable

Emulating container types

============== ======================
Method         Operator
============== ======================
__len__        len
__length_hit__ operator.length_hint()
__getitem__    v = obj[key]
__setitem__    obj[key] = v
__delitem__    del obj[key]
__iter__       for _ in obj, Iteration
__reversed__   reversed()
__contains__   key in obj
============== ======================

With statment context manager

========= ========
Method    Operator
========= ========
__enter__ with
__exit__  with
========= ========

::

  class cd:

      def __init__(self, path):
          self.path = path
          self.old = os.getcwd()

      def __enter__(self):
          os.chdir(self.path)

      def __exit__(self, exc_type, exc_value, traceback):
          os.chdir(self.old)

    with cd('/some/path'):
        ...
    # cd back to old path even exception occurs


See `PEP 0343 <http://www.python.org/dev/peps/pep-0343>`_ - The "with" statement


Instance and subclass checks

================= ==========
Method            Operator
================= ==========
__instancecheck__ isinstance
__subclasscheck__ issubclass
================= ==========

See `PEP 3119 <PEP 3119 - Introducing Abstract Base Classes>`_ - Introducing Abstract Base Classes


Misc.

======== ======== ==================================================================================
Method   Operator Comments
======== ======== ==================================================================================
__hash__ hash     members of hashable collections including set, forzenset, dict.
__bool__ bool     if a class defines neither __bool__ and __len__, all its instances considered true
======== ======== ==================================================================================

Customize attribute access
--------------------------

__getattr__
__getattribute__
__setattr__
__delattr__
__dir__
__get__
__set__
__delete__
__slots__


::

  class Proxy:

    def __init__(self, wrapped):
      self.__dict__['_wrapped'] = wrapped

    def __getattr__(self, name):
      return getattr(self._wrapped, name)

    def __setattr__(self, name, value):
      setattr(self._wrapped, name, value)

::

  >>> d = {}
  >>> p = Proxy(d)
  >>> p['a'] = 1
  >>> p.b = 2
  >>> p.keys()
  dict_keys(['a'])
  >>> p.__dict__
  {'b': 2, '_wrapped': {'a': 1}}

Comparison between __getattr__ and __getattribute__

- Both methods should return the (computed) attribute value or raise an AttributeError exception
- __getattr__ is called when an attribute lookup has not found; however __getattribute__ is called
  unconditionally.
- If AttributeError was raised in __getattribute__ then __getattr__ will be called.
- In order to avoid infinite recursion in __getattribute__, its implementation should always call
  object.__getattribute__(self, name) to get attributes it needs.
- Similarly, always call object.__setattr__(self, name, value) in __setattr__.

Descriptor

See `Descriptor HowTo Guide <https://docs.python.org/3.4/howto/descriptor.html#descriptor-howto-guide>`_

Slots

See `Saving 9GB of ram with Python's __slots__ <http://tech.oyster.com/save-ram-with-python-slots/>`_


Customize class creation
------------------------

__new__
__init__
__del__
__prepare__
__class__

See `PEP 3115 <http://www.python.org/dev/peps/pep-3115>`_ - Metaclasses in Python 3000
  Introduced the __prepare__ namespace hook
See `PEP 3135 <http://www.python.org/dev/peps/pep-3135>`_ - New super
  Describes the implicit __class__ closure reference


See `Special method names <https://docs.python.org/3.4/reference/datamodel.html#special-method-names>`_ for the full list of special method names
