import sys

archivo = sys.argv[1]

try:
    # abrir archivo
    handleFile = open("../entradas/"+ archivo, "r")

    # comprobar extension file
    if not archivo.endswith(".gcl"):
        raise Exception("Error, la extension del archivo debe ser .gcl")

except FileNotFoundError as e:
    print("Error, archivo [" + archivo + "] no encontrado")
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(0)

print(handleFile.read())
