"""
This is a naive lisp evaluator implemented by ply
"""
from __future__ import print_function
import sys

from ply import lex, yacc


tokens = ('INT', 'OP')
literals = ['(', ')']

t_INT = r'\d+'
t_OP = r'\+|-|\*'
t_ignore = " \t\n"

OP = {
    '+': lambda i,j: i+j,
    '-': lambda i,j: i-j,
    '*': lambda i,j: i*j,
}

def p_exp(p):
    '''
    exp : '(' OP exp exp ')'
        | INT
    '''
    if len(p) > 2:
        operator = OP[p[2]]
        p[0] = operator(p[3], p[4])
    else:
        p[0] = int(p[1])


def test():
    in_ = '(* (+ 1 2) (- 3 4))'
    lexer = lex.lex()
    lexer.input(in_)
    for tok in lexer:
        print(tok)

    in_ = '(* (+ 1 2) (- 3 4))'
    val = yacc.yacc().parse(in_)
    print(val)


if __name__ == '__main__':
    test()

