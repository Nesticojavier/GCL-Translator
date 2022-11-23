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


def print_arbol(nodo: Nodo, guion = ""):
    print(guion + str(nodo)) 

    if nodo.leftChild :  
        print_arbol(nodo.leftChild, guion + "-")
        
    
    if nodo.rigthChild:  
        print_arbol(nodo.rigthChild, guion + "-")
   