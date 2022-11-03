import codecs
import sys
import ply.lex as lex
from Utils.utils import *
import re

archivo = sys.argv[1]

try:

    # abrir archivo
    handleFile = codecs.open(archivo, "r")

    # comprobar extension file
    if not archivo.endswith(".gcl"):
        raise Exception("Error, la extension del archivo debe ser .gcl")

    data = handleFile.read()
    
except FileNotFoundError as e:
    print("Error, archivo [" + archivo + "] no encontrado")
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(0)

handleFile.close()

# Palabras reservadas
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

# defincion de tokens
tokens = ['TkId', 'TkNum', 'TkString', 'TkOBlock', 
'TkCBlock', 'TkSoForth', 'TkComma', 'TkOpenPar', 'TkClosePar', 'TkAsig', 
'TkSemicolon', 'TkArrow', 'TkPlus', 'TkMinus', 'TkMult', 'TkOr',
'TkAnd', 'TkNot', 'TkLeq', 'TkGeq', 'TkLess', 'TkGreater',
'TkEqual', 'TkNEqual', 'TkOBracket', 'TkCBracket', 'TkTwoPoints', 
'TkConcat', 'TkGuard'] + list(reservadas.values())

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
    t.type = reservadas.get(t.value,'TkId') # verificar si pertenece a reservadas

    # verificar si el token es de tipo id
    if t.type == 'TkId' : t.value = "\""+t.value+"\""
    return t

def t_COMMENT(t):
    r'//.*'

def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Error: Unexpected character \"{}\" in row {}, column {}"
    .format(t.value[0], t.lineno, find_column(data, t)))
    t.lexer.skip(1)
    return t

t_ignore  = ' \t'

analizador = lex.lex()
analizador.input(data)
found_error = False
tokens_storage = []

for tok in analizador:
    # tok = analizador.token()
    if not tok : break

    if tok.type == 'error':
        found_error = True

    if found_error:
        continue

    tokens_storage += [tok]

if not found_error:
    for tok in tokens_storage:
        if tok.type == "TkId" or tok.type == "TkNum" or tok.type == "TkString":
            print(tok.type+"("+str(tok.value)+")",
                tok.lineno, find_column(data, tok))
        else:
            print(tok.type, tok.lineno, find_column(data, tok))
