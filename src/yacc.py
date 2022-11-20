import ply.yacc as yacc
from lexer import tokens
from Utils.AST import *

# precedence = (
#     ('rigth', 'TkAsig')
# )

def p_error(p):
    print("error")
    print(p)

def p_program(p):
    '''
    B : TkOBlock DECLARE INSTRUCTIONS TkCBlock
    '''
    p[0] = Nodo("Block", p[2], p[3])
    print(f'******** Todo bien **********')

def p_declare(p):
    '''
    DECLARE : TkDeclare LIST_DECLARE
    '''
    p[0] = Nodo("Declare", p[2])

def p_list_declare_base(p):
    '''
    LIST_DECLARE : VARIABLE_DECLARATION
    '''
    p[0] = p[1]

def p_list_declare(p):
    '''
    LIST_DECLARE : LIST_DECLARE TkSemicolon VARIABLE_DECLARATION
    '''
    p[0] = Nodo('Sequencing', p[1], p[3])

                
def p_list_variables_declare_base(p):
    '''
    VARIABLE_DECLARATION : TkId TkTwoPoints TYPE
    '''
    p[0] = Nodo(f"{p[1]} {p[2]} {p[3]}")

def p_list_variables_declare(p):
    '''
    VARIABLE_DECLARATION : TkId TkComma VARIABLE_DECLARATION
    '''
    p[0] = Nodo(f"{p[1]}{p[2]} " + f"{p[3]}")

def p_type_varible_declare(p):
    '''
    TYPE : TkInt 
         | TkBool 
         | TkArray
    '''
    p[0] = p[1]
    

def p_statements(p):
    '''
    INSTRUCTIONS : INSTRUCTION TkSemicolon INSTRUCTIONS
                  | INSTRUCTION
    '''
    p[0] = Nodo("Hola")

def p_statement(p):
    '''
    INSTRUCTION : TkFor
                | TkIf
                | TkDo
                | TkPrint
                | TkId
    '''

parser = yacc.yacc('SLR')

data = '''
|[ 
    declare
        h : int;
        g, h, k : array;
        f : int;
        y, x: bool

    print;
    do;
    for;
    if;
    estoEsUnId
]|
'''

ast = parser.parse(data)
# print(ast)

printArbol(ast)

# print(result)

