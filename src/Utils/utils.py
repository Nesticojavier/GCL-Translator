""" Algunas funciones de utilidad para el proyecto

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""

def find_column(input, token):
    '''
        Funcion auxiliar usada para encontrar la posicion de la columna del
        token

        input -- str con el contenido del archivo
        token -- token a buscar

        return integer con el numero de columna donde se encuentra el token
    '''
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1