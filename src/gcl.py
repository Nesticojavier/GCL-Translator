"""Programa principal para el analizador del lenguaje GCL

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""
import sys
from tokens import analizador_lexico
import codecs
from Utils.AST import print_arbol
from grammar import parser

# Tomar el archivo 
archivo = sys.argv[1]

# Intentar leer el archivo con el formato correcto
try:

    # abrir archivo
    handleFile = codecs.open(archivo)

    try:   
        # comprobar extension file
        if not archivo.endswith(".gcl"):
            raise Exception("Error, la extension del archivo debe ser .gcl")

        data = handleFile.read()

        # # pasar la cadena de string a analizar al lexer
        analizador_lexico.input(data)

        # clonar lexer e intentar hallar errores lexicos
        newLexer = analizador_lexico.clone()
        found_lexical_error = False
        for tok in newLexer:
            if not tok : break

            if tok.type == 'error':
                found_lexical_error = True

        # Si no hay ningun error lexico, se ejecuta el analisis sintactico
        if not found_lexical_error:
            ast = parser.parse(data)
            print_arbol(ast)

    finally:
        handleFile.close()

except FileNotFoundError as e:
    print("Error, archivo [" + archivo + "] no encontrado")
except Exception as e:
    print(e)
