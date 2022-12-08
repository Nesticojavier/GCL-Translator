""" Implementacion de la clase que ayuda con la construccion del AST

Copyright (C) 2022 - Nestor Gonzalez - José Pérez
CI3725 - Traductores e Interpretadores
"""

class Nodo():
    def __init__(self, name: str, leftChild: object = None, rigthChild: object = None):
        """Nodo del AST"""
        # String que describe al nodo, y valor
        self.name = name 

        # Terminos izquierdo y derecho de la operacion
        self.leftChild = leftChild 
        self.rigthChild = rigthChild

    def __str__(self) -> str:
      return self.name

class NodoExpresiones(Nodo):
    def __init__(self, name: str, type: str,leftChild: object = None, rigthChild: object = None):
        """
        Nodo para las expresiones.
        Estas estos tendran como atributo adicional el tipo de datos de la expresion
        """
        # String que describe al nodo, y valor
        self.name = name 
        self.type = type 

        # Terminos izquierdo y derecho de la operacion
        self.leftChild = leftChild 
        self.rigthChild = rigthChild

    def __str__(self) -> str:
      return f"{self.name} | type: {self.type}"


def print_arbol(nodo: Nodo, tab = "", probate = ""):
    '''
    Funcion recursiva usada para imprimir el AST
    
    nodo -- nodo raiz a imprimir en el momento
    tab -- valor por defecto para facilitar la vista del arbol

    return void
    '''
    print(tab + str(nodo))

    # Si el nodo es tabla de simbolos; el leftChild es el diccionario
    if nodo.name == 'Symbols Table':
        tabla = nodo.leftChild
        for i in tabla:
            print(f"{tab}-variable: {i} | type: {tabla[i]}")
        return

    # if nodo.leftChild and nodo.name != 'Declare':  
    if nodo.leftChild:  
        print_arbol(nodo.leftChild, tab + "-")
        
    
    # if nodo.rigthChild and nodo.name != 'Declare':  
    if nodo.rigthChild:  
        print_arbol(nodo.rigthChild, tab + "-")
   