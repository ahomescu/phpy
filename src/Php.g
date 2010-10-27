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
}

program
  : statement+
  ;

variable
  : DOLLAR^ ID
  | DOLLAR^ variable
  | DOLLAR^ LBRACE! expr RBRACE!
  ;

statement
  : expr SEMICOLON!
  | LBRACE! statement+ RBRACE!
  | if_statement
  | while_statement
  | function_def
  ;

function_def
  : KW_FUNCTION! ID LPAREN! (DOLLAR! ID (COMMA! DOLLAR! ID)*)? RPAREN!
    LBRACE! statement* RBRACE!
  ;

if_statement
  : KW_IF LPAREN! expr RPAREN! statement ((KW_ELSE) => KW_ELSE statement)?
  ;

while_statement
  : KW_WHILE LPAREN! expr RPAREN! statement
  ;

expr
  : (variable EQ) => assignment
  | logical
  ;

assignment
  : variable EQ^ expr
  ;

logical
  : comp ((LOG_AND | LOG_OR) =>
    (LOG_AND^ | LOG_OR^) comp)*
  ;

comp
  : concat ((IS_LE | IS_GE | IS_EQ | IS_LT | IS_GT) =>
    (IS_LE^ | IS_GE^ | IS_EQ^ | IS_LT^ | IS_GT^) concat)*
  ;

concat
  : sum ((DOT) => DOT^ sum)*
  ;

sum
  : term ((PLUS | MINUS) => (PLUS | MINUS)^ term)*
  ;

term
  : fact ((MUL | DIV) => (MUL^ | DIV^) fact)*
  ;

fact
  : (((atom OBJ_ACCESS) => call_chain) | atom)
  ;

call_chain
  : (atom d1=OBJ_ACCESS call_tail ->
    ^($d1 ^(CallerObject atom) call_tail))
    ((OBJ_ACCESS) => d2=OBJ_ACCESS t=call_tail ->
    ^($d2 ^(CallerObject $call_chain) $t))*
  ;

atom
  : LPAREN! expr RPAREN!
  | L_INT
  | L_STRING
  | KW_TRUE
  | KW_FALSE
  | (ID LPAREN) => call_tail -> ^(SimpleCall call_tail) 
  | variable
  ;

call_tail
  : ID LPAREN (expr (COMMA expr)*)? RPAREN ->
    ^(Name ID) ^(LPAREN (expr+)?) ;

/**
* Lexer
*/

KW_FUNCTION : 'function' ;
KW_CLASS: 'class' ;
// TODO: de-uglify with a token filter
KW_TRUE: ('t' | 'T') ('r' | 'R') ('u' | 'U') ('e' | 'E') ;
KW_FALSE: ('f' | 'F') ('a' | 'A') ('l' | 'L') ('s' | 'S') ('e' | 'E') ;
KW_IF: 'if' ;
KW_ELSE: 'else' ;
KW_WHILE: 'while' ;

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
IS_EQ: '==' ;
IS_NEQ: '!=' ;
IS_LE: '<=' ;
IS_LT: '<' ;
IS_GE: '>=' ;
IS_GT: '>' ;
LOG_AND: '&&' ;
LOG_OR: '||' ;
EQ: '=' ;
NOT: '!' ;
fragment ESC_SEQ
  : '\\' .
  ;
