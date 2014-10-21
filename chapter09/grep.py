"""
Example of argparse to show usage of grep command
"""
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='grep',
        description="The grep utility searches any given input files, selecting "
        "lines that match one or more patterns.  By default, a pattern matches an "
        "input line if the regular expression (RE) in the pattern matches the input "
        "line without its trailing newline.  An empty expression matches every line. "
        "Each input line that matches at least one of the patterns is written to the "
        "standard output.",
        epilog="SEE ALSO ed(1), ex(1), gzip(1), sed(1), re_format(7)")

    parser.add_argument('pattern')
    parser.add_argument('files', nargs='*', type=os.path.abspath)
    parser.add_argument('-n', '--line-numerber', action='store_true',
        help="Each output line is preceded by its relative line number in the file, "
        "starting at line 1.  The line number counter is reset for each file processed. "
        "This option is ignored if -c, -L, -l, or -q is specified.")
    parser.add_argument('-A', '--after-context', type=int,
        help="Print num lines of trailing context after each match. See also the -B "
        "and -C options.")
    return parser.parse_args()


if __name__ == '__main__':
    namespace = parse_args()
    print(namespace)
