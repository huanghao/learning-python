import time

def timing(initial, setup, testing, times=3, verbose=False):
    print('Testing the following code for {} times ...\n{}'.format(times, testing.strip()))
    namespace = {}
    exec(initial, namespace)

    av = 0
    for i in range(times):
        exec(setup, namespace)

        begin = time.time()
        exec(testing, namespace)
        cost = time.time() - begin

        if verbose:
            print('{}: {}'.format(i + 1, cost))
        av += cost
    print('av: {}\n'.format(av / times))


initial = '''
from collections import deque
data = list(range(10**5))
'''

list_add_setup = 'l = []'
deque_add_setup = 'd = deque()'

list_add_in_the_head = '''
for i in data:
  l.insert(0, i)        # O(N)
'''

list_add_in_the_tail = '''
for i in data:
  l.append(i)           # O(1)
'''

deque_add_in_the_head = '''
for i in data:
  d.appendleft(i)       # O(1)
'''

deque_add_in_the_tail = '''
for i in data:
  d.append(i)           # O(1)
'''

list_remove_setup = 'l = list(range(10**5))'
deque_remove_setup = 'd = deque(range(10**5))'

list_remove_in_the_head = '''
for _ in data:
  l.pop(0)              # O(n)
'''

list_remove_in_the_tail = '''
for _ in data:
  l.pop()               # O(1)
'''

deque_remove_in_the_head = '''
for _ in data:
  d.popleft()           # O(1)
'''

deque_remove_in_the_tail = '''
for _ in data:
  d.pop()               # O(1)
'''

if __name__ == '__main__':
    timing(initial, list_add_setup, list_add_in_the_head)
    timing(initial, list_add_setup, list_add_in_the_tail)

    timing(initial, deque_add_setup, deque_add_in_the_head)
    timing(initial, deque_add_setup, deque_add_in_the_tail)

    timing(initial, list_remove_setup, list_remove_in_the_head)
    timing(initial, list_remove_setup, list_remove_in_the_tail)

    timing(initial, deque_remove_setup, deque_remove_in_the_head)
    timing(initial, deque_remove_setup, deque_remove_in_the_tail)

