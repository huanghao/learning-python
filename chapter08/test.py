import sys

class MyException(Exception):
    def pretty_print(self):
        print 'asdfasdf'

def divmod(a, b):
    return a / b, a % b

a, b = map(int, sys.argv[1:])

def func1():
    try:
        func2()
    except ArithmeticError:
        print 'ignore'

def func2():
    func3()
    print 'after func3'

def func3():
    print divmod(a, b)


func1()
print 'after func1'
