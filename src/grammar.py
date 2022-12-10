"""Implementacion de un analizador sintactico para el lenguaje GCL

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""

from tokens import tokens
import ply.yacc as yacc
from Utils.utils import *
from Utils.AST import Nodo, NodoExpresiones
import sys

# Pila de tabla de simbolos global
symbols_tables = []

# tabla de tendrá los datos (temporalmente) de la ultima tabla 
# empilada
table_tmp = {}

# Diccionario para traducir operadores a su formato correcto de impresion
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
    '!=' : 'NotEqual',
    '!' : 'Not',
    'in' : 'In'
}

# Definicion de las reglas de precedencia
precedence = (
    ('left', 'TkOr'),
    ('left', 'TkAnd'),
    ('right', 'TkNot'),
    ('nonassoc', 'TkEqual', 'TkNEqual'),
    ('nonassoc','TkLess', 'TkLeq', 'TkGeq', 'TkGreater'),
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult'),
    ('nonassoc', 'UNARY')
)

# ------ DETECCION DE ERRORES ---------
def p_error(p):
    print(f"Sintax error in row {p.lineno}, column" ,
    f"{find_column(p.lexer.lexdata, p)} unexpected token '{str(p.value)}'")
    sys.exit(0)


# ------ ESTRUCTURA DEL PROGRAMA PRINCIPAL ---------
# Simbolo inicial de la gramatica: BLOCK
def p_program(p):
    '''
    BLOCK : TkOBlock DECLARE LIST_INSTRUCTIONS TkCBlock
    '''
    # se desempila la tabla de simbolos del subprograma actual
    symbols_tables.pop(0)
    p[0] = Nodo("Block", p[2], p[3])

# ------ SUBPROGRAMA ---------
def p_subprogram(p):
    '''
    SUBPROGRAM : LIST_INSTRUCTIONS
    '''
    p[0] = p[1]

# ------ BLOQUE DECLARE ---------
def p_declare(p):
    '''
    DECLARE : TkDeclare LIST_DECLARE
            | NO_DECLARE
    '''

    # if len(p) == 1:
    #     p[0] = None
    # else:
    global symbols_tables
    global table_tmp
    symbols_tables.insert(0, table_tmp)
    table_tmp = {}
    p[0] = Nodo("Symbols Table", symbols_tables[0])

def p_no_declare(p):
    '''
    NO_DECLARE : 
    '''
    p[0] = None


# -- Lista de declaracones de variables 
# Condicion para parar la recursion
def p_list_declare_base(p):
    '''
    LIST_DECLARE : VARIABLE_DECLARATION
    '''
    p[0] = p[1]

# -- Lista de declaracones de variables 
def p_list_declare(p):
    '''
    LIST_DECLARE : LIST_DECLARE TkSemicolon VARIABLE_DECLARATION
    '''
    # p[0] = Nodo('Sequencing', p[1], p[3])

                
# -- Lista de variables declaradas en una linea 
# Condicion para parar la recursion
def p_list_variables_declare_base(p):
    '''
    VARIABLE_DECLARATION : TkId TkTwoPoints TYPE
    '''
    global table_tmp
    if p[1] in table_tmp:
        print(f"Error in row {p.lineno(1)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(1))}: "\
        f"variable '{p[1]}' already declared")
        sys.exit(0)
        
    else:
        table_tmp[p[1]] = (p[3], False)
    p[0] = p[3]

# -- Lista de variables declaradas en una linea 
def p_list_variables_declare(p):
    '''
    VARIABLE_DECLARATION : TkId TkComma VARIABLE_DECLARATION
    '''
    global table_tmp
    if p[1] in table_tmp:
        print(f"Error in row {p.lineno(1)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(1))}: "\
        f"variable '{p[1]}' already declared")
        sys.exit(0)
    else:
        table_tmp[p[1]] = (p[3], False)
    p[0] = (p[3])

# -- Tipo de datos para las variables declaradas 
def p_type_varible_declare(p):
    '''
    TYPE : TkInt 
         | TkBool 
         | ARRAY_DECLARATION
    '''
    p[0] = p[1]
    
# -- Declaracion de arreglos 
def p_array_declaration(p):
    '''
    ARRAY_DECLARATION : TkArray TkOBracket NUM TkSoForth NUM TkCBracket
    '''
    p[0] = f"array[{p[3]}..{p[5]}]"

# -- Num puede ser negativo 
def p_num_integer(p):
    '''
    NUM : TkNum
        | TkMinus TkNum
    '''
    if len(p) == 3:
        p[0] = -p[2]
    else:
        p[0] = p[1]

#----- BLOQUE DE INSTRUCCIONES -----
def p_intruccions_list_base(p):
    '''
    LIST_INSTRUCTIONS : INSTRUCTION
    '''
    p[0] = p[1]

#----- Secuencia de instrucciones
def p_intruccions_list(p):
    '''
    LIST_INSTRUCTIONS : LIST_INSTRUCTIONS TkSemicolon INSTRUCTION
    '''
    p[0] = Nodo('Sequencing', p[1], p[3])

#----- Tipos de instrucciones
def p_instruccion(p):
    '''
    INSTRUCTION : ASIG
                | PRINT
                | FOR_LOOP
                | DO_LOOP
                | CONDITIONAL
                | TkSkip
                | BLOCK
    '''
    if p[1] != 'skip':
        p[0] =  p[1]
    else:
        p[0] = Nodo('skip')

#----- INSTRUCCION ASIGNACION -----
def p_asig(p):
    '''
    ASIG : TkId TkAsig EXPRESSION
    '''
    # Verificar que la variable de asignacion fue declarada
    existe_variable = False
    for t in symbols_tables:
        if p[1] in t:

            # verificar si la variable que existe es la 
            # variable de iteracion de un ciclo for
            # if t[p[1]] == 'for':
            if t[p[1]][1]:
                print(f"Error in row {p.lineno(1)}, column "\
                f"{find_column2(p.lexer.lexdata, p.lexpos(1))}: "\
                f"It is changing the variable '{p[1]}', wich is a "
                f"control variable of 'for' statement.'")
                sys.exit(0)

            # verificar que la variable de asignacion posee
            # el mismo tipo que lo asignado
            if t[p[1]][0] != p[3].type:
                print(f"ErrorType in row {p.lineno(2)}, column "\
                f"{find_column2(p.lexer.lexdata, p.lexpos(2))}. "\
                f"'{p[3].name}' is type '{p[3].type}' but '{t[p[1]][0]}' is expected.")
                sys.exit(0)

            p[0] = Nodo('Asig', Nodo(f"Ident: {p[1]} | type: {t[p[1]][0]}"), p[3])
            existe_variable = True
            break

    if not existe_variable:
        print(f"ErrorType in row {p.lineno(1)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(1))}. "\
        f"Undeclared variable '{p[1]}'")
        sys.exit(0)

#-- Puede ser una expresion o la creacion de un arreglo
def p_asig_expresion(p):
    '''
    EXPRESSION : E
               | ASIG_ARRAY
    '''
    p[0] = p[1]

#-- Se puede crear un arreglo de forma manual o extendida
# CREATE_ARRAY --> E,E,E,E, ...
# WRITE_ARRAY  --> array(b:1)(b:2)
def p_asig_array(p):
    '''
    ASIG_ARRAY : CREATE_ARRAY
               | WRITE_ARRAY
    '''
    p[0] = p[1]

#-- Creacion de arreglos de forma manual
# E, E, E, E, E, E, E, ...
# condicion de parada de la recursion
def p_create_array_base(p):
    '''
    CREATE_ARRAY : E TkComma E
    '''
    type_array = symbols_tables[0][p[-2]][0]
    if type_array[0] == 'a':
        len_array = get_len_array_declared(type_array)
        p[0] = NodoExpresiones(f'Comma | type: array with length={len_array}', type_array,p[1], p[3])
    # directo al error
    else:
        p[0] = NodoExpresiones('Comma ', 'array',p[1], p[3])



#-- Creacion de arreglos de forma manual
def p_create_array(p):
    '''
    CREATE_ARRAY : CREATE_ARRAY TkComma E
    '''
    type_array = (symbols_tables[0][p[-2]])[0]
    if type_array[0] == 'a':
        len_array = get_len_array_declared(type_array)
        p[0] = NodoExpresiones(f'Comma | type: array with length={len_array}', type_array,p[1], p[3])
    # directo al error
    else:
        p[0] = NodoExpresiones('Comma ', 'array',p[1], p[3])

#-- Creacion de arreglos de forma extendia
# condicion de parada de la recursion
def p_write_array_base(p):
    '''
    WRITE_ARRAY : TkId TkOpenPar E TkTwoPoints E TkClosePar
    '''
    p[0] = Nodo('WriteArray',Nodo(f"Ident: {p[1]} | type: {(symbols_tables[0][p[1]])[0]}") , Nodo('TwoPoints', p[3], p[5]))
    # p[0] = Nodo("Holas")

#-- Creacion de arreglos de forma extendia
def p_write_array(p):
    '''
    WRITE_ARRAY : WRITE_ARRAY TkOpenPar E TkTwoPoints E TkClosePar
    '''
    p[0] = Nodo('WriteArray', p[1], Nodo("TwoPoints", p[3], p[5]))

#-- Identificar expresiones aritmeticas y booleanas
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

    if p[1].type == p[3].type:
        
        # operadores aritmeticos deben operar con integer
        if p[2] == '+' or p[2] == '*' or p[2] == '-':
            if p[1].type != 'int':
                print(f"ErrorType in row {p.lineno(2)}, column "\
                f"{find_column2(p.lexer.lexdata, p.lexpos(2))}. "\
                f"Arithmetic operator '{p[2]}' expects values of type: 'int'")
                sys.exit(0)
            else:
                p[0] = NodoExpresiones(trad_op.get(p[2]), 'int',p[1], p[3])

        # operadores de orden solo comparan integer
        elif p[2] == '>' or p[2] == '>=' or p[2] == '<' or p[2] == '<=':
            if p[1].type != 'int':
                print(f"ErrorType in row {p.lineno(2)}, column "\
                f"{find_column2(p.lexer.lexdata, p.lexpos(2))}. "\
                f"Comparison operator '{p[2]}' expects values of type: 'int'")
                sys.exit(0)
            else:
                p[0] = NodoExpresiones(trad_op.get(p[2]), 'bool',p[1], p[3])

        # operadores logicos 'and' y 'or' solo operan con booleanos
        elif p[2] == '/\\' or p[2] == '\/':
            if p[1].type != 'bool':
                print(f"ErrorType in row {p.lineno(2)}, column "\
                f"{find_column2(p.lexer.lexdata, p.lexpos(2))}. "\
                f"Logical operator '{p[2]}' expects values of type: 'bool'")
                sys.exit(0)
            else:
                p[0] = NodoExpresiones(trad_op.get(p[2]), 'bool',p[1], p[3])
        
        # operadores restantes (==, !=) operan con cualquier expresion
        else:
            p[0] = NodoExpresiones(trad_op.get(p[2]), 'bool',p[1], p[3])

    else:
        print(f"ErrorType in row {p.lineno(2)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(2))}. "\
        f"'{p[1].name}' is type '{p[1].type}' and " \
        f"'{p[3].name}' is type '{p[3].type}'." )
        sys.exit(0)

#-- Expresoion entre parentesis
def p_expression_par(p):
    '''
    E : TkOpenPar E TkClosePar
    '''
    p[0] = p[2]

#-- Operador unario aplicdo a una expresion
def p_expression_op_unary(p):
    '''
    E : TkNot E
      | TkMinus E %prec UNARY
    '''
    if p[1] == '-':
        p[0] = NodoExpresiones(trad_op.get(p[1]),'int', p[2])
    elif p[1] == '!':
        p[0] = NodoExpresiones(trad_op.get(p[1]),'bool', p[2])


#-- Tipos de expresiones TERMINALES
# acceso al indice de un arreglo
def p_expression_base(p):
    '''
    E : TkNum
      | TkId
      | TkTrue
      | TkFalse
      | READ_ARRAY
    '''
    # si p[1] es un integer
    if isinstance(p[1], int):
        p[0] = NodoExpresiones(f"Literal: {p[1]}", "int")

    # si p[1] es un boleano
    elif p[1] == 'true' or p[1] == 'false':
        p[0] = NodoExpresiones(f"Literal: {p[1]}", "bool")

    # si p[1] es un readArray
    elif isinstance(p[1], Nodo):
        p[0] = p[1]

    # si p[1] es un id
    else:
        # Verificar que la variable de asignacion fue declarada
        existe_variable = False
        for t in symbols_tables:
            if p[1] in t:
                p[0] = NodoExpresiones(f"Ident: {p[1]}", t[p[1]][0])
                existe_variable = True
                break

        if not existe_variable:
            print(f"ErrorType in row {p.lineno(1)}, column "\
            f"{find_column2(p.lexer.lexdata, p.lexpos(1))}. "\
            f"Undeclared variable '{p[1]}'")
            sys.exit(0)
        
#-------- DETECCION DE PRINT'S ------
def p_print(p):
    '''
    PRINT : TkPrint TOPRINT  
    '''
    p[0] = Nodo("Print" ,p[2])

#-- EXpresion a imprimir con multiples concatenaciones
# COndicion de parada para la recursividad
def p_to_print_base(p):
    '''
    TOPRINT : EXPRESSION_TO_PRINT   
    '''
    p[0] = p[1]
    
#-- EXpresion a imprimir con multiples concatenaciones
def p_to_print(p):
    '''
    TOPRINT : TOPRINT TkConcat EXPRESSION_TO_PRINT   
    '''
    p[0] = Nodo('Concat', p[1], p[3])

#-- EXpresiones que son posibles de concatenar e imprimir
def p_expression_print(p):
    '''
    EXPRESSION_TO_PRINT : E
               | STRING
               | READ_ARRAY
    '''
    p[0] = p[1]

#-- Produccio auxiliar de ayuda para la contruccion del AST
def p_string(p):
    '''
    STRING : TkString
    '''
    p[0] = Nodo(f"String: {p[1]} | type: string")

#-- Acceso a un array index
def p_array_index(p):
    '''
    READ_ARRAY : ARRAY TkOBracket E TkCBracket
    '''
    # siempre se accede a la posicion de un arreglo
    # con un numeor entero. Entonces, p[3] tiene
    # que ser un numero entero.
    if p[3].type != 'int':
        print(f"Error in row {p.lineno(2)}, column "\
            f"{find_column2(p.lexer.lexdata, p.lexpos(2))+1}: "\
            f"to access array position with 'int' value")
        sys.exit(0)

    p[0] = NodoExpresiones("ReadArray","int", p[1], p[3])

#-- Acceso a un array index con
# TkId con el nombre del array |
# arreglo escrito de forma estendida
def p_array_index_id_or_read(p):
    '''
    ARRAY : TkId
          | WRITE_ARRAY
    '''
    if isinstance(p[1], Nodo):
        p[0] = p[1]
    else:
        p[0] = NodoExpresiones(f"Ident: {p[1]}", (symbols_tables[0][p[1]])[0])

#-------- DETECCION DE CICLOS FOR ------
def p_for_loop(p):
    '''
    FOR_LOOP : TkFor IT_VAR TkIn E TkTo E TkArrow SUBPROGRAM TkRof
    '''
    # desempilar tabla de simbolos del ciclo for
    global symbols_tables
    symbols_tables.pop(0)

    p[0] = Nodo('For', Nodo('In', p[2], Nodo('To', p[4], p[6])), p[8])

def p_iteration_var(p):
    '''
    IT_VAR : TkId
    '''
    global symbols_tables

    # empilar tabla de simbolos que solo tiene la variable de iteracion del for
    symbols_tables.insert(0, {p[1] : ('int', True)})
    p[0] = Nodo(f"Ident: {p[1]} | type: int")

#-------- DETECCION DE CICLOS DO ------
# Es posible que tenga multiples guardias
def p_do_loop(p):
    '''
    DO_LOOP : TkDo GUARD TkOd
    '''
    p[0] = Nodo('Do', p[2])

#-------- DETECCION DE SENTENCIAS IF / GUARD------
# Es posible que tenga multiples guardias
def p_if_conditional(p):
    '''
    CONDITIONAL : TkIf GUARD TkFi
    '''
    p[0] = Nodo('If', p[2])

#-- Multiples guardias
# Condicion de parada de la recursividad
def p_guard_base(p):
    '''
    GUARD : E TkArrow SUBPROGRAM
    '''
    if p[1].type != 'bool':
        print(f"Error in row {p.lineno(2)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(2))-1}. "\
        f"Condition of statement 'if' expected is type: 'bool'")
        sys.exit(0)
    p[0] = Nodo('Then', p[1], p[3])

#-- Multiples guardias
def p_guard(p):
    '''
    GUARD : GUARD TkGuard E TkArrow SUBPROGRAM
    '''
    if p[3].type != 'bool':
        print(f"Error in row {p.lineno(4)}, column "\
        f"{find_column2(p.lexer.lexdata, p.lexpos(4))-1}. "\
        f"Condition of statement 'if' expected is type: 'bool'")
        sys.exit(0)
    p[0] = Nodo("Guard", p[1], Nodo('Then', p[3], p[5]))

# se construye el parser para el analizador sintactico
parser = yacc.yacc()