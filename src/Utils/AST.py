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



def printArbol(nodo: Nodo, guion = "-"):
    print(guion + str(nodo)) 

    if nodo.leftChild :  
        printArbol(nodo.leftChild, guion + "-")
        guion
    
    if nodo.rigthChild:  
        printArbol(nodo.rigthChild, guion + "-")
   


""" 
Test print Arbol
nieto = Nodo("Nieto")
hijoIzq = Nodo("HijoIzq",nieto)
hijoIzq2 = Nodo("HijoIzq",nieto)

hijoDer = Nodo("HijoDer",hijoIzq2)
Padre = Nodo("Padre",hijoIzq,hijoDer)

printArbol(Padre) """