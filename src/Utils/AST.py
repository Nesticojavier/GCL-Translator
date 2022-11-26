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


def print_arbol(nodo: Nodo, tab = ""):
    '''
    Funcion recursiva usada para imprimir el AST
    
    nodo -- nodo raiz a imprimir en el momento
    tab -- valor por defecto para facilitar la vista del arbol

    return void
    '''
    print(tab + str(nodo)) 

    if nodo.leftChild :  
        print_arbol(nodo.leftChild, tab + "-")
        
    
    if nodo.rigthChild:  
        print_arbol(nodo.rigthChild, tab + "-")
   