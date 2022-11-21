import ply.yacc as yacc
from lexer import tokens
from Utils.AST import *

trad_op = {
    '+' : 'Plus',
    '*' : 'Mult',
    '-' : 'Minus',
    '\\/' : 'Or',
    '/\\' : 'And',
    '<=' : 'Leq',
    '<' : 'Less',
    '>=' : 'Geq',
    '>' : 'Greater',
    '==' : 'Equal',
    '!=' : 'Not Equal',
    '!' : 'Not',
    'in' : 'In'
}

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

def p_type_varible_declare(p):
    '''
    TYPE : TkInt 
         | TkBool 
         | ARRAY_DECLARATION
    '''
    p[0] = p[1]
    
def p_array_declaration(p):
    '''
    ARRAY_DECLARATION : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket
    '''
    p[0] = f"array[Literal: {p[3]}..Literal: {p[5]}]"

################### BLOQUE DE INSTRUCCIONES #######################
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
                | DO_LOOP
    '''
    p[0] =  p[1]
                # | FOR_LOOP
                # | CONDITIONAL

# Produccion para detectar asignaciones
def p_asig(p):
    '''
    ASIG : TkId TkAsig E
    '''
    p[0] = Nodo('Asig', Nodo(f"Ident: {p[1]}"), p[3])

# TODO: detectar parentesis
def p_expression_op_binary(p):
    '''
    E : E TkMult E
      | E TkPlus E
      | E TkMinus E
      | E TkOr E
      | E TkAnd E
      | E TkLess E
      | E TkLeq E
      | E TkGeq E
      | E TkGreater E
      | E TkEqual E
      | E TkNEqual E
    '''
    p[0] = Nodo(trad_op.get(p[2]), p[1], p[3])

def p_expression_op_unary(p):
    '''
    E : TkNot E
      | TkMinus E
    '''
    p[0] = Nodo(trad_op.get(p[1]), p[2])

def p_expression_base(p):
    '''
    E : TkNum
      | TkId
      | TkTrue
      | TkFalse
    '''
    if isinstance(p[1], int) or p[1] == 'true' or p[1] == 'false':
        p[0] = Nodo(f"Literal: {p[1]}")
    
    else:
        p[0] = Nodo(f"Ident: {p[1]}")
        

# Produccion para detectar un print en una secuenciacion
def p_print(p):
    '''
    PRINT : TkPrint TOPRINT  
    '''
    p[0] = Nodo("Print" ,p[2])

def p_to_print_base(p):
    '''
    TOPRINT : EXPRESSION_TO_PRINT   
    '''
    p[0] = p[1]
    
def p_to_print(p):
    '''
    TOPRINT : TOPRINT TkConcat EXPRESSION_TO_PRINT   
    '''
    p[0] = Nodo('Concat', p[1], p[3])

def p_expression_print(p):
    '''
    EXPRESSION_TO_PRINT : TkId
               | TkString
               | TkNum
               | TkTrue
               | TkFalse
               | READ_ARRAY
    '''
    if isinstance(p[1], Nodo):
        p[0] = p[1]
    else:
        p[0] = Nodo(str(p[1]))

def p_array_index(p):
    '''
    READ_ARRAY : TkId TkOBracket E TkCBracket
    '''
    p[0] = Nodo("ReadArray", Nodo(f"Ident: {p[1]}"), p[3])

# Produccion para detectar un do-loop
def p_do_loop(p):
    '''
    DO_LOOP : TkDo E TkArrow LIST_INSTRUCTIONS TkOd
    '''
    p[0] = Nodo("Do", Nodo("Then", p[2], p[4]))

# Produccion para detectar un for-loop
def p_for_loop(p):
    '''
    DO_LOOP : TkFor TkId TkIn E TkTo E TkArrow LIST_INSTRUCTIONS TkRof
    '''
    p[0] = Nodo('For', Nodo('In', Nodo(f"Ident: {p[2]}"), Nodo('To', p[4], p[6])), p[8])

parser = yacc.yacc()

data = '''
|[ 
    declare
        h : int;
        g, h, k : int;
        f : array[2..4];
        y, x: bool

    do i < 10 --> 
        print "Still here!";
        i := i + 1
    od;

    a := 4;

    for j in 2 to 5 -->
        print i
    rof

]|
'''

ast = parser.parse(data)
# print(ast)

print_arbol(ast)

# print(result)

