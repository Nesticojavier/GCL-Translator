"""Implementacion de un analizador lexicografico para el lenguaje GCL

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""

import ply.lex as lex
from Utils.utils import *
# from main import data

# Diccionarion con las palabras reservadas del lenguaje
reservadas = {
    'declare' : 'TkDeclare',
    'if' : 'TkIf',
    'fi' : 'TkFi',
    'do' : 'TkDo',
    'od' : 'TkOd',
    'for' : 'TkFor',
    'rof' : 'TkRof',
    'print' : 'TkPrint',
    'array' : 'TkArray',
    'int' : 'TkInt',
    'bool' : 'TkBool',
    'false' : 'TkFalse',
    'true' : 'TkTrue',
    'in' : 'TkIn',
    'to' : 'TkTo',
    'skip' : 'TkSkip'
}

# Defincion de los tokens
tokens = ['TkId', 'TkNum', 'TkString', 'TkOBlock', 
'TkCBlock', 'TkSoForth', 'TkComma', 'TkOpenPar', 'TkClosePar', 'TkAsig', 
'TkSemicolon', 'TkArrow', 'TkPlus', 'TkMinus', 'TkMult', 'TkOr',
'TkAnd', 'TkNot', 'TkLeq', 'TkGeq', 'TkLess', 'TkGreater',
'TkEqual', 'TkNEqual', 'TkOBracket', 'TkCBracket', 'TkTwoPoints', 
'TkConcat', 'TkGuard'] + list(reservadas.values())

# RegEx para obtener para obtener cada token
t_TkString = r'\"((\\\")|[^\"\n(\\.)]|(\\\\)|(\\n)|(\.))*\"'
t_TkOBlock = r'\|\['
t_TkCBlock = r'\]\|'
t_TkSoForth = r'\.\.'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'-->'
t_TkPlus = r'\+'
t_TkGuard = r'\[\]'
t_TkMinus = r'\-'
t_TkMult = r'\*'
t_TkOr = r'\\\/'
t_TkAnd = r'\/\\'
t_TkNot = r'\!'
t_TkLess = r'\<'
t_TkLeq = r'\<\='
t_TkGeq = r'\>\='
t_TkGreater = r'\>'
t_TkEqual = r'=='
t_TkNEqual = r'\!\='
t_TkOBracket = r'\['
t_TkCBracket = r'\]'
t_TkTwoPoints = r':'
t_TkConcat = r'\.'

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    """ RegEx para obtener el token de las variables del lenguaje
        
        Si  esta hace match con alguna palabra reservada, esta
        no será considerada como un id y retornara el token
        correspondiente a la palabra reserada.
    """


    # Verificar si el token pertenece a las palabras reservadas
    t.type = reservadas.get(t.value,'TkId') 

    # Verificar si el token es de tipo id.
    # En caso de serlo, obtener el valor del id
    if t.type == 'TkId' : t.value = t.value

    return t

# Se ignoran toda la linea despues de un //
def t_COMMENT(t):
    r'//.*'

# RegEx correspondiente al token de un numero decimal
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Se ignoran los saltos de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Se debe ignorar espacios en blanco y tabs
t_ignore  = ' \t'

# Manejo de caracteres ilegales
def t_error(t):
    print("Error: Unexpected character \"{}\" in row {}, column {}"
    .format(t.value[0], t.lineno, find_column(data, t)))
    t.lexer.skip(1)
    return t

# construccion del lexer
analizador = lex.lex()