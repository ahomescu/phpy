import sys
import antlr3
import antlr3.tree
import PhpLexer
import PhpParser

char_stream = antlr3.ANTLRInputStream(sys.stdin)
lexer = PhpLexer.PhpLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = PhpParser.PhpParser(tokens)

r = parser.program()
print r.tree.toStringTree()

