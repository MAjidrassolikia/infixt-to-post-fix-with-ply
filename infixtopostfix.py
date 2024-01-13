import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Invalid character {t.value[0]}")
    t.lexer.skip(1)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = [p[1]]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = p[1] + p[3] + [p[2]]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = [-p[2]]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input('Enter infix expression: ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    postfix = ' '.join([str(i) for i in result])
    print(f"Postfix expression: {postfix}")