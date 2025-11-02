import ply.lex as lex

reserved = {
    'fn': 'FN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'return': 'RETURN',
    'let': 'LET',
    'mut': 'MUT',
}

tokens = [
    'NAME', 'NUMBER', 'TYPE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COLON', 'COMMA', 'ARROW', 'SEMI', 'DOTDOT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NEQ',
    'ASSIGN'
] + list(reserved.values())

t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NEQ = r'!='


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_ARROW = r'->'
t_SEMI = r';'
t_DOTDOT = r'\.\.'

t_ignore = ' \t'

def t_TYPE(t):
    r'i32|f64|bool|char|String'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()