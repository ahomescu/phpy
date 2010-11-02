tree grammar PhpTree;

options {
  tokenVocab = Php;
  ASTLabelType = CommonTree;
  language = Python;
}

@header {
  import sys
}

@members {
  indentLevel = 0
  was_indent = False
  was_newline = False

  def indent(self):
    self.indentLevel += 1

  def unindent(self):
    self.indentLevel -= 1

  def print_indent(self):
    if self.was_indent:
      return
    sys.stdout.write(self.indentLevel * 2 * ' ')
    self.was_indent = True
    self.was_newline = False

  def print_newline(self):
    if self.was_newline:
      return
    sys.stdout.write('\n')
    self.was_newline = True
    self.was_indent = False

  def print_custom(self, str):
    sys.stdout.write(str)
    self.was_newline = False
    self.was_indent = False
}

program
@init {
  print 'import sys'
  print ''
  print 'def array(x):'
  print '  return [x]'
  print ''
  print 'def count(x):'
  print '  return len(x)'
  print ''
} : top_statement*
  ;

top_statement
@init {
  self.print_indent()
}
@after {
  self.print_newline()
} : statement
  | function_def
  | class_def
  | interface_def
  ;

function_def
@init {
  param_list = []
} : ^(KW_FUNCTION name=ID
      {
        self.print_indent()
        self.print_custom('def ' + $name.text + '(')
      }
      (^(Parameter pname=ID { param_list.append($pname.text) }))*
      {
        self.print_custom(','.join(param_list))
        self.print_custom('):')
        self.print_newline()
        self.indent()
      }
      statement*)
      {
        self.unindent()
        self.print_indent()
        self.print_newline()
      }
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
@init {
  self.print_indent()
}
@after {
  self.print_newline()
} : ^(EvalExpr expr)
  | ^(Block statement+)
  | if_statement
  | while_statement
  | echo_statement
  | KW_BREAK { self.print_custom($KW_BREAK.text) }
  | KW_CONTINUE { self.print_custom($KW_CONTINUE.text) }
  ;

if_statement
  : ^(KW_IF
      {
        self.print_custom('if ')
      }
      cond=expr
      {
        self.print_custom(':')
        self.print_newline()
        self.indent()
      }
      true_stat=statement
      false_stat=statement?)
      {
        self.unindent()
      }
  ;

while_statement
  : ^(KW_WHILE
      {
        self.print_custom('while ')
      }
      expr
      {
        self.print_custom(':')
        self.print_newline()
        self.indent()
      }
      statement)
      {
        self.unindent()
      }
  ;

echo_statement
  : ^(KW_ECHO { self.print_custom('sys.stdout.write(str(') } expr { self.print_custom('))') })
  ;

incdec_op
  : INCR
  | DECR
  ;

expr
  : ^(EQ expr { self.print_custom(' = ') } expr)
  | ^(PLUS_EQ expr { self.print_custom(' += ') } expr)
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
  | ^(IS_EQ expr { self.print_custom(' == ') } expr)
  | ^(IS_NEQ expr { self.print_custom(' != ') } expr)
  | ^(IS_IDENT expr expr)
  | ^(IS_NIDENT expr expr)
  | ^(IS_LE expr { self.print_custom(' <= ') } expr)
  | ^(IS_GE expr { self.print_custom(' >= ') } expr)
  | ^(IS_LT expr { self.print_custom(' < ') } expr)
  | ^(IS_GT expr { self.print_custom(' > ') } expr)
  | ^(SHL expr expr)
  | ^(SHR expr expr)
  | ^(PLUS expr { self.print_custom(' + ') } expr)
  | ^(MINUS expr expr)
  | ^(DOT
      { self.print_custom('str(') }
      expr
      { self.print_custom(') + str(') }
      expr
      { self.print_custom(')') })
  | ^(MUL expr expr)
  | ^(DIV expr expr)
  | ^(MOD expr { self.print_custom(' \% ') } expr)
  | ^(NOT expr)
  | ^(KW_INSTANCEOF expr class_name)
  | ^(UnaryMinus expr)
  | ^(NEG expr)
  | ^(Pre expr incdec_op)
  | ^(Post expr incdec_op)
  | L_INT { self.print_custom($L_INT.text) }
  | L_STRING { self.print_custom($L_STRING.text) }
  | KW_TRUE
  | KW_FALSE
  | ^(OBJ_ACCESS variable_or_call variable_or_call)
  | ^(KW_NEW class_name actual_parameter_list?)
  | ^(Call name=ID { self.print_custom($ID.text + '(') }
      actual_parameter_list
      { self.print_custom(')') }
      index*)
  | ^(Variable variable_name index*)
  ;

actual_parameter_list
  : (^(Parameter expr))+
  ;

index
  : ^(Index ArrayEnd
      {
        # TODO - hard
        self.print_custom('[-1]')
      })
  | ^(Index
      {
        self.print_custom('[')
      }
      expr
      {
        self.print_custom(']')
      })
  ;

variable_or_call
  : ^(Variable variable_name index*)
  | ^(Call name=ID actual_parameter_list? index*)
  ;

variable_name
  : ^(DOLLAR ID { self.print_custom($ID.text) })
  | ^(DOLLAR variable_name)
  | ^(DOLLAR expr)
  ;
