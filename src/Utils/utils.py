""" Algunas funciones de utilidad para el proyecto

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""

import re

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

def find_column2(input, token_pos):
    '''
        Funcion auxiliar usada para encontrar la posicion de la columna del
        token

        input -- str con el contenido del archivo
        token_pos -- el token lex pos de cierto token(int)

        return integer con el numero de columna donde se encuentra el token
    '''
    line_start = input.rfind('\n', 0, token_pos) + 1
    return (token_pos - line_start) + 1

def get_len_array_declared(array: str) -> int:
    '''
        Funcion usada para calcular el tamanyo de un array en su forma de
        declaracion. 

        array -- str de la forma "array[x..y]"
        
        return integer que corresponde al tamanyo del arreglo. len = y-x
            
    '''
    rango = re.findall(r'[-]?\d+', array)
    return int(rango[1]) - int(rango[0]) + 1