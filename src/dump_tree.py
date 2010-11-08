import sys
import antlr3
import antlr3.tree
import PhpLexer
import PhpParser
import PhpTree

char_stream = antlr3.ANTLRInputStream(sys.stdin)
lexer = PhpLexer.PhpLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = PhpParser.PhpParser(tokens)

r = parser.program()
#print r.tree.toStringTree()

root = r.tree
nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
phpTree = PhpTree.PhpTree(nodes)
phpTree.program()
