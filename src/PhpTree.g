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
  VAR_PREFIX = 'v_'
  TEMP_PREFIX = 't_'
  
  indentLevel = 0
  was_indent = False
  was_newline = False
  next_temp = 0

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

  def print_line(self, str):
    self.print_indent()
    self.print_custom(str)
    self.print_newline()

  def get_temp(self):
    tmp = '\%s\%d' \% (self.TEMP_PREFIX, self.next_temp)
    self.next_temp += 1
    return tmp
}

program
@init {
  print 'import sys'
  print ''
  print 'def array(x):'
  print '  return [[[x]]]'
  print ''
  print 'def count(x):'
  print '  return [len(x)]'
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
  : if_statement
  | while_statement
  | echo_statement
  | KW_BREAK { self.print_line('break') }
  | KW_CONTINUE { self.print_line('continue') }
  | ^(Block statement+)
  | ^(EvalExpr expr)
  ;

if_statement
  : ^(KW_IF
      cond=expr {
        self.print_line('if \%s:' \% $cond.val)
        self.indent()
      } true_stat=statement
      ({
        self.unindent()
        self.print_line('else:')
        self.indent()
      } false_stat=statement)? { self.unindent() })
  ;

while_statement
  : ^(KW_WHILE
      {
        self.print_line('while True:')
        self.indent()
      }
      cond=expr {
        self.print_line('if not \%s:' \% $expr.val)
        self.indent()
        self.print_line('break')
        self.unindent()
      } statement { self.unindent() })
  ;

echo_statement
  : ^(KW_ECHO expr { self.print_line('sys.stdout.write(\%s)' \% $expr.val) })
  ;

assign_op returns [op]
  : PLUS_EQ { $op = '+' }
  | MINUS_EQ { $op = '-' }
  | MUL_EQ { $op = '*' }
  | DIV_EQ { $op = '/' } // TODO: figure whether to use / or //
  | MOD_EQ { $op = '\%' }
  | AND_EQ { $op = '&' }
  | OR_EQ { $op = '|' }
  | XOR_EQ { $op = '^' }
  | SHL_EQ { $op = '<<' }
  | SHR_EQ { $op = '>>' }
  ;

incdec_op returns [op]
  : INCR { $op = '+' }
  | DECR { $op = '-' }
  ;

expr returns [val]
  : ^(EQ 
    voc=variable_or_call e=expr
    { 
      self.print_line('\%s[0] = \%s' \% ($voc.tmp, $e.val))
      $val = '\%s[0]' \% $voc.tmp
    })
  | ^(DOT_EQ
    voc=variable_or_call expr
    {
      self.print_line('\%s[0] = str(\%s[0]) + str(\%s)' \% ($voc.tmp, $voc.tmp, $e.val))
      $val = '\%s[0]' \% $voc.tmp
    })
  | ^(assign_op voc=variable_or_call expr
    {
      self.print_line('\%s[0] = \%s[0] \%s \%s' \% ($voc.tmp, 
                        $voc.tmp, $assign_op.op, $e.val))
      $val = '\%s[0]' \% $voc.tmp
    })
  | ^(LOG_OR { $val = '(\%s or \%s)' \% ($e1.val, $e2.val) })
  | ^(LOG_AND { $val = '(\%s and \%s)' \% ($e1.val, $e2.val) })
  | ^(OR { $val = '(\%s | \%s)' \% ($e1.val, $e2.val) })
  | ^(XOR { $val = '(\%s ^ \%s)' \% ($e1.val, $e2.val) })
  | ^(AND { $val = '(\%s & \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_EQ e1=expr e2=expr { $val = '(\%s == \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_NEQ e1=expr e2=expr { $val = '(\%s != \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_IDENT expr expr)
  | ^(IS_NIDENT expr expr)
  | ^(IS_LE e1=expr e2=expr { $val = '(\%s <= \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_GE e1=expr e2=expr { $val = '(\%s >= \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_LT e1=expr e2=expr { $val = '(\%s < \%s)' \% ($e1.val, $e2.val) })
  | ^(IS_GT e1=expr e2=expr { $val = '(\%s > \%s)' \% ($e1.val, $e2.val) })
  | ^(SHL { $val = '(\%s << \%s)' \% ($e1.val, $e2.val) })
  | ^(SHR { $val = '(\%s >> \%s)' \% ($e1.val, $e2.val) })
  | ^(PLUS e1=expr e2=expr  { $val = '(\%s + \%s)' \% ($e1.val, $e2.val) })
  | ^(MINUS e1=expr e2=expr { $val = '(\%s - \%s)' \% ($e1.val, $e2.val) })
  | ^(DOT e1=expr e2=expr { $val = '(str(\%s) + str(\%s))' \% ($e1.val, $e2.val) })
  | ^(MUL e1=expr e2=expr { $val = '(\%s * \%s)' \% ($e1.val, $e2.val) })
  | ^(DIV e1=expr e2=expr { $val = '(\%s / \%s)' \% ($e1.val, $e2.val) })
  | ^(MOD e1=expr e2=expr { $val = '(\%s \%\% \%s)' \% ($e1.val, $e2.val) })
  | ^(NOT expr)
  | ^(KW_INSTANCEOF expr class_name)
  | ^(UnaryMinus expr)
  | ^(NEG expr)
  | L_INT { $val = $L_INT.text }
  | L_STRING { $val = $L_STRING.text }
  | KW_TRUE { $val = "True" }
  | KW_FALSE { $val = "False" }
  | ^(KW_NEW class_name actual_parameter_list?)
  | voc=variable_or_call { $val = '\%s[0]' \% $voc.tmp }
  | ^(Pre voc=variable_or_call incdec_op
    {
      self.print_line('\%s[0] = \%s[0] \%s 1' \% ($voc.tmp, 
                        $voc.tmp, $incdec_op.op))
      $val = '\%s[0]' \% $voc.tmp
    })
  | ^(Post voc=variable_or_call incdec_op
    {
      $val = self.get_temp()
      self.print_line('\%s = \%s[0]' \% ($val, $voc.tmp))
      self.print_line('\%s[0] = \%s[0] \%s 1' \% ($voc.tmp, 
                        $voc.tmp, $incdec_op.op))
    })
  ;

variable_or_call returns [tmp]
  : ^(Call name=ID apl=actual_parameter_list 
    { indexed_val = '\%s(\%s)' \% ($name.text, $apl.params_list) } 
    (index[indexed_val] { indexed_val = '\%s[0][\%s]' \% (indexed_val, $index.idx) })* 
    {
      $tmp = self.get_temp()
      self.print_line('\%s = \%s' \% ($tmp, indexed_val)) 
    })
  | ^(Variable variable_name { indexed_val = $variable_name.tmp } 
    (index[indexed_val] { indexed_val = '\%s[0][\%s]' \% (indexed_val, $index.idx) })*)
    {
      $tmp = self.get_temp()
      self.print_line('\%s = \%s' \% ($tmp, indexed_val)) 
    }
  | ^(OBJ_ACCESS variable_or_call variable_or_call)
  ;

actual_parameter_list returns [params_list]
  // TODO: actually push references to parameters
  : { params = [] } (^(Parameter expr { params.append($expr.val) }))+
    { $params_list = ','.join(params) }
  ;

index[vector] returns [idx]
  : ^(Index ArrayEnd
    {
      $idx = self.get_temp()
      self.print_line('\%s = len(\%s[0])' \% ($idx, $vector))
      self.print_line('\%s[0].append([None])' \% $vector)
    })
  | ^(Index expr { $idx = $expr.val })
  ;

variable_name returns [tmp]
  : ^(DOLLAR ID 
    { 
      $tmp = '\%s\%s' \% (self.TEMP_PREFIX, $ID.text)
      self.print_line('try: \%s = \%s\%s' \% ($tmp, self.VAR_PREFIX, $ID.text))
      self.print_line('except NameError: \%s = \%s\%s = [None]' \% ($tmp, 
                        self.VAR_PREFIX, $ID.text))
    })
  | ^(DOLLAR variable_name)
  | ^(DOLLAR expr)
  ;

