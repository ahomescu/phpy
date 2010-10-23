# Generator script that outputs classes for all nodes
# For output, see ast_nodes.py

node_descs = {
    # Names
    "Name": [['parse_string', 'WRAP']],
    "DName": [['parse_string', 'WRAP']],
    "Qualifier": [['parse_node'], ['parse_tok']],
    "Self": [['parse_tok'], ['parse_tok']],
    "Parent": [['parse_tok'], ['parse_tok']],

    # Types
    "BoolTy": [],
    "IntTy": [],
    "DoubleTy": [],
    "StringTy": [],
    "ArrayTy": [],
    "ObjectTy": [],

    # Expressions
    "Lv": [['parse_lvalue']],
    "Sc": [['parse_node']],
    "Binary": [['parse_expr'], ['parse_node', 'WRAP'], ['parse_expr']],
    "Unary": [['parse_node', 'WRAP'], ['parse_expr']],
    "Assign": [['parse_lvalue'], ['parse_tok'], ['parse_expr']],
    "AssignOp": [['parse_lvalue'], ['parse_node', 'WRAP'], ['parse_expr']],
    "Postfix": [['parse_lvalue'], ['parse_node', 'WRAP']],
    "Infix": [['parse_node', 'WRAP'], ['parse_lvalue']],
    "CondExpr": [['parse_expr'], ['parse_tok'], ['parse_expr'], 
                               ['parse_tok'], ['parse_expr']],
    "AssignList": [['parse_tok'], ['parse_node', 'COMMA_LIST', 'PAREN'],
                   ['parse_tok'], ['parse_expr']],
    "ConsArray": [['parse_tok'], ['parse_node', 'COMMA_LIST', 'PAREN']],
    "New": [['parse_tok'], ['parse_node'], 
            ['parse_node', 'COMMA_LIST', 'PAREN', 'OPTION']],
    "Clone": [['parse_tok'], ['parse_expr']],
    "AssignRef": [['parse_lvalue'], ['parse_tok'], 
                  ['parse_tok'], ['parse_lvalue']],
    "AssignNew": [['parse_lvalue'], ['parse_tok'], ['parse_tok'],
                  ['parse_tok'], ['parse_node'], ['parse_node', 'COMMA_LIST',
                      'PAREN', 'OPTION']],
    "Cast": [['parse_tok', 'WRAP'], ['parse_expr']],
    "CastUnset": [['parse_tok'], ['parse_expr']],
    "InstanceOf": [['parse_expr'], ['parse_tok'], ['parse_node']],
    "Eval": [['parse_tok'], ['parse_expr', 'PAREN']],
    "Lambda": [['parse_lambda_def']],
    "Exit": [['parse_tok'], ['parse_expr', 'OPTION', 'PAREN', 'OPTION']],
    "At": [['parse_tok'], ['parse_expr']],
    "Print": [['parse_tok'], ['parse_expr']],
    "BackQuote": [['parse_tok'], ['parse_node', 'LIST'], ['parse_tok']],
    "Include": [['parse_tok'], ['parse_expr']],
    "IncludeOnce": [['parse_tok'], ['parse_expr']],
    "Require": [['parse_tok'], ['parse_expr']],
    "RequireOnce": [['parse_tok'], ['parse_expr']],
    "Empty": [['parse_tok'], ['parse_lvalue', 'PAREN']],
    "Isset": [['parse_tok'], ['parse_lvalue', 'COMMA_LIST', 'PAREN']],
    "EDots": [['parse_info']],
    "ParenExpr": [['parse_expr', 'PAREN']],
    "C": [['parse_node']],
    "ClassConstant": [['parse_node'], ['parse_node']],
    "Guil": [['parse_tok'], ['parse_node', 'LIST'], ['parse_tok']],
    "HereDoc": [['parse_tok'], ['parse_node', 'LIST'], ['parse_tok']],
    "Int": [['parse_string', 'WRAP']],
    "Double": [['parse_string', 'WRAP']],
    "String": [['parse_string', 'WRAP']],
    "CName": [['parse_node']],
    "PreProcess": [['parse_node', 'WRAP']],
    "Line": [],
    "File": [],
    "ClassC": [],
    "MethodC": [],
    "FunctionC": [],
    "EncapsString": [['parse_string', 'WRAP']],
    "EncapsVar": [['parse_lvalue']],
    "EncapsCurly": [['parse_tok'], ['parse_lvalue'], ['parse_tok']],
    "EncapsDollarCurly": [['parse_tok'], ['parse_lvalue'], ['parse_tok']],
    "EncapsExpr": [['parse_tok'], ['parse_expr'], ['parse_tok']],
    "Inc": [],
    "Dec": [],
    "Arith": [['parse_node']],
    "Logical": [['parse_node']],
    "BinaryConcat": [],
    "Plus": [],
    "Minus": [],
    "Mul": [],
    "Div": [],
    "Mod": [],
    "DecLeft": [],
    "DecRight": [],
    "And": [],
    "Or": [],
    "Xor": [],
    "Inf": [],
    "Sup": [],
    "InfEq": [],
    "SupEq": [],
    "Eq": [],
    "NotEq": [],
    "Identical": [],
    "NotIdentical": [],
    "AndLog": [],
    "OrLog": [],
    "XorLog": [],
    "AndBool": [],
    "OrBool": [],
    "AssignOpArith": [['parse_node']],
    "AssignConcat": [],
    "UnPlus": [],
    "UnMinus": [],
    "UnBang": [],
    "UnTilde": [],
    "ListVar": [['parse_lvalue']],
    "ListList": [['parse_tok'], ['parse_node', 'COMMA_LIST', 'PAREN']],
    "ListEmpty": [],
    "ArrayExpr": [['parse_expr']],
    "ArrayRef": [['parse_tok'], ['parse_lvalue']],
    "ArrayArrowExpr": [['parse_expr'], ['parse_tok'], ['parse_expr']],
    "ArrayArrowRef": [['parse_expr'], ['parse_tok'],
                ['parse_tok'], ['parse_lvalue']],
    "ClassNameRefStatic": [['parse_node']],
    "ClassNameRefDynamic": [['parse_lvalue'],
                ['parse_obj_prop_access', 'LIST']],

    # Lvalues
    "Var": [['parse_node'], ['parse_scope', 'REF']],
    "This": [['parse_tok']],
    "VArrayAccess": [['parse_lvalue'], ['parse_expr', 'OPTION', 'BRACKET']],
    "VBrace": [['parse_tok'], ['parse_expr', 'BRACE']],
    "VBraceAccess": [['parse_lvalue'], ['parse_expr', 'BRACE']],
    "Indirect": [['parse_lvalue'], ['parse_node']],
    "VQualifier": [['parse_node'], ['parse_lvalue']],
    "FunCallSimple": [['parse_node'], ['parse_node', 'COMMA_LIST', 'PAREN']],
    "FunCallVar": [['parse_node'], ['parse_node', 'COMMA_LIST', 'PAREN']],
    "StaticMethodCallSimple": [['parse_node'], ['parse_node'],
                ['parse_node', 'COMMA_LIST', 'PAREN']],
    "MethodCallSimple": [['parse_lvalue'], ['parse_tok'], ['parse_node'],
                ['parse_node', 'COMMA_LIST', 'PAREN']],
    "ObjAccessSimple": [['parse_lvalue'], ['parse_tok'], ['parse_node']],
    "ObjAccess": [['parse_lvalue'], ['parse_obj_access']],
    "Dollar": [['parse_tok']],
    "Arg": [['parse_expr']],
    "ArgRef": [['parse_tok'], ['parse_lvalue']],
    "ObjProp": [['parse_node']],
    "ObjPropVar": [['parse_lvalue']],
    "OName": [['parse_node']],
    "OBrace": [['parse_expr', 'BRACE']],
    "OArrayAccess": [['parse_node'], ['parse_expr', 'OPTION', 'BRACKET']],
    "OBraceAccess": [['parse_node'], ['parse_expr', 'BRACE']],

    # Statements
    "ExprStmt": [['parse_expr'], ['parse_tok']],
    "EmptyStmt": [['parse_tok']],
    "Block": [['parse_node', 'LIST', 'BRACE']],
    "If": [['parse_tok'], ['parse_expr', 'PAREN'], ['parse_node'],
           ['parse_elseif', 'LIST'], ['parse_else', 'OPTION']],
    "IfColon": [['parse_tok'], ['parse_expr', 'PAREN'], ['parse_tok'],
                ['parse_node', 'LIST'], ['parse_new_elseif', 'LIST'],
                ['parse_new_else', 'OPTION'], ['parse_tok'], ['parse_tok']],
    "While": [['parse_tok'], ['parse_expr', 'PAREN'], ['parse_node']],
    "Do": [['parse_tok'], ['parse_node'], ['parse_tok'],
           ['parse_expr', 'PAREN'], ['parse_tok']],
    "For": [['parse_tok'], ['parse_tok'], ['parse_expr', 'COMMA_LIST'],
            ['parse_tok'], ['parse_expr', 'COMMA_LIST'], ['parse_tok'],
            ['parse_expr', 'COMMA_LIST'], ['parse_tok'], ['parse_node']],
    "Switch": [['parse_tok'], ['parse_expr', 'PAREN'], ['parse_node']],
    "Foreach": [['parse_tok'], ['parse_tok'], ['parse_expr'], ['parse_tok'],
                ['parse_foreach_variable_or_lvalue'],
                ['parse_foreach_arrow', 'OPTION'],
                ['parse_tok'], ['parse_node']],
    "Break": [['parse_tok'], ['parse_expr', 'OPTION'], ['parse_tok']],
    "Continue": [['parse_tok'], ['parse_expr', 'OPTION'], ['parse_tok']],
    "Return": [['parse_tok'], ['parse_expr', 'OPTION'], ['parse_tok']],
    "Throw": [['parse_tok'], ['parse_expr'], ['parse_tok']],
    "Try": [['parse_tok'], ['parse_node', 'LIST', 'BRACE'],
            ['parse_catch'], ['parse_catch', 'LIST']],
    "Echo": [['parse_tok'], ['parse_expr', 'COMMA_LIST'], ['parse_tok']],
    "Globals": [['parse_tok'], ['parse_node', 'COMMA_LIST'], ['parse_tok']],
    "StaticVars": [['parse_tok'], ['parse_static_var', 'COMMA_LIST'], ['parse_tok']],
    "InlineHtml": [['parse_string', 'WRAP']],
    "Use": [['parse_tok'], ['parse_node'], ['parse_tok']],
    "Unset": [['parse_tok'], ['parse_lvalue', 'COMMA_LIST', 'PAREN'], 
              ['parse_tok']],
    "Declare": [['parse_tok'], ['parse_declare', 'COMMA_LIST', 'PAREN'],
                ['parse_node']],
    "TypedDeclaration": [['parse_node'], ['parse_lvalue'],
                         ['parse_tok_expr', 'OPTION'], ['parse_tok']],
    "CaseList": [['parse_tok'], ['parse_tok', 'OPTION'],
                 ['parse_node', 'LIST'], ['parse_tok']],
    "CaseColonList": [['parse_tok'], ['parse_tok', 'OPTION'],
                      ['parse_node', 'LIST'], 
                      ['parse_tok'], ['parse_tok']],
    "Case": [['parse_tok'], ['parse_expr'], ['parse_tok'],
             ['parse_node', 'LIST']],
    "Default": [['parse_tok'], ['parse_tok'], ['parse_node', 'LIST']],
    "UseDirect": [['parse_string', 'WRAP']],
    "UseParen": [['parse_string', 'WRAP', 'PAREN']],
    "SingleStmt": [['parse_node']],
    "ColonStmt": [['parse_tok'], ['parse_node', 'LIST'], 
                  ['parse_tok'], ['parse_tok']],

    # Classes
    "Hint": [['parse_node']],
    "HintArray": [['parse_tok']],
    "LexicalVar": [['parse_is_ref'], ['parse_node']],
    "ClassRegular": [['parse_tok']],
    "ClassFinal": [['parse_tok'], ['parse_tok']],
    "ClassAbstract": [['parse_tok'], ['parse_tok']],
    "ClassConstants": [['parse_tok'], ['parse_class_constant', 'COMMA_LIST'],
                       ['parse_tok']],
    "ClassVariables": [['parse_node'], ['parse_node', 'OPTION'],
                       ['parse_class_variable', 'COMMA_LIST'],
                       ['parse_tok']],
    "Method": [['parse_method_def']],
    "NoModifiers": [['parse_tok']],
    "VModifiers": [['parse_node', 'WRAP', 'LIST']],
    "Public": [],
    "Private": [],
    "Protected": [],
    "Static": [],
    "Abstract": [],
    "Final": [],
    "AbstractMethod": [['parse_tok']],
    "MethodBody": [['parse_node', 'LIST', 'BRACE']],

    # Other declarations
    "GlobalVar": [['parse_node']],
    "GlobalDollar": [['parse_tok'], ['parse_lvalue']],
    "GlobalDollarExpr": [['parse_tok'], ['parse_expr', 'BRACE']],
    "StaticConstant": [['parse_node']],
    "StaticClassConstant": [['parse_node'], ['parse_node']],
    "StaticPlus": [['parse_tok'], ['parse_node']],
    "StaticMinus": [['parse_tok'], ['parse_node']],
    "StaticArray": [['parse_tok'], ['parse_node', 'COMMA_LIST', 'PAREN']],
    "StaticArraySingle": [['parse_node']],
    "StaticArrayArrow": [['parse_node'], ['parse_tok']],

    # Statements and definitions
    "Stmt": [['parse_node']],
    "FuncDefNested": [['parse_node']],
    "ClassDefNested": [['parse_node']],
    "InterfaceDefNested": [['parse_node']],

    # Top level
    "StmtList": [['parse_node', 'LIST']],
    "FuncDef": [['parse_func_def']],
    "ClassDef": [['parse_class_def']],
    "InterfaceDef": [['parse_interface_def']],
    "Halt": [['parse_tok'], ['parse_string', 'PAREN'], ['parse_tok']],
    "NotParsedCorrectly": [['parse_info', 'LIST']],
    "FinalDef": [['parse_info']],
}

