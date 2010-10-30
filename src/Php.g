grammar Php;

options {
  output = AST;
  ASTLabelType = CommonTree;
  language = Python;
}

tokens {
  SimpleCall;
  Name;
  CallerObject;
  PARAMETER;
  ABSTRACT_METHOD;
  REFERENCE;
  MODIFIERS;
  BLOCK;
  EVAL_EXPR;
  VAR_OR_ASSIGN;
  PRE;
  POST;
}

program
  : top_statement*
  ;

top_statement
  : statement
  | function_def
  | class_def
  | interface_def
  | constant_def
  ;

constant_def
  : KW_CONST constant_decl+ -> ^(KW_CONST constant_decl+);

constant_decl
  : ID EQ const_initializer;

const_initializer
  :
  ;

function_def
  : KW_FUNCTION name=ID LPAREN formal_parameter_list RPAREN
    LBRACE statement* RBRACE -> ^(KW_FUNCTION $name
      formal_parameter_list statement*)
  ;

formal_parameter_list
  : formal_parameter (COMMA formal_parameter_list)?
      -> formal_parameter formal_parameter_list?
  ;

formal_parameter
  : ID -> ^(PARAMETER ID)
  ;

class_def
  : KW_CLASS name=ID extends_from_list? implements_list?
      LBRACE class_statement* RBRACE
      -> ^(KW_CLASS $name extends_from_list?
            implements_list? class_statement*)
  ;

extends_from_list
  : KW_EXTENDS class_name -> ^(KW_EXTENDS class_name)
  ;

implements_list
  : KW_IMPLEMENTS class_name+ -> ^(KW_IMPLEMENTS class_name+)
  ;

interface_def
  : KW_INTERFACE name=ID interface_extends_list?
      LBRACE class_statement* RBRACE
      -> ^(KW_INTERFACE $name interface_extends_list? class_statement*)
  ;

interface_extends_list
  : KW_EXTENDS class_name+ -> ^(KW_EXTENDS class_name+)
  ;

class_name
  : ID
  ;

class_statement
  : constant_def
  | class_method_def
  ;

class_method_def
  : method_mod_list KW_FUNCTION is_ref name=ID
      LPAREN formal_parameter_list RPAREN method_body
      -> ^(KW_FUNCTION $name method_mod_list is_ref
                        formal_parameter_list method_body)
  ;

method_mod_list
  : method_mod+ -> ^(MODIFIERS method_mod+)
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
  | AND -> REFERENCE
  ;

method_body
  : SEMICOLON -> ABSTRACT_METHOD
  | LBRACE statement* RBRACE -> statement*
  ;

statement
  : expr SEMICOLON            -> ^(EVAL_EXPR expr)
  | LBRACE statement+ RBRACE  -> ^(BLOCK statement+)
  | if_statement
  | while_statement
  ;

if_statement
  : KW_IF LPAREN expr RPAREN statement if_else
      -> ^(KW_IF expr statement if_else)
  ;

if_else
  : (KW_ELSE) => KW_ELSE statement -> ^(KW_ELSE statement)
  |
  ;

while_statement
  : KW_WHILE LPAREN expr RPAREN statement -> ^(KW_WHILE expr statement)
  ;

expr
  : expr_assign
  ;

expr_assign
  : logical_or
  | variable op=(PLUS_EQ | MINUS_EQ | MUL_EQ | DIV_EQ | DOT_EQ | MOD_EQ |
                 AND_EQ | OR_EQ | XOR_EQ | SHL_EQ | SHR_EQ) expr_assign
      -> ^($op variable expr_assign)
  ;

logical_or
  : logical_and (LOG_OR^ logical_and)*
  ;

logical_and
  : bitwise_or (LOG_AND^ bitwise_or)*
  ;

bitwise_or
  : bitwise_xor (OR^ bitwise_xor)*
  ;

bitwise_xor
  : bitwise_and (XOR^ bitwise_and)*
  ;

bitwise_and
  : comp_eq (AND^ comp_eq)*
  ;

comp_eq
  : comp_le ((IS_EQ^ | IS_NEQ^ | IS_IDENT^ | IS_NIDENT^) comp_le)*
  ;

comp_le
  : shift ((IS_LE^ | IS_GE^ | IS_LT^ | IS_GT^) shift)*
  ;

shift
  : sum ((SHL^ | SHR^) sum)*
  ;

sum
  : term ((PLUS | MINUS | DOT)^ term)*
  ;

term
  : fact ((MUL^ | DIV^ | MOD^) fact)*
  ;

