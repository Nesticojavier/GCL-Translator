
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TkAnd TkArray TkArrow TkAsig TkBool TkCBlock TkCBracket TkClosePar TkComma TkConcat TkDeclare TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMinus TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkRof TkSemicolon TkSkip TkSoForth TkString TkTo TkTrue TkTwoPoints\n    BLOCK : TkOBlock DECLARE LIST_INSTRUCTIONS TkCBlock\n    \n    DECLARE : TkDeclare LIST_DECLARE\n    \n    LIST_DECLARE : VARIABLE_DECLARATION\n    \n    LIST_DECLARE : LIST_DECLARE TkSemicolon VARIABLE_DECLARATION\n    \n    VARIABLE_DECLARATION : TkId TkTwoPoints TYPE\n    \n    VARIABLE_DECLARATION : TkId TkComma VARIABLE_DECLARATION\n    \n    TYPE : TkInt \n         | TkBool \n         | ARRAY_DECLARATION\n    \n    ARRAY_DECLARATION : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket\n    \n    LIST_INSTRUCTIONS : INSTRUCTION\n    \n    LIST_INSTRUCTIONS : LIST_INSTRUCTIONS TkSemicolon INSTRUCTION\n    \n    INSTRUCTION : ASIG\n                | PRINT\n                | DO_LOOP\n                | FOR_LOOP\n                | TkSkip\n    \n    ASIG : TkId TkAsig EXPRESSION\n    \n    EXPRESSION : E\n               | ASIG_ARRAY\n    \n    ASIG_ARRAY : CREATE_ARRAY\n               | WRITE_ARRAY\n    \n    CREATE_ARRAY : E TkComma E\n    \n    CREATE_ARRAY : CREATE_ARRAY TkComma E\n    \n    WRITE_ARRAY : TkId TkOpenPar E TkTwoPoints E TkClosePar\n    \n    WRITE_ARRAY : WRITE_ARRAY TkOpenPar E TkTwoPoints E TkClosePar\n    \n    E : E TkMult E\n      | E TkPlus E\n      | E TkMinus E\n      | E TkOr E\n      | E TkAnd E\n      | E TkLess E\n      | E TkLeq E\n      | E TkGeq E\n      | E TkGreater E\n      | E TkEqual E\n      | E TkNEqual E\n    \n    E : TkOpenPar E TkClosePar\n    \n    E : TkNot E\n      | TkMinus E\n    \n    E : TkNum\n      | TkId\n      | TkTrue\n      | TkFalse\n    \n    PRINT : TkPrint TOPRINT  \n    \n    TOPRINT : EXPRESSION_TO_PRINT   \n    \n    TOPRINT : TOPRINT TkConcat EXPRESSION_TO_PRINT   \n    \n    EXPRESSION_TO_PRINT : TkId\n               | TkString\n               | TkNum\n               | TkTrue\n               | TkFalse\n               | READ_ARRAY\n    \n    READ_ARRAY : TkId TkOBracket E TkCBracket\n    \n    DO_LOOP : TkDo E TkArrow LIST_INSTRUCTIONS TkOd\n    \n    FOR_LOOP : TkFor TkId TkIn E TkTo E TkArrow LIST_INSTRUCTIONS TkRof\n    '
    
