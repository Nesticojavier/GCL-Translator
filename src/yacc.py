import ply.yacc as yacc
from lexer import tokens
from Utils.AST import *
import sys
import codecs

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

precedence = (
    ('left', 'TkOr'),
    ('left', 'TkAnd'),
    ('right', 'TkNot'),
    ('left', 'TkEqual', 'TkNEqual'),
    ('left','TkLess', 'TkLeq', 'TkGeq', 'TkGreater'), 
    ('left', 'TkPlus', 'TkMinus'),
    ('right', 'TkMult'),
    ('right', 'UNARY')
)

def p_error(p):
    print("error")
    print(p)

def p_program(p):
    '''
    BLOCK : TkOBlock DECLARE LIST_INSTRUCTIONS TkCBlock
    '''
    p[0] = Nodo("Block", p[2], p[3])
    # p[0] = Nodo("Block", p[3])
    # p[0] = Nodo("Block", p[2])
    print(f'******** Todo bien **********')

def p_subprogram(p):
    '''
    SUBPROGRAM : BLOCK
               | LIST_INSTRUCTIONS
    '''
    p[0] = p[1]

def p_declare(p):
    '''
    DECLARE : TkDeclare LIST_DECLARE
            | 
    '''
    if len(p) == 1:
        p[0] = None
    else:
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
                | FOR_LOOP
                | DO_LOOP
                | CONDITIONAL
                | TkSkip
    '''
    if p[1] != 'skip':
        p[0] =  p[1]
    else:
        p[0] = Nodo('skip')

# Produccion para detectar asignaciones
def p_asig(p):
    '''
    ASIG : TkId TkAsig EXPRESSION
    '''
    p[0] = Nodo('Asig', Nodo(f"Ident: {p[1]}"), p[3])

def p_asig_expresion(p):
    '''
    EXPRESSION : E
               | ASIG_ARRAY
    '''
    p[0] = p[1]

def p_asig_array(p):
    '''
    ASIG_ARRAY : CREATE_ARRAY
               | WRITE_ARRAY
    '''
    p[0] = p[1]

def p_create_array(p):
    '''
    CREATE_ARRAY : E TkComma E
    '''
    p[0] = Nodo('Comma', p[1], p[3])

def p_create_array_base(p):
    '''
    CREATE_ARRAY : CREATE_ARRAY TkComma E
    '''
    p[0] = Nodo('Comma', p[1], p[3])

def p_write_array_base(p):
    '''
    WRITE_ARRAY : TkId TkOpenPar E TkTwoPoints E TkClosePar
    '''
    p[0] = Nodo('WriteArray',Nodo(f"Ident: {p[1]}") , Nodo('TwoPoints', p[3], p[5]))
    # p[0] = Nodo("Holas")

def p_write_array(p):
    '''
    WRITE_ARRAY : WRITE_ARRAY TkOpenPar E TkTwoPoints E TkClosePar
    '''
    p[0] = Nodo('WriteArray', p[1], Nodo("TwoPoints", p[3], p[5]))
    # p[0] = Nodo("hola")

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

def p_expression_par(p):
    '''
    E : TkOpenPar E TkClosePar
    '''
    p[0] = p[2]

def p_expression_op_unary(p):
    '''
    E : TkNot E %prec UNARY
      | TkMinus E %prec UNARY
    '''
    p[0] = Nodo(trad_op.get(p[1]), p[2])

# def p_unary_minus(p):
#     '''
#     UMINUS : TkMinus
#     '''
#     p[0] = p[1]

def p_expression_base(p):
    '''
    E : TkNum
      | TkId
      | TkTrue
      | TkFalse
      | READ_ARRAY
    '''
    if isinstance(p[1], int) or p[1] == 'true' or p[1] == 'false':
        p[0] = Nodo(f"Literal: {p[1]}")
    
    elif isinstance(p[1], Nodo):
        p[0] = p[1]
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

    elif isinstance(p[1], int) or p[1] == 'true' or p[1] == 'false':
        p[0] = Nodo(f"Literal: {p[1]}")

    else:
        p[0] = Nodo(f"String: {p[1]}")

def p_array_index(p):
    '''
    READ_ARRAY : ARRAY TkOBracket E TkCBracket
    '''
    p[0] = Nodo("ReadArray", p[1], p[3])

def p_array_index_id_or_read(p):
    '''
    ARRAY : TkId
          | WRITE_ARRAY
    '''
    if isinstance(p[1], Nodo):
        p[0] = p[1]
    else:
        p[0] = Nodo(f"Ident: {p[1]}")

# Produccion para detectar un for-loop
def p_for_loop(p):
    '''
    FOR_LOOP : TkFor TkId TkIn E TkTo E TkArrow SUBPROGRAM TkRof
    '''
    p[0] = Nodo('For', Nodo('In', Nodo(f"Ident: {p[2]}"), Nodo('To', p[4], p[6])), p[8])

# Produccion para detectar un do-loop TODO: multiples guardias
def p_do_loop(p):
    '''
    DO_LOOP : TkDo GUARD TkOd
    '''
    p[0] = Nodo('Do', p[2])

# Produccion para detectar If/Guard
def p_if_conditional(p):
    '''
    CONDITIONAL : TkIf GUARD TkFi
    '''
    p[0] = Nodo('If', p[2])

def p_guard_base(p):
    '''
    GUARD : E TkArrow LIST_INSTRUCTIONS
    '''
    p[0] = Nodo('Then', p[1], p[3])

def p_guard(p):
    '''
    GUARD : GUARD TkGuard E TkArrow LIST_INSTRUCTIONS
    '''
    p[0] = Nodo("Guard", p[1], Nodo('Then', p[3], p[5])) 
    
archivo = sys.argv[1]
# abrir archivo
handleFile = codecs.open(archivo)
data = handleFile.read()


parser = yacc.yacc()
ast = parser.parse(data)

print_arbol(ast)







################### TEST ######################
arch = sys.argv[2]
f = open(f"../CasosDePrueba/MyOuts/{arch}", "w")

def write_arbol(nodo: Nodo, guion = ""):
    f.write(guion + str(nodo))
    f.write("\n")

    if nodo.leftChild :  
        write_arbol(nodo.leftChild, guion + "-")
        
    
    if nodo.rigthChild:  
        write_arbol(nodo.rigthChild, guion + "-")

write_arbol(ast)

# f.truncate(f.tell()-1)

f.close()
