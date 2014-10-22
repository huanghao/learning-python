Debugging and Profiling
=======================

Does list comprehension run faster than map ?

::

  $ python -m timeit 'list(map(str, range(10)))'
  100000 loops, best of 3: 3.36 usec per loop

  $ python -m timeit '[str(i) for i in range(10)]'
  100000 loops, best of 3: 4.76 usec per loop

See also: `Python List Comprehension Vs. Map <http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map>`_

Equivalent to::

  def timeit(setup, statements, repeat=3, number=1000000):
    exec(setup)
    for _ in range(repeat):
      start = time.time()
      for _ in range(number):
        exec(statements)
      cost = time.time() - start

Advanced control::

  # -s: setup statement, run once
  # -n: how many times to execute 'statement'
  # -r: how many times to repeat the timer(default 3)
  # multiple statements

  $ python -m timeit -r 5 -n 1000 -s 'data=range(50)' 'l=[]' 'for i in data: l.append(i)'
  1000 loops, best of 5: 6.76 usec per loop

  $ python -m timeit -r 5 -n 1000 -s 'data=range(50)' 'l=[None]*50' 'for i in data: l[i]=i'
  1000 loops, best of 5: 3.71 usec per loop


Profiling

::

  $ python -m cProfile chapter10/grep.py pattern .
  ...
         706259 function calls (673963 primitive calls) in 1.597 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1000(__init__)
  ...
        1    0.000    0.000    1.597    1.597 grep.py:1(<module>)
     3409    0.192    0.000    0.644    0.000 grep.py:15(search_file)
      702    0.001    0.000    0.002    0.000 grep.py:23(colored)
      702    0.005    0.000    0.040    0.000 grep.py:27(print_matches)
     6708    0.147    0.000    0.388    0.000 grep.py:34(is_binary)
        1    0.058    0.058    1.594    1.594 grep.py:45(main)
        1    0.000    0.000    0.003    0.003 grep.py:7(parse_args)
  ...
   397099    0.128    0.000    0.128    0.000 {method 'search' of '_sre.SRE_Pattern' objects}

ncalls
  for the number of calls,

tottime
  for the total time spent in the given function (and excluding time made in calls to sub-functions)

percall
  is the quotient of tottime divided by ncalls

cumtime
  is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.

percall
  is the quotient of cumtime divided by primitive calls


Tracing
-------

::

  $ python -m trace --count grep.py pattern .
  ...
  $ cat grep.cover
    1: import os
    1: import re
  ...
  202:         for i, line in enumerate(file.readlines()):
  199:             m = pattern.search(line)
  199:             if m:
   13:                 print_matches(name, i+1, line, m)