_lr_action_items = {'TkOBlock':([0,],[2,]),'$end':([1,19,],[0,-1,]),'TkDeclare':([2,],[4,]),'TkSkip':([3,16,17,20,51,67,68,69,70,71,73,109,114,],[11,-2,-3,11,11,-4,-5,-7,-8,-9,-6,11,-10,]),'TkId':([3,4,13,14,15,16,17,20,21,31,32,33,39,41,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,73,74,75,76,77,101,103,104,109,114,],[12,18,24,35,38,-2,-3,12,43,35,35,35,18,18,24,35,12,35,35,35,35,35,35,35,35,35,35,35,35,-4,-5,-7,-8,-9,-6,35,35,35,35,35,35,35,12,-10,]),'TkPrint':([3,16,17,20,51,67,68,69,70,71,73,109,114,],[13,-2,-3,13,13,-4,-5,-7,-8,-9,-6,13,-10,]),'TkDo':([3,16,17,20,51,67,68,69,70,71,73,109,114,],[14,-2,-3,14,14,-4,-5,-7,-8,-9,-6,14,-10,]),'TkFor':([3,16,17,20,51,67,68,69,70,71,73,109,114,],[15,-2,-3,15,15,-4,-5,-7,-8,-9,-6,15,-10,]),'TkCBlock':([5,6,7,8,9,10,11,22,23,24,25,26,27,28,29,34,35,36,37,42,43,44,45,46,47,48,63,65,78,81,82,83,84,85,86,87,88,89,90,91,92,96,97,99,100,111,112,115,],[19,-11,-13,-14,-15,-16,-17,-45,-46,-48,-49,-50,-51,-52,-53,-41,-42,-43,-44,-12,-42,-18,-19,-20,-21,-22,-40,-39,-47,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-23,-24,-54,-55,-25,-26,-56,]),'TkSemicolon':([5,6,7,8,9,10,11,16,17,22,23,24,25,26,27,28,29,34,35,36,37,42,43,44,45,46,47,48,63,65,67,68,69,70,71,73,78,80,81,82,83,84,85,86,87,88,89,90,91,92,96,97,99,100,111,112,113,114,115,],[20,-11,-13,-14,-15,-16,-17,39,-3,-45,-46,-48,-49,-50,-51,-52,-53,-41,-42,-43,-44,-12,-42,-18,-19,-20,-21,-22,-40,-39,-4,-5,-7,-8,-9,-6,-47,20,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-23,-24,-54,-55,-25,-26,20,-10,-56,]),'TkOd':([6,7,8,9,10,11,22,23,24,25,26,27,28,29,34,35,36,37,42,43,44,45,46,47,48,63,65,78,80,81,82,83,84,85,86,87,88,89,90,91,92,96,97,99,100,111,112,115,],[-11,-13,-14,-15,-16,-17,-45,-46,-48,-49,-50,-51,-52,-53,-41,-42,-43,-44,-12,-42,-18,-19,-20,-21,-22,-40,-39,-47,100,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-23,-24,-54,-55,-25,-26,-56,]),'TkRof':([6,7,8,9,10,11,22,23,24,25,26,27,28,29,34,35,36,37,42,43,44,45,46,47,48,63,65,78,81,82,83,84,85,86,87,88,89,90,91,92,96,97,99,100,111,112,113,115,],[-11,-13,-14,-15,-16,-17,-45,-46,-48,-49,-50,-51,-52,-53,-41,-42,-43,-44,-12,-42,-18,-19,-20,-21,-22,-40,-39,-47,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-23,-24,-54,-55,-25,-26,115,-56,]),'TkAsig':([12,],[21,]),'TkString':([13,49,],[25,25,]),'TkNum':([13,14,21,31,32,33,49,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,94,101,103,104,106,],[26,34,34,34,34,34,26,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,102,34,34,34,110,]),'TkTrue':([13,14,21,31,32,33,49,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,101,103,104,],[27,36,36,36,36,36,27,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TkFalse':([13,14,21,31,32,33,49,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,101,103,104,],[28,37,37,37,37,37,28,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TkOpenPar':([14,21,31,32,33,43,48,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,101,103,104,111,112,],[32,32,32,32,32,74,77,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-25,-26,]),'TkNot':([14,21,31,32,33,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,101,103,104,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TkMinus':([14,21,30,31,32,33,34,35,36,37,43,45,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,75,76,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,101,103,104,105,107,108,],[31,31,54,31,31,31,-41,-42,-43,-44,-42,54,31,31,31,31,31,31,31,31,31,31,31,31,54,54,54,31,31,31,31,31,54,54,54,54,54,54,54,54,54,54,54,54,-38,54,54,54,54,54,31,31,31,54,54,54,]),'TkTwoPoints':([18,34,35,36,37,63,65,81,82,83,84,85,86,87,88,89,90,91,92,95,98,],[40,-41,-42,-43,-44,-40,-39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,103,104,]),'TkComma':([18,34,35,36,37,43,45,47,63,65,81,82,83,84,85,86,87,88,89,90,91,92,96,97,],[41,-41,-42,-43,-44,-42,75,76,-40,-39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-23,-24,]),'TkConcat':([22,23,24,25,26,27,28,29,78,99,],[49,-46,-48,-49,-50,-51,-52,-53,-47,-54,]),'TkOBracket':([24,72,],[50,94,]),'TkArrow':([30,34,35,36,37,63,65,81,82,83,84,85,86,87,88,89,90,91,92,105,],[51,-41,-42,-43,-44,-40,-39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,109,]),'TkMult':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[52,-41,-42,-43,-44,-42,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-38,52,52,52,52,52,52,52,52,]),'TkPlus':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[53,-41,-42,-43,-44,-42,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-38,53,53,53,53,53,53,53,53,]),'TkOr':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[55,-41,-42,-43,-44,-42,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-38,55,55,55,55,55,55,55,55,]),'TkAnd':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[56,-41,-42,-43,-44,-42,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-38,56,56,56,56,56,56,56,56,]),'TkLess':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[57,-41,-42,-43,-44,-42,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-38,57,57,57,57,57,57,57,57,]),'TkLeq':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[58,-41,-42,-43,-44,-42,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-38,58,58,58,58,58,58,58,58,]),'TkGeq':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[59,-41,-42,-43,-44,-42,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-38,59,59,59,59,59,59,59,59,]),'TkGreater':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[60,-41,-42,-43,-44,-42,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-38,60,60,60,60,60,60,60,60,]),'TkEqual':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[61,-41,-42,-43,-44,-42,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-38,61,61,61,61,61,61,61,61,]),'TkNEqual':([30,34,35,36,37,43,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,105,107,108,],[62,-41,-42,-43,-44,-42,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-38,62,62,62,62,62,62,62,62,]),'TkClosePar':([34,35,36,37,63,64,65,81,82,83,84,85,86,87,88,89,90,91,92,107,108,],[-41,-42,-43,-44,-40,92,-39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,111,112,]),'TkCBracket':([34,35,36,37,63,65,79,81,82,83,84,85,86,87,88,89,90,91,92,110,],[-41,-42,-43,-44,-40,-39,99,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,114,]),'TkTo':([34,35,36,37,63,65,81,82,83,84,85,86,87,88,89,90,91,92,93,],[-41,-42,-43,-44,-40,-39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,101,]),'TkIn':([38,],[66,]),'TkInt':([40,],[69,]),'TkBool':([40,],[70,]),'TkArray':([40,],[72,]),'TkSoForth':([102,],[106,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'BLOCK':([0,],[1,]),'DECLARE':([2,],[3,]),'LIST_INSTRUCTIONS':([3,51,109,],[5,80,113,]),'INSTRUCTION':([3,20,51,109,],[6,42,6,6,]),'ASIG':([3,20,51,109,],[7,7,7,7,]),'PRINT':([3,20,51,109,],[8,8,8,8,]),'DO_LOOP':([3,20,51,109,],[9,9,9,9,]),'FOR_LOOP':([3,20,51,109,],[10,10,10,10,]),'LIST_DECLARE':([4,],[16,]),'VARIABLE_DECLARATION':([4,39,41,],[17,67,73,]),'TOPRINT':([13,],[22,]),'EXPRESSION_TO_PRINT':([13,49,],[23,78,]),'READ_ARRAY':([13,49,],[29,29,]),'E':([14,21,31,32,33,50,52,53,54,55,56,57,58,59,60,61,62,66,74,75,76,77,101,103,104,],[30,45,63,64,65,79,81,82,83,84,85,86,87,88,89,90,91,93,95,96,97,98,105,107,108,]),'EXPRESSION':([21,],[44,]),'ASIG_ARRAY':([21,],[46,]),'CREATE_ARRAY':([21,],[47,]),'WRITE_ARRAY':([21,],[48,]),'TYPE':([40,],[68,]),'ARRAY_DECLARATION':([40,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> BLOCK","S'",1,None,None,None),
  ('BLOCK -> TkOBlock DECLARE LIST_INSTRUCTIONS TkCBlock','BLOCK',4,'p_program','yacc.py',31),
  ('DECLARE -> TkDeclare LIST_DECLARE','DECLARE',2,'p_declare','yacc.py',39),
  ('LIST_DECLARE -> VARIABLE_DECLARATION','LIST_DECLARE',1,'p_list_declare_base','yacc.py',45),
  ('LIST_DECLARE -> LIST_DECLARE TkSemicolon VARIABLE_DECLARATION','LIST_DECLARE',3,'p_list_declare','yacc.py',51),
  ('VARIABLE_DECLARATION -> TkId TkTwoPoints TYPE','VARIABLE_DECLARATION',3,'p_list_variables_declare_base','yacc.py',58),
  ('VARIABLE_DECLARATION -> TkId TkComma VARIABLE_DECLARATION','VARIABLE_DECLARATION',3,'p_list_variables_declare','yacc.py',64),
  ('TYPE -> TkInt','TYPE',1,'p_type_varible_declare','yacc.py',70),
  ('TYPE -> TkBool','TYPE',1,'p_type_varible_declare','yacc.py',71),
  ('TYPE -> ARRAY_DECLARATION','TYPE',1,'p_type_varible_declare','yacc.py',72),
  ('ARRAY_DECLARATION -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket','ARRAY_DECLARATION',6,'p_array_declaration','yacc.py',78),
  ('LIST_INSTRUCTIONS -> INSTRUCTION','LIST_INSTRUCTIONS',1,'p_intruccions_list_base','yacc.py',85),
  ('LIST_INSTRUCTIONS -> LIST_INSTRUCTIONS TkSemicolon INSTRUCTION','LIST_INSTRUCTIONS',3,'p_intruccions_list','yacc.py',91),
  ('INSTRUCTION -> ASIG','INSTRUCTION',1,'p_instruccion','yacc.py',97),
  ('INSTRUCTION -> PRINT','INSTRUCTION',1,'p_instruccion','yacc.py',98),
  ('INSTRUCTION -> DO_LOOP','INSTRUCTION',1,'p_instruccion','yacc.py',99),
  ('INSTRUCTION -> FOR_LOOP','INSTRUCTION',1,'p_instruccion','yacc.py',100),
  ('INSTRUCTION -> TkSkip','INSTRUCTION',1,'p_instruccion','yacc.py',101),
  ('ASIG -> TkId TkAsig EXPRESSION','ASIG',3,'p_asig','yacc.py',112),
  ('EXPRESSION -> E','EXPRESSION',1,'p_asig_expresion','yacc.py',118),
  ('EXPRESSION -> ASIG_ARRAY','EXPRESSION',1,'p_asig_expresion','yacc.py',119),
  ('ASIG_ARRAY -> CREATE_ARRAY','ASIG_ARRAY',1,'p_asig_array','yacc.py',125),
  ('ASIG_ARRAY -> WRITE_ARRAY','ASIG_ARRAY',1,'p_asig_array','yacc.py',126),
  ('CREATE_ARRAY -> E TkComma E','CREATE_ARRAY',3,'p_create_array','yacc.py',132),
  ('CREATE_ARRAY -> CREATE_ARRAY TkComma E','CREATE_ARRAY',3,'p_create_array_base','yacc.py',138),
  ('WRITE_ARRAY -> TkId TkOpenPar E TkTwoPoints E TkClosePar','WRITE_ARRAY',6,'p_write_array_base','yacc.py',144),
  ('WRITE_ARRAY -> WRITE_ARRAY TkOpenPar E TkTwoPoints E TkClosePar','WRITE_ARRAY',6,'p_write_array','yacc.py',151),
  ('E -> E TkMult E','E',3,'p_expression_op_binary','yacc.py',158),
  ('E -> E TkPlus E','E',3,'p_expression_op_binary','yacc.py',159),
  ('E -> E TkMinus E','E',3,'p_expression_op_binary','yacc.py',160),
  ('E -> E TkOr E','E',3,'p_expression_op_binary','yacc.py',161),
  ('E -> E TkAnd E','E',3,'p_expression_op_binary','yacc.py',162),
  ('E -> E TkLess E','E',3,'p_expression_op_binary','yacc.py',163),
  ('E -> E TkLeq E','E',3,'p_expression_op_binary','yacc.py',164),
  ('E -> E TkGeq E','E',3,'p_expression_op_binary','yacc.py',165),
  ('E -> E TkGreater E','E',3,'p_expression_op_binary','yacc.py',166),
  ('E -> E TkEqual E','E',3,'p_expression_op_binary','yacc.py',167),
  ('E -> E TkNEqual E','E',3,'p_expression_op_binary','yacc.py',168),
  ('E -> TkOpenPar E TkClosePar','E',3,'p_expression_par','yacc.py',174),
  ('E -> TkNot E','E',2,'p_expression_op_unary','yacc.py',180),
  ('E -> TkMinus E','E',2,'p_expression_op_unary','yacc.py',181),
  ('E -> TkNum','E',1,'p_expression_base','yacc.py',187),
  ('E -> TkId','E',1,'p_expression_base','yacc.py',188),
  ('E -> TkTrue','E',1,'p_expression_base','yacc.py',189),
  ('E -> TkFalse','E',1,'p_expression_base','yacc.py',190),
  ('PRINT -> TkPrint TOPRINT','PRINT',2,'p_print','yacc.py',202),
  ('TOPRINT -> EXPRESSION_TO_PRINT','TOPRINT',1,'p_to_print_base','yacc.py',208),
  ('TOPRINT -> TOPRINT TkConcat EXPRESSION_TO_PRINT','TOPRINT',3,'p_to_print','yacc.py',214),
  ('EXPRESSION_TO_PRINT -> TkId','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',220),
  ('EXPRESSION_TO_PRINT -> TkString','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',221),
  ('EXPRESSION_TO_PRINT -> TkNum','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',222),
  ('EXPRESSION_TO_PRINT -> TkTrue','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',223),
  ('EXPRESSION_TO_PRINT -> TkFalse','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',224),
  ('EXPRESSION_TO_PRINT -> READ_ARRAY','EXPRESSION_TO_PRINT',1,'p_expression_print','yacc.py',225),
  ('READ_ARRAY -> TkId TkOBracket E TkCBracket','READ_ARRAY',4,'p_array_index','yacc.py',234),
  ('DO_LOOP -> TkDo E TkArrow LIST_INSTRUCTIONS TkOd','DO_LOOP',5,'p_do_loop','yacc.py',241),
  ('FOR_LOOP -> TkFor TkId TkIn E TkTo E TkArrow LIST_INSTRUCTIONS TkRof','FOR_LOOP',9,'p_for_loop','yacc.py',248),
]
