grammar Php;

options {
  output = AST;
  ASTLabelType = CommonTree;
  language = Python;
}

tokens {
  Call;
  CallerObject;
  Parameter;
  AbstractMethod;
  Reference;
  Modifiers;
  Block;
  EvalExpr;
  Pre;
  Post;
  Variable;
  ArrayEnd;
  Index;
  UnaryMinus;
}

program
  : PHP_START top_statement* PHP_END -> top_statement*
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
  : KW_FUNCTION is_ref? name=ID LPAREN formal_parameter_list? RPAREN
    LBRACE statement* RBRACE -> ^(KW_FUNCTION $name
      is_ref? formal_parameter_list? statement*)
  ;

formal_parameter_list
  : formal_parameter (COMMA formal_parameter)*
      -> formal_parameter+
  ;

formal_parameter
  : is_ref? DOLLAR ID -> ^(Parameter ID is_ref?)
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
  : method_mod_list KW_FUNCTION is_ref? name=ID
      LPAREN formal_parameter_list? RPAREN method_body
      -> ^(KW_FUNCTION $name method_mod_list is_ref?
                        formal_parameter_list? method_body)
  ;

method_mod_list
  : method_mod+ -> ^(Modifiers method_mod+)
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
  : AND -> Reference
  ;

method_body
  : SEMICOLON -> AbstractMethod
  | LBRACE statement* RBRACE -> statement*
  ;

statement
  : if_statement
  | while_statement
  | echo_statement
  | return_statement
  | KW_BREAK SEMICOLON        -> KW_BREAK
  | KW_CONTINUE SEMICOLON     -> KW_CONTINUE
  | LBRACE statement+ RBRACE  -> ^(Block statement+)
  | expr SEMICOLON            -> ^(EvalExpr expr)
  ;

if_statement
  : KW_IF LPAREN expr RPAREN s1=statement ((KW_ELSE) => KW_ELSE s2=statement)?
      -> ^(KW_IF expr $s1 $s2?)
  ;

while_statement
  : KW_WHILE LPAREN expr RPAREN statement -> ^(KW_WHILE expr statement)
  ;

echo_statement
  : KW_ECHO expr SEMICOLON -> ^(KW_ECHO expr)
  ;

return_statement
  : KW_RETURN expr? SEMICOLON -> ^(KW_RETURN expr?)
  ;

expr
  : expr_assign
  ;

expr_assign
  : (indexed_variable assign_op) =>
     indexed_variable assign_op expr_assign
      -> ^(assign_op indexed_variable expr_assign)
  | logical_or
  ;

assign_op
  : EQ
  | PLUS_EQ
  | MINUS_EQ
  | MUL_EQ
  | DIV_EQ
  | DOT_EQ
  | MOD_EQ
  | AND_EQ
  | OR_EQ
  | XOR_EQ
  | SHL_EQ
  | SHR_EQ
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
  : NOT^ fact
  | expr_instanceof
  ;

expr_instanceof
  : (expr_cast KW_INSTANCEOF) => expr_cast KW_INSTANCEOF class_name
      -> ^(KW_INSTANCEOF expr_cast class_name)
  | expr_cast
  ;

expr_cast
  : expr_incdec
  | NEG^ expr_incdec
  | MINUS expr_incdec -> ^(UnaryMinus expr_incdec)
  ;

expr_incdec
  : incdec_op variable_or_call_list -> ^(Pre variable_or_call_list incdec_op)
  | variable_or_call_list 
         (incdec_op -> ^(Post variable_or_call_list incdec_op)
         |          -> variable_or_call_list)
  | atom
  ;

incdec_op
  : INCR
  | DECR
  ;

atom
  : LPAREN expr RPAREN -> expr
  | L_INT
  | L_STRING
  | KW_TRUE
  | KW_FALSE
  | new_object
  ;

new_object
  : KW_NEW class_name LPAREN actual_parameter_list? RPAREN
      -> ^(KW_NEW class_name actual_parameter_list?)
  ;

variable_or_call_list
  : variable_or_call (OBJ_ACCESS^ variable_or_call)*
  ;

variable_or_call
  : indexed_variable
  | indexed_function_call
  ;

indexed_function_call
  : name=ID LPAREN actual_parameter_list? RPAREN call_result_index* ->
    ^(Call $name actual_parameter_list? call_result_index*) ;

actual_parameter_list
  : actual_parameter (COMMA actual_parameter)*
    -> actual_parameter+
  ;

actual_parameter
  : expr -> ^(Parameter expr)
  ;

indexed_variable
  : variable_name variable_index* -> ^(Variable variable_name variable_index*)
  ;

call_result_index
  : LBRACKET expr RBRACKET -> ^(Index expr)
  | LBRACKET RBRACKET -> ^(Index ArrayEnd)
  ;

variable_index
  : call_result_index
  | LBRACE expr RBRACE -> ^(Index expr)
  ;

variable_name
  : DOLLAR^ ID
  | DOLLAR^ variable_name
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
KW_ECHO: 'echo' ;
KW_CONST: 'const';
KW_INSTANCEOF: 'instanceof';
KW_NEW: 'new';
KW_BREAK: 'break';
KW_CONTINUE: 'continue';
KW_RETURN: 'return';

PHP_START: '<?php' ;
PHP_END: '?>' ;

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
LBRACKET: '[' ;
RBRACKET: ']' ;
DOLLAR: '$' ;
COLON: ':' ;
SEMICOLON: ';' ;
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
fragment SINGLE_QUOTE: '\'';
fragment DOUBLE_QUOTE: '"' ;

WHITESPACE: (' ' | '\t') { $channel = HIDDEN; };
NEWLINE: ('\r')? ('\n') { $channel = HIDDEN; };