fact
  : NOT fact
  | expr_instanceof
  ;

expr_instanceof
  : (expr_cast KW_INSTANCEOF) => expr_cast KW_INSTANCEOF class_name
      -> ^(KW_INSTANCEOF expr_cast class_name)
  | expr_cast
  ;

expr_cast
  : expr_incdec
  | NEG expr_incdec
  | MINUS expr_incdec
  ;

expr_incdec
  : op=(INCR | DECR) expr_index -> ^(PRE expr_index $op)
  | (expr_index (INCR | DECR)) =>
      expr_index op=(INCR | DECR) -> ^(POST expr_index $op)
  | expr_index
  ;

expr_index
  : expr_leaf
  ;

expr_leaf
  : (atom OBJ_ACCESS) => call_chain
  | atom
  ;

call_chain
  : (atom d1=OBJ_ACCESS call_tail ->
    ^($d1 ^(CallerObject atom) call_tail))
    ((OBJ_ACCESS) => d2=OBJ_ACCESS t=call_tail ->
    ^($d2 ^(CallerObject $call_chain) $t))*
  ;

atom
  : LPAREN expr RPAREN -> expr
  | L_INT
  | L_STRING
  | KW_TRUE
  | KW_FALSE
  | (ID LPAREN) => call_tail -> ^(SimpleCall call_tail)
  ;

call_tail
  : ID LPAREN (expr (COMMA expr)*)? RPAREN ->
    ^(Name ID) ^(LPAREN (expr+)?) ;

variable
  : DOLLAR^ ID
  | DOLLAR^ variable
  | DOLLAR^ LBRACE! expr RBRACE!
  ;

/**
* Lexer
*/

KW_FUNCTION : 'function' ;
KW_CLASS: 'class' ;
KW_INTERFACE: 'interface';
KW_EXTENDS: 'extends';
KW_IMPLEMENTS: 'implements';
KW_PUBLIC: 'public';
KW_PROTECTED: 'protected';
KW_PRIVATE: 'private';
KW_STATIC: 'static';
KW_ABSTRACT: 'abstract';
KW_FINAL: 'final';
// TODO: de-uglify with a token filter
KW_TRUE: ('t' | 'T') ('r' | 'R') ('u' | 'U') ('e' | 'E') ;
KW_FALSE: ('f' | 'F') ('a' | 'A') ('l' | 'L') ('s' | 'S') ('e' | 'E') ;
KW_IF: 'if' ;
KW_ELSE: 'else' ;
KW_WHILE: 'while' ;
KW_CONST: 'const';
KW_INSTANCEOF: 'instanceof';

ID:
  ('a'..'z'|'A'..'Z'|'_'|'\u007f'..'\u00ff') ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'\u007f'..'\u00ff')*
  ;
L_INT: ('+' | '-')? ('0'..'9')+ ;
L_STRING
  : (DOUBLE_QUOTE ( ESC_SEQ | ~('\\'|'"'|'\n') )* DOUBLE_QUOTE)
  | (SINGLE_QUOTE ( ESC_SEQ | ~('\\'|'\''|'\n') )* SINGLE_QUOTE)
  ;
LPAREN: '(' ;
RPAREN: ')' ;
LBRACE: '{' ;
RBRACE: '}' ;
DOLLAR: '$' ;
COLON: ':' ;
SEMICOLON: ';' ;
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"' ;
OBJ_ACCESS: '->' ;
COMMA: ',' ;
DOT: '.' ;
PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;
AND: '&' ;
XOR: '^' ;
OR: '|' ;
IS_IDENT: '===';
IS_NIDENT: '!==';
IS_EQ: '==' ;
IS_NEQ: '!=' ;
IS_DIFF: '<>';
IS_LE: '<=' ;
IS_LT: '<' ;
IS_GE: '>=' ;
IS_GT: '>' ;
LOG_AND: '&&' ;
LOG_OR: '||' ;
INCR: '++';
DECR: '--';
SHL: '<<' ;
SHR: '>>' ;
EQ: '=' ;
NOT: '!' ;
NEG: '~' ;
PLUS_EQ: '+=' ;
MINUS_EQ: '-=' ;
MUL_EQ: '*=' ;
DIV_EQ: '/=' ;
DOT_EQ: '.=' ;
MOD_EQ: '%=' ;
AND_EQ: '&=' ;
OR_EQ: '|=' ;
XOR_EQ: '^=' ;
SHL_EQ: '<<=' ;
SHR_EQ: '>>=' ;
fragment ESC_SEQ
  : '\\' .
  ;
