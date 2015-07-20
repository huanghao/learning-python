import os

"""
os.listdir(path) -> list of names
os.path.isdir(path) -> ture or false
str.endswith('.py') -> true or false
os.path.join(path1, path2) -> path1/path2
"""

def find_files(topdir, ext):
    for name in os.listdir(topdir):
        name = os.path.join(topdir, name)
        if os.path.isdir(name):
            find_files(name, ext)
        else:
            if name.endswith(ext):
                print name

find_files('/Users/huanghao/workspace/kepl', '.py')
