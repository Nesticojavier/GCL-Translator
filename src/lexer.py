import codecs
import sys
import ply.lex as lex

archivo = sys.argv[1]

try:
    # abrir archivo
    handleFile = codecs.open("../entradas/"+ archivo, "r", "utf-8")

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
finally:
    handleFile.close()

# defincion de tokens
tokens = ('TkId', 'TkNum', 'TkString', 'TkTrue', 'TkFalse', 'TkOBlock', 
'TkCBlock', 'TkSoForth', 'TkComma', 'TkOpenPar', 'TkClosePar', 'TkAsig', 
'TkSemicolon', 'TkArrow', 'TkPlus', 'TkMinus', 'TkMult', 'TkOr',
'TkAnd', 'TkNot', 'TkLess', 'TkLeq', 'TkGeq', 'TkGreater',
'TkEqual', 'TkNEqual', 'TkOBracket', 'TkCBracket', 'TkTwoPoints', 'TkConcat')

# TODO: terminar de definir tokens y funciones
t_TkOBlock = r'\|\['
t_TkCBlock = r'\]\|'
t_TkSoForth = r'\.\.'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'==>'
t_TkPlus = r'\+'
t_TkMinus = r'\-'

t_TkOBracket = r'\['
t_TkCBracket = r'\]'
t_TkTwoPoints = r':'


def t_COMMENT(t):
    r'//.*'

def t_TkNum(t):
     r'\d+'
     t.value = int(t.value)    
     return t

# por los momentos se ignoraras todos los ID para evitar errores en las pruebas
t_ignore  = ' \tabcdefghijklmnopqrstuvxyzED'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

analizador = lex.lex()
analizador.input(data)


def find_column(input, token):
    '''
        Funcion auxiliar usada para encontrar la posicion de la columna del
        token
    '''
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

while True:
    tok = analizador.token()
    if not tok : break

    if tok.type == "TkId" or tok.type == "TkNum" or tok.type == "TkString":
        print(tok.type+"("+str(tok.value)+")", tok.lineno, find_column(data, tok))
    else:
        print(tok.type, tok.lineno, find_column(data, tok))
