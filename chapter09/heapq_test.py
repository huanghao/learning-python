from random import random

from timing import timing

data = [random() for _ in range(10**7)]

initial = '''
from heapq import nsmallest
from __main__ import data
'''

setup = '''
nums = data[:]
'''

top10_by_sort = '''
nums.sort()
print nums[:10]
'''

top10_by_heapq = '''
print nsmallest(10, nums)
'''

if __name__ == '__main__':
    timing(initial, setup, top10_by_sort, times=1)
    timing(initial, setup, top10_by_heapq, times=1)
