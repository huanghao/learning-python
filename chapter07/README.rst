Classes and OOP
===============

Everything in python are objects, even classes and codes.

Object identity

Every object has an identify, a type and a value. An object's identify never changes once it
has been created. You may think of it as the object's address in memory. The *is* operator
compares the identity of two objects. The *id()* functions returns an integer representing
its identity.

CPython implementation detail: For CPython, id(x) is the memory address where x is stored.

An object's type determines the operators that the object supports and also defines the possible
values for objects of that type. The *type()* function returns an object's type (which is an
object itself).

The value of some objects can change. Objects whose value can change are said to be mutable;
objects whose value is unchangeable once they are created are called immutable.

Objects are never explicitly destroyed; however, when they become unreachable they may be
garbage-collected.


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

Properties::

  class Person:
    def __init__(self, name):
      self._name = name

    def getName(self):
      print('fetch...')
      return self._name

    def setName(self, value):
      print('change...')
      self._name = value

    def delName(self):
      print('remove...')
      del self._name

    name = property(getName, setName, delName, "name property docs")

  bob = Person('Bob Smith')
  print(bob.name)             # getName
  bob.name = 'Robert Smith'   # setName
  print(bob.name)

Class decorator
  Similar as function decorator. It's a callable object which accepts a class and return a class.


Special attributes
------------------

object.__dict__
  A dictionary or other mapping object used to store an object’s (writable) attributes.

instance.__class__
  The class to which a class instance belongs.

class.__bases__
  The tuple of base classes of a class object.

class.__name__
  The name of the class or type.

class.__qualname__
  The qualified name of the class or type.

  New in version 3.3.

  See `PEP 3155 <http://legacy.python.org/dev/peps/pep-3155/>`_ - Qualified name for classes and functions

class.__mro__
  This attribute is a tuple of classes that are considered when looking for base classes during method resolution.

class.mro()
  This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called at class instantiation, and its result is stored in __mro__.

class.__subclasses__()
  Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. Example::

    >>> int.__subclasses__()
    [<class 'bool'>]

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

See `PEP 3119 <http://www.python.org/dev/peps/pep-3119>`_ - Introducing Abstract Base Classes


Misc.

======== ======== ==================================================================================
Method   Operator Comments
======== ======== ==================================================================================
__hash__ hash     members of hashable collections including set, forzenset, dict.
__bool__ bool     if a class defines neither __bool__ and __len__, all its instances considered true
======== ======== ==================================================================================

Customize attribute access
--------------------------

================ ==========================
Method           Operator
================ ==========================
__getattr__      o.attr, getattr(o, 'attr')
__getattribute__ o.attr, getattr(o, 'attr')
__setattr__      o.attr = val
__delattr__      del o.attr
__dir__          dir()
================ ==========================

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

- __get__
- __set__
- __delete__

See `Descriptor HowTo Guide <https://docs.python.org/3.4/howto/descriptor.html#descriptor-howto-guide>`_

Slots

__slots__

See `Saving 9GB of ram with Python's __slots__ <http://tech.oyster.com/save-ram-with-python-slots/>`_


Customize class creation
------------------------

=========== ===================
Method      Operator
=========== ===================
__new__     C() before __init__
__init__    C()
__del__     del o (gc)
__prepare__
=========== ===================

__new__
  Called to create a new instance of class cls.

- If __new__() returns an instance of cls, then the new instance's __init__() method will be invoked like __init__(self, ...), where self is the new instance and the remaining arguments are the same as were passed to __new__().
- If __new__() does not return an instance of cls, then the new instance's __init__() method will not be invoked.

__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It's also commonly overridden in custom metaclasses in order to customize class creation.

::

  class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.PasswordField()

  form = LoginForm(request.POST)    # {'username': 'abcd', 'password': 'abcd'}
  if not form.is_valid()
    return HttpResponse(form.error_as_string())

::

  class Form(six.with_metaclass(DeclarativeFieldsMetaclass, BaseForm)):
    ...

  class DeclarativeFieldsMetaclass:

    def __new__(mcs, name, bases, attrs):
      current_fields = []
        for key, value in list(attrs.items()):
          if isinstance(value, Field):
            current_fields.append((key, value))
            attrs.pop(key)
            attrs['declared_fields'] = OrderedDict(current_fields)
      ...
      new_class = (super(DeclarativeFieldsMetaclass, mcs)
        .__new__(mcs, name, bases, attrs))
      ...

      new_class.base_fields = declared_fields
      new_class.declared_fields = declared_fields

      return new_class

  class BaseForm(object):
    def __init__(self, ...):
      ...
      self.fields = copy.deepcopy(self.base_fields)

    def __getitem__(self, name):
      "Returns a BoundField with the given name."
      try:
        field = self.fields[name]
      except KeyError:
        raise KeyError(
          "Key %r not found in '%s'" % (name, self.__class__.__name__))
      return BoundField(self, field, name)

By default, classes are construted using `type(name, bases, dict) <https://docs.python.org/3.4/library/functions.html#type>`_.
In the following exmaple, both MyClass and MySubclass are instances of Meta::

  class Meta(type):
    pass

  class MyClass(metaclass=Meta):
    pass

  class MySubclass(MyClass):
    pass

When a class definition is executed, the following steps occur:

1. the appropriate metaclass is determined
2. the class namespace is prepared
3. the class body is executed
4. the class object is created

Determining the appropriate metaclass

- if no bases and no explicit metaclass are given, then type() is used
- if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass
- if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used

Preparing the class namespace

- namespace = metaclass.__prepare__(name, bases, \*\*kwds)
- otherwise, an empty dict() instance

kwds come from the class definition.

Executing the class body

  exec(body, globals(), namespace)

Creating the class object

Once the class namespace has been populated by executing the class body, the class object is created by calling

  metaclass(name, bases, namespace, \*\*kwds)

After the class object is created, it is passed to the class decorators included in the class definition (if any)
and the resulting object is bound in the local namespace as the defined class.

::

  class OrderedClass(type):

       @classmethod
       def __prepare__(metacls, name, bases, **kwds):
          return collections.OrderedDict()

       def __new__(cls, name, bases, namespace, **kwds):
          result = type.__new__(cls, name, bases, dict(namespace))
          result.members = tuple(namespace)
          return result

  class A(metaclass=OrderedClass):
      def one(self): pass
      def two(self): pass
      def three(self): pass
      def four(self): pass

::

  >>> A.members
  ('__module__', 'one', 'two', 'three', 'four')

See `PEP 3115 <http://www.python.org/dev/peps/pep-3115>`_ - Metaclasses in Python 3000
  Introduced the __prepare__ namespace hook
See `PEP 3135 <http://www.python.org/dev/peps/pep-3135>`_ - New super
  Describes the implicit __class__ closure reference


See `Special method names <https://docs.python.org/3.4/reference/datamodel.html#special-method-names>`_ for the full list of special method names


Advanced topics
---------------

The "New style" class model
  From 2.2, python introduced a new flavor of classes, known as new-style classes. classes following the original and traditional model became known as classic classes. In 3.x only the new style remained.

For 2.x, classes must explicitly inherit from object to be considered "new style", otherwise they are "classic"::

  class Foo:          # classic
    pass

  class Bar(object):  # new style
    pass

See `Old and New classes <https://docs.python.org/3/whatsnew/2.2.html#old-and-new-classes>`_

MRO and super #TODO
