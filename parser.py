import ply.yacc as yacc
from lexer import tokens

# Operator precedence for reducing conflicts
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("nonassoc", "GT", "LT", "GE", "LE", "EQ", "NEQ"),
)


def p_program(p):
    """program : statement_list 
                | function_def"""
    pass

# Function definition
def p_function_def(p):
    """function_def : FN NAME LPAREN param_list RPAREN ret_type block"""
    print("Valid function definition")


def p_param_list(p):
    """param_list : param_list COMMA param
    | param
    | empty"""
    pass


def p_param(p):
    """param : NAME COLON TYPE"""
    pass


def p_ret_type(p):
    """ret_type : ARROW TYPE
    | empty"""
    pass


def p_block(p):
    """block : LBRACE statement_list RBRACE"""
    pass


def p_statement_list(p):
    """statement_list : statement_list statement
    | statement
    | empty"""
    pass


# If-Else statement 
def p_if_else(p):
    """statement : IF expression block else_part"""
    print("Valid if-else statement")

def p_else_part(p):
    """else_part : ELSE block
    | empty"""
    pass


# For loop
def p_for_loop(p):
    """statement : FOR NAME IN range block"""
    print("Valid for loop")


def p_range(p):
    """range : NUMBER DOTDOT NUMBER"""
    pass


# Local Variable Declaration 
def p_statement_declaration(p):
    """statement : LET opt_mut NAME COLON TYPE ASSIGN expression SEMI"""
    print("Valid variable declaration")

def p_opt_mut(p):
    """opt_mut : MUT
               | empty"""
    pass

# Expressions
def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression GT expression
    | expression LT expression
    | expression GE expression
    | expression LE expression
    | expression EQ expression
    | expression NEQ expression"""
    pass


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    pass


def p_expression_number(p):
    """expression : NUMBER"""
    pass


def p_expression_name(p):
    """expression : NAME"""
    pass

# Function Call 
def p_expression_function_call(p):
    """expression : NAME LPAREN arg_list RPAREN"""
    print("Valid function call expression")

def p_arg_list(p):
    """arg_list : arg_list COMMA expression
                | expression
                | empty"""
    pass


def p_statement_expr(p):
    """statement : expression SEMI"""
    pass

def p_statement_return(p):
    '''statement : RETURN expression SEMI'''
    pass

def p_empty(p):
    "empty :"
    pass


parse_errors = []

#error rule
def p_error(p):
    if p:
        msg = f"Syntax error at '{p.value}'"
    else:
        msg = "Syntax error at EOF"
    parse_errors.append(msg)
    print(msg)


parser = yacc.yacc(start='program')