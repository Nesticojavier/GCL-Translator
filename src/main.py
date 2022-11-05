"""Programa cliente para el analizador lexicografico para el lenguaje GCL

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""
from lexer import *
import codecs
import sys

# Tomar el archivo 
archivo = sys.argv[1]

# Intentar leer el archivo con el formato correcto
try:

    # abrir archivo
    handleFile = codecs.open(archivo)

    # comprobar extension file
    if not archivo.endswith(".gcl"):
        raise Exception("Error, la extension del archivo debe ser .gcl")
        
    data = handleFile.read()

    # Ejecutar algoritmo de impresion de tokens
    repl(data)

except FileNotFoundError as e:
    print("Error, archivo [" + archivo + "] no encontrado")
    # sys.exit(0)
except Exception as e:
    print(e)
    # sys.exit(0)
finally:
    handleFile.close()

