"""
This is a naive re grammar parser implemented via ply
"""
from __future__ import print_function
from ast import literal_eval

from ply import lex, yacc


tokens = ('ALPHA', 'ESC')

t_ALPHA = r'[a-zA-Z0-9]'
literals = ['.', '*', '|', '(', ')'] # + ? {n, m}


def t_ESC(t):
    val = t.value[1]
    if val in ('t', 'n', 'r'):
        val = literal_eval('\\' + val)
    t.value = val
    return t

t_ESC.__doc__ = r'\\(%s)' % '|'.join([ ('\\'+i) for i in (literals+['\\']) ])


def p_exp(p):
    '''
    exp : concatenation '|' concatenation
        | concatenation
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        start, end = new()
        link(
            (start, EMPTY, p[1][0]),
            (start, EMPTY, p[3][0]),
            (p[1][1], EMPTY, end),
            (p[3][1], EMPTY, end),
            )
        p[0] = (start, end)

def p_concatenation(p):
    '''
    concatenation : concatenation group
        | group
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        link(p[1][1], EMPTY, p[2][0])
        p[0] = (p[1][0], p[2][1])


def p_group(p):
    '''
    group : star
        | term
    '''
    p[0] = p[1]


def p_star(p):
    '''
    star : term '*'
    '''
    start, end = new()
    link(
        (start, EMPTY, end),
        (start, EMPTY, p[1][0]),
        (p[1][1], EMPTY, end),
        (end, EMPTY, start),
        )
    p[0] = (start, end)


def p_term(p):
    '''
    term : ALPHA
        | ESC
        | '.'
        | '(' exp ')'
    '''
    if len(p) == 2:
        start, end = new()
        if p[1] == '.':
            link(start, ANY, end)
        else:
            link(start, p[1], end)
        p[0] = (start, end)
    else:
        p[0] = p[2]


EMPTY = 'e'
ANY = '.'
INC = 0


def new():
    global INC
    ret = (INC, INC+1)
    INC += 2
    return ret


TT = []
def link(*args):
    global TT
    if type(args[0]) == int:
        TT.append(args)
    else:
        TT.extend(args)


def match(start, end, tt, string):
    def e_closure1(st):
        ret = set([st])
        while True:
            n1 = len(ret)
            ret |= set([ e for s, t, e in tt if s in ret and t == EMPTY ])
            if len(ret) == n1:
                break
        return ret

    def e_closure2(st, term):
        ret = set()
        for i in st:
            for s, t, e in tt:
                if s == i and t == term:
                    ret |= e_closure1(e)
        return ret

    st = e_closure1(start)
    for term in string:
        st = e_closure2(st, term)
    return end in st


def lexer():
    lexer = lex.lex()
    lexer.input(r'ab*')
    for tok in lexer:
        print(tok)



def grammar():
    pattern = r'a|(bc)*'
    string = 'bcbc'
    start, end = yacc.yacc().parse(pattern)
    print("string %s matches pattern %s ? %s" % (
        string, pattern, match(start, end, TT, string)))
    #dot(start, end, TT)


def dot(start, end, tt):
    print('digraph {')
    for s, t, e in tt:
        print('  %d -> %d[label="%s"];' % (s, e, t))
    print('}')


if __name__ == '__main__':
    lexer()
    grammar()

