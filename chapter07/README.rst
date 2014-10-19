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


Full list of numeric types


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


See `Special method names <https://docs.python.org/3.4/reference/datamodel.html#special-method-names>`_
