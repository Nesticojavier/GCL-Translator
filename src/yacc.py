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
         | TkString
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
                | PRINT
    '''
    p[0] =  p[1]
                # | FOR_LOOP
                # | DO_LOOP
                # | CONDITIONAL

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

# Gramática para detectar un print en una secuenciacion
def p_print(p):
    '''
    PRINT : TkPrint TOPRINT  
    '''
    p[0] = Nodo("Print" ,p[2])

def p_to_print_base(p):
    '''
    TOPRINT : EXPRESSION   
    '''
    p[0] = p[1]
    
def p_to_print(p):
    '''
    TOPRINT : TOPRINT TkConcat EXPRESSION   
    '''
    p[0] = Nodo('Concat', p[1], p[3])

def p_expression_print(p):
    '''
    EXPRESSION : TkId
               | TkString
               | TkNum
               | TkTrue
               | TkFalse
    '''
    print(f"###########  {type(p[1])}   ############")
    p[0] = Nodo(str(p[1]))

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
    print "hola1" . "hola2" . "hola3" . 7
    
]|
'''

ast = parser.parse(data)
# print(ast)

print_arbol(ast)

# print(result)

