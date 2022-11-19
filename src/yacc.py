import ply.yacc as yacc
from lexer import tokens

# precedence = (
#     ('rigth', 'TkAsig')
# )

def p_error(p):
    print("error")
    print(p)

def p_program(p):
    '''
    B : TkOBlock DECLARE INSTRUCTIONS TkCBlock
    '''
    p[0] = p[2]
    print(f'******** Todo bien **********')

def p_declare(p):
    '''
    DECLARE : TkDeclare LIST_DECLARE
    '''
    p[0] = (p[1],p[2])

def p_list_declare_base(p):
    '''
    LIST_DECLARE : VARIABLE_DECLARATION
    '''
    p[0] = p[1]

def p_list_declare(p):
    '''
    LIST_DECLARE : VARIABLE_DECLARATION TkSemicolon LIST_DECLARE
    '''
    p[0] = ('Sequencing',p[1], p[3])

                
def p_list_variables_declare_base(p):
    '''
    VARIABLE_DECLARATION : TkId TkTwoPoints TYPE
    '''
    p[0] = ('declaracion', f"{p[1]} {p[2]} {p[3]}")

def p_list_variables_declare(p):
    '''
    VARIABLE_DECLARATION : TkId TkComma VARIABLE_DECLARATION
    '''

def p_type_varible_declare(p):
    '''
    TYPE : TkInt 
         | TkBool 
         | TkArray
    '''
    p[0] = p[1]
    

def p_statements(p):
    '''
    INSTRUCTIONS : INSTRUCTION TkSemicolon INSTRUCTIONS
                  | INSTRUCTION
    '''

def p_statement(p):
    '''
    INSTRUCTION : TkFor
                | TkIf
                | TkDo
                | TkPrint
                | TkId
    '''

parser = yacc.yacc()

data = '''
|[ 
    declare
        h : int;
        g : array;
        g, a, b, c, d, e : int
        //y : bool

    print;
    do;
    for;
    if;
    estoEsUnId
]|
'''

ast = parser.parse(data)
print(ast)
# print(result)