
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

# Auto-generated classes
class BinaryConcat:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class NotIdentical:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class StaticClassConstant:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

class Self:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class StaticMinus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

class Var:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_scope, ast_parse.REF])])

class ClassNameRefStatic:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Public:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class InstanceOf:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node])])

class Dec:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class MethodCallSimple:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class Parent:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class ObjAccessSimple:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node])])

class FunCallVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class CName:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class AssignConcat:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ArrayExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr])])

class Mod:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ClassConstants:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_class_constant, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class EmptyStmt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class While:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node])])

class OArrayAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION, ast_parse.BRACKET])])

class MethodC:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class CaseList:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok])])

class Declare:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_declare, ast_parse.COMMA_LIST, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node])])

class FinalDef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_info])])

class Guil:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class VModifiers:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.WRAP, ast_parse.LIST])])

class OName:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class OrBool:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class AndBool:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class For:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_expr, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[6], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[7], [ast_parse.parse_expr, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[8], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[9], [ast_parse.parse_node])])

class ArrayArrowExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr])])

class StaticArrayArrow:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class StaticArray:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class EDots:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_info])])

class ObjAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_obj_access])])

class FunctionC:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class PreProcess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.WRAP])])

class Line:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Identical:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class C:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class ClassDef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_class_def])])

class CondExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_expr])])

class StmtList:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.LIST])])

class OBraceAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.BRACE])])

class HereDoc:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class NotEq:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ArrayArrowRef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_lvalue])])

class CastUnset:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class ObjProp:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Binary:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.WRAP]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr])])

class BackQuote:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class AssignOpArith:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Exit:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION, ast_parse.PAREN, ast_parse.OPTION])])

class ClassConstant:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

class Method:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_method_def])])

class DecLeft:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class VBrace:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.BRACE])])

class GlobalDollar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue])])

class InlineHtml:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class Default:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node, ast_parse.LIST])])

class Require:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class ClassAbstract:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class ArgRef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue])])

class Switch:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node])])

class StaticMethodCallSimple:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class Sc:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class StaticArraySingle:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Lambda:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lambda_def])])

class And:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ClassNameRefDynamic:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_obj_prop_access, ast_parse.LIST])])

class DecRight:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Int:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class Dollar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class Inf:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class HintArray:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class Inc:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class EncapsCurly:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class Xor:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ArrayTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ParenExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr, ast_parse.PAREN])])

class Lv:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue])])

class ColonStmt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok])])

class ListList:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class AndLog:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Return:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class ClassDefNested:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class OrLog:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class UnBang:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Isset:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class MethodBody:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.LIST, ast_parse.BRACE])])

class Continue:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class ArrayRef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue])])

class VQualifier:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue])])

class EncapsDollarCurly:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class AssignRef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_lvalue])])

class IncludeOnce:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class File:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Plus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ListEmpty:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class If:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_elseif, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_else, ast_parse.OPTION])])

class ClassVariables:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_class_variable, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok])])

class UnTilde:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class StaticVars:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_static_var, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class FuncDef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_func_def])])

class Include:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class Final:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Qualifier:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class ObjPropVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue])])

class Stmt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Or:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Eval:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.PAREN])])

class ClassFinal:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class InfEq:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class StringTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class EncapsString:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class Try:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.LIST, ast_parse.BRACE]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_catch]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_catch, ast_parse.LIST])])

class Protected:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Div:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Minus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class VBraceAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.BRACE])])

class ClassC:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class VArrayAccess:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION, ast_parse.BRACKET])])

class Arg:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr])])

class FunCallSimple:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class NotParsedCorrectly:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_info, ast_parse.LIST])])

class ExprStmt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok])])

class GlobalVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Foreach:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_foreach_variable_or_lvalue]), ast_parse.parse_with_options(ast_node[6], [ast_parse.parse_foreach_arrow, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[7], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[8], [ast_parse.parse_node])])

class Sup:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Print:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class Mul:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Echo:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class AssignList:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_expr])])

class DName:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class Infix:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.WRAP]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue])])

class Throw:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class This:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class Block:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.LIST, ast_parse.BRACE])])

class Abstract:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Logical:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class UseDirect:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class Unary:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node, ast_parse.WRAP]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class Globals:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class Static:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class DoubleTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Eq:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Use:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class ObjectTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class LexicalVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_is_ref]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

class Empty:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue, ast_parse.PAREN])])

class TypedDeclaration:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok_expr, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok])])

class AssignOp:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.WRAP]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr])])

class Arith:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class StaticConstant:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Break:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class ClassRegular:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class IntTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class OBrace:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_expr, ast_parse.BRACE])])

class UseParen:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP, ast_parse.PAREN])])

class InterfaceDef:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_interface_def])])

class SingleStmt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class RequireOnce:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class BoolTy:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class ListVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue])])

class EncapsExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class UnPlus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Assign:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_expr])])

class SupEq:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class IfColon:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_new_elseif, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[6], [ast_parse.parse_new_else, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[7], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[8], [ast_parse.parse_tok])])

class Hint:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class EncapsVar:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue])])

class StaticPlus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

class AssignNew:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[6], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN, ast_parse.OPTION])])

class New:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN, ast_parse.OPTION])])

class FuncDefNested:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class NoModifiers:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class Do:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_expr, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_tok])])

class UnMinus:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Halt:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_string, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class Clone:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class InterfaceDefNested:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_node])])

class Case:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_node, ast_parse.LIST])])

class Name:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class AbstractMethod:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok])])

class Postfix:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.WRAP])])

class Double:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class XorLog:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class Cast:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok, ast_parse.WRAP]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class Unset:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_lvalue, ast_parse.COMMA_LIST, ast_parse.PAREN]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_tok])])

class String:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_string, ast_parse.WRAP])])

class CaseColonList:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_tok, ast_parse.OPTION]), ast_parse.parse_with_options(ast_node[3], [ast_parse.parse_node, ast_parse.LIST]), ast_parse.parse_with_options(ast_node[4], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[5], [ast_parse.parse_tok])])

class ConsArray:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node, ast_parse.COMMA_LIST, ast_parse.PAREN])])

class Private:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([])

class At:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr])])

class GlobalDollarExpr:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_tok]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_expr, ast_parse.BRACE])])

class Indirect:
  def __init__(self, ast_node):
    self.sons = ast_parse.prune_sons([ast_parse.parse_with_options(ast_node[1], [ast_parse.parse_lvalue]), ast_parse.parse_with_options(ast_node[2], [ast_parse.parse_node])])

