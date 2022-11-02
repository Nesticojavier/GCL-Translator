def find_column(input, token):
    '''
        Funcion auxiliar usada para encontrar la posicion de la columna del
        token
    '''
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1