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
    BLOCK : TkOBlock DECLARE LIST_INSTRUCTIONS TkCBlock
    '''
    # p[0] = Nodo("Block", p[2], p[3])
    p[0] = Nodo("Block", p[3])
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

# TODO: falta completar array completo y no solo array
def p_type_varible_declare(p):
    '''
    TYPE : TkInt 
         | TkBool 
         | TkArray
    '''
    p[0] = p[1]
    
################### INSTRUCCIONES #######################
def p_intruccions_list_base(p):
    '''
    LIST_INSTRUCTIONS : INSTRUCTION
    '''
    p[0] = p[1]

def p_intruccions_list(p):
    '''
    LIST_INSTRUCTIONS : LIST_INSTRUCTIONS TkSemicolon INSTRUCTION
    '''
    p[0] = Nodo('Sequencing', p[1], p[3])

def p_instruccion(p):
    '''
    INSTRUCTION : ASIG
    '''
    p[0] =  p[1]
                # | FOR_LOOP
                # | DO_LOOP
                # | CONDITIONAL
                # | PRINT

def p_asig(p):
    '''
    ASIG : TkId TkAsig E
    '''
    p[0] = Nodo('Asig', Nodo(p[1]), p[3])

# TODO: falata hacer que detecte una expresion compleja y no solo un numero
def p_expression(p):
    '''
    E : TkNum
    '''
    p[0] = Nodo(f"Literal: {p[1]}")

# def p_instruccion(p):
#     '''
#     INSTRUCTION : TkId
#                 | TkFor
#                 | TkDo
#                 | TkIf
#                 | TkPrint
#     '''
    # p[0] =  Nodo(p[1])
    # print(f"############### {p[1]}  #############")

parser = yacc.yacc('SLR')

data = '''
|[ 
    declare
        h : int;
        g, h, k : array;
        f : int;
        y, x: bool

    a := 1;
    b := 3;
    c := 4;
    d := 5;
    x := 5;
    y := 5;
    z := 5;
    w := 5;
    p := 5
]|
'''

ast = parser.parse(data)
# print(ast)

print_arbol(ast)

# print(result)

