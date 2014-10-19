import os
from contextlib import contextmanager

def test1(cd):
    before = os.getcwd()
    with cd('/'):
        inner = os.getcwd()
    after = os.getcwd()
    assert before == after != inner


def test2(cd):
    before = os.getcwd()
    try:
        with cd('/'):
            inner = os.getcwd()
            1/0
    except ZeroDivisionError:
        error = os.getcwd()
    after = os.getcwd()
    assert before == after == error != inner


class cd:

    def __init__(self, path):
        self.path = path
        self.old = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.old)

test1(cd)
test2(cd)


@contextmanager
def cd(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

test1(cd)
test2(cd)
