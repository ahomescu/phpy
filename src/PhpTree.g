tree grammar PhpTree;

options {
  tokenVocab = Php;
  ASTLabelType = CommonTree;
  language = Python;
}

program
  : top_statement*
  ;

top_statement
  : statement
  | function_def
  | class_def
  | interface_def
  ;

function_def
  : ^(KW_FUNCTION name=ID (^(Parameter ID))* statement*)
  ;

class_def
  : ^(KW_CLASS name=ID extends_from_list? implements_list? class_statement*)
  ;

extends_from_list
  : ^(KW_EXTENDS class_name)
  ;

implements_list
  : ^(KW_IMPLEMENTS class_name+)
  ;

interface_def
  : ^(KW_INTERFACE name=ID interface_extends_list? class_statement*)
  ;

interface_extends_list
  : ^(KW_EXTENDS class_name+)
  ;

class_name
  : ID
  ;

class_statement
  : class_method_def
  ;

class_method_def
  : ^(KW_FUNCTION name=ID method_mod_list is_ref (^(Parameter ID))* method_body)
  ;

method_mod_list
  : ^(Modifiers method_mod+)
  |
  ;

method_mod
  : KW_PUBLIC
  | KW_PROTECTED
  | KW_PRIVATE
  | KW_STATIC
  | KW_ABSTRACT
  | KW_FINAL
  ;

is_ref
  :
  | Reference
  ;

method_body
  : AbstractMethod
  | statement*
  ;

statement
  : ^(EvalExpr expr)
  | ^(Block statement+)
  | if_statement
  | while_statement
  | echo_statement
  | KW_BREAK
  | KW_CONTINUE
  ;

if_statement
  : ^(KW_IF cond=expr true_stat=statement false_stat=statement?)
  ;

while_statement
  : ^(KW_WHILE expr statement)
  ;

echo_statement
  : ^(KW_ECHO expr)
  ;

incdec_op
  : INCR
  | DECR
  ;

expr
  : ^(EQ expr expr)
  | ^(PLUS_EQ expr expr)
  | ^(MINUS_EQ expr expr)
  | ^(MUL_EQ expr expr)
  | ^(DIV_EQ expr expr)
  | ^(DOT_EQ expr expr)
  | ^(MOD_EQ expr expr)
  | ^(AND_EQ expr expr)
  | ^(OR_EQ expr expr)
  | ^(XOR_EQ expr expr)
  | ^(SHL_EQ expr expr)
  | ^(SHR_EQ expr expr)
  | ^(LOG_OR expr expr)
  | ^(LOG_AND expr expr)
  | ^(OR expr expr)
  | ^(XOR expr expr)
  | ^(AND expr expr)
  | ^(IS_EQ expr expr)
  | ^(IS_NEQ expr expr)
  | ^(IS_IDENT expr expr)
  | ^(IS_NIDENT expr expr)
  | ^(IS_LE expr expr)
  | ^(IS_GE expr expr)
  | ^(IS_LT expr expr)
  | ^(IS_GT expr expr)
  | ^(SHL expr expr)
  | ^(SHR expr expr)
  | ^(PLUS expr expr)
  | ^(MINUS expr expr)
  | ^(DOT expr expr)
  | ^(MUL expr expr)
  | ^(DIV expr expr)
  | ^(MOD expr expr)
  | ^(NOT expr)
  | ^(KW_INSTANCEOF expr class_name)
  | ^(UnaryMinus expr)
  | ^(NEG expr)
  | ^(Pre expr incdec_op)
  | ^(Post expr incdec_op)
  | L_INT
  | L_STRING
  | KW_TRUE
  | KW_FALSE
  | ^(OBJ_ACCESS variable_or_call variable_or_call)
  | ^(KW_NEW class_name actual_parameter_list?)
  | ^(Call name=ID actual_parameter_list index*)
  | ^(Variable variable_name index*)
  ;

actual_parameter_list
  : (^(Parameter expr))+
  ;

index
  : ^(Index ArrayEnd)
  | ^(Index expr)
  ;

variable_or_call
  : ^(Variable variable_name index*)
  | ^(Call name=ID actual_parameter_list? index*)
  ;

variable_name
  : ^(DOLLAR ID)
  | ^(DOLLAR variable_name)
  | ^(DOLLAR expr)
  ;
