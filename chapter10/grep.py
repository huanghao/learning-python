import os
import re
import sys
import argparse


def parse_args():
    p = argparse.ArgumentParser(
        description='recursively search `pattern` in all files under `path`')
    p.add_argument('pattern')
    p.add_argument('path')
    return p.parse_args()


def search_file(name, pattern):
    with open(name) as file:
        for i, line in enumerate(file.readlines()):
            m = pattern.search(line)
            if m:
                print_matches(name, i+1, line, m)


def colored(msg):
    return ''.join(['\x1b[32m', msg, '\x1b[0m'])


def print_matches(filename, lineno, line, match):
    start, end = match.start(0), match.end(0)
    before, found, after = line[:start], line[start:end], line[end:]
    line = ''.join([before, colored(found), after])
    print('{}:{}:{}'.format(filename, lineno, line), end='')


def is_binary(name):
    CHUNKSIZE = 1024
    with open(name, 'rb') as file:
        while 1:
            chunk = file.read(CHUNKSIZE)
            if b'\0' in chunk:
                return True
            if len(chunk) < CHUNKSIZE:
                break
    return False

def main():
    args = parse_args()

    pattern = re.compile(args.pattern)

    for dirpath, dirnames, filenames in os.walk(args.path):
        for name in filenames:
            name = os.path.join(dirpath, name)
            if not is_binary(name):
                try:
                    search_file(name, pattern)
                except Exception as err:
                    print("Can't read file:{}:{}".format(name, str(err)), file=sys.stderr)


if __name__ == '__main__':
    main()