def main():
    print r"""
# File auto-generated by ast_gen.py

import ast_parse

# Classes written by hand
class Parameter:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_with_options(ast_node[0],
               [ast_parse.parse_node, ast_parse.OPTION]),
        ast_parse.parse_is_ref(ast_node[1]),
        ast_parse.parse_node(ast_node[2]),
        ast_parse.parse_with_options(ast_node[3],
               [ast_parse.parse_node, ast_parse.OPTION])
        ])

class Catch:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_tok(ast_node[0]),
        ast_parse.parse_with_options(ast_node[1],
               [ast_parse.parse_catch_name, ast_parse.PAREN]),
        ast_parse.parse_with_options(ast_node[2],
               [ast_parse.parse_node, ast_parse.LIST, ast_parse.BRACE])
        ])

class ObjAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_tok(ast_node[0]),
        ast_parse.parse_node(ast_node[1]),
        ast_parse.parse_with_options(ast_node[2],
                [ast_parse.parse_node, ast_parse.COMMA_LIST, 
                    ast_parse.PAREN, ast_parse.OPTION])
        ])

class ObjPropAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_tok(ast_node[0]),
        ast_parse.parse_node(ast_node[1])
        ])

class ElseIf:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_token(ast_node[0]),
        ast_parse.parse_with_options(ast_node[1], 
                [ast_parse.parse_expr, ast_parse.PAREN]),
        ast_parse.parse_node(ast_node[2])
        ])

class Else:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_token(ast_node[0]),
        ast_parse.parse_node(ast_node[1])
        ])

class New_ElseIf:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_token(ast_node[0]),
        ast_parse.parse_with_options(ast_node[1], 
                [ast_parse.parse_expr, ast_parse.PAREN]),
        ast_parse.parse_token(ast_node[2]),
        ast_parse.parse_with_options(ast_node[3], 
                [ast_parse.parse_node, ast_parse.LIST])
        ])

class New_Else:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([
        ast_parse.parse_token(ast_node[0]),
        ast_parse.parse_token(ast_node[1]),
        ast_parse.parse_with_options(ast_node[2],
                [ast_parse.parse_node, ast_parse.LIST])
        ])

# Auto-generated classes"""

    for name, sons in node_descs.iteritems():
        son_parsers = []
        i = 0
        for son in sons:
            i = i + 1
            son_parsers.append('ast_parse.parse_with_options(ast_node[%d], [%s])' % (
                i, ', '.join([('ast_parse.%s' % str(x)) for x in son])))
        print 'class %s:' % name
        print '  def __init__(self, ast_node):'
        #print '    self.name = "%s"' % name
        print '    self.sons = ast_parse.prune_sons([%s])' % (
                ', '.join(son_parsers))
        print

if __name__ == '__main__':
    main()

