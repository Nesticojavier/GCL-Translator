from lexer import *

import codecs
import sys
import ply.lex as lex
from Utils.utils import *

def main():
    # Tomar el archivo 
    archivo = sys.argv[1]

    # Intentar leer el archivo con el formato correcto
    try:

        # abrir archivo
        handleFile = codecs.open(archivo, "r")

        # comprobar extension file
        if not archivo.endswith(".gcl"):
            raise Exception("Error, la extension del archivo debe ser .gcl")

        data = handleFile.read()

        # Ejecutar algoritmo de impresion de tokens
        repl()

    except FileNotFoundError as e:
        print("Error, archivo [" + archivo + "] no encontrado")
        # sys.exit(0)
    except Exception as e:
        print(e)
        # sys.exit(0)
    finally:
        handleFile.close()

main()
