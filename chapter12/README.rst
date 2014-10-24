Auto-Testing
============

`doctest <https://docs.python.org/3.4/library/doctest.html>`_
-------------------------------------------------------------

::

  """
  This is the "example" module.

  The example module supplies one function, factorial().  For example,

  >>> factorial(5)
  120
  """

  def factorial(n):
      """Return the factorial of n, an exact integer >= 0.

      >>> [factorial(n) for n in range(6)]
      [1, 1, 2, 6, 24, 120]
      >>> factorial(30)
      265252859812191058636308480000000
      >>> factorial(-1)
      Traceback (most recent call last):
          ...
      ValueError: n must be >= 0

      Factorials of floats are OK, but the float must be an exact integer:
      >>> factorial(30.1)
      Traceback (most recent call last):
          ...
      ValueError: n must be exact integer
      >>> factorial(30.0)
      265252859812191058636308480000000

      It must also not be ridiculously large:
      >>> factorial(1e100)
      Traceback (most recent call last):
          ...
      OverflowError: n too large
      """

      import math
      if not n >= 0:
          raise ValueError("n must be >= 0")
      if math.floor(n) != n:
          raise ValueError("n must be exact integer")
      if n+1 == n:  # catch a value like 1e300
          raise OverflowError("n too large")
      result = 1
      factor = 2
      while factor <= n:
          result *= factor
          factor += 1
      return result


  if __name__ == "__main__":
      import doctest
      doctest.testmod()

::

  $ python example.py -v

  # or

  $ python -m doctest example.py


`unittest <https://docs.python.org/3.4/library/unittest.html>`_
---------------------------------------------------------------

Important concepts:

test fixture
  A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case
  A test case is the individual unit of testing.

test suite
  A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runner
  A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

Example::

  import random
  import unittest

  class TestSequenceFunctions(unittest.TestCase):

      def setUp(self):
          self.seq = list(range(10))

      def test_shuffle(self):
          # make sure the shuffled sequence does not lose any elements
          random.shuffle(self.seq)
          self.seq.sort()
          self.assertEqual(self.seq, list(range(10)))

          # should raise an exception for an immutable sequence
          self.assertRaises(TypeError, random.shuffle, (1,2,3))

      def test_choice(self):
          element = random.choice(self.seq)
          self.assertTrue(element in self.seq)

      def test_sample(self):
          with self.assertRaises(ValueError):
              random.sample(self.seq, 20)
          for element in random.sample(self.seq, 5):
              self.assertTrue(element in self.seq)

  if __name__ == '__main__':
      unittest.main()

::

  $ python example.py
  ...
  ----------------------------------------------------------------------
  Ran 3 tests in 0.000s

  OK

  $ python -v example.py
  test_choice (__main__.TestSequenceFunctions) ... ok
  test_sample (__main__.TestSequenceFunctions) ... ok
  test_shuffle (__main__.TestSequenceFunctions) ... ok

  ----------------------------------------------------------------------
  Ran 3 tests in 0.110s

  OK


Mocking
~~~~~~~

pytest
------

See also: Nose

Tox
---

Selenium
--------

WebDriver
~~~~~~~~~

PhantomJS
~~~~~~~~~

Coverage
--------

python-coverage

coversall.io
~~~~~~~~~~~~
