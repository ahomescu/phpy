
import sys
import json

import ast_nodes

LIST, PAREN, BRACE, COMMA_LIST, OPTION, BRACKET, WRAP, REF = (
        1, 2, 4, 8, 16, 32, 64, 128)

IGNORE_NODE = -1

def prune_sons(sons):
    return [x for x in sons if x != IGNORE_NODE]

def parse_with_options(ast_node, opts):
    if len(opts) == 1:
        return opts[0](ast_node)

    opt, rest_opts = opts[-1], opts[:-1]
    if opt == LIST:
        return [parse_with_options(x, rest_opts) for x in ast_node]
    elif opt == COMMA_LIST:
        return [parse_with_options(x[1], rest_opts) for x in ast_node
                if x[0] == "Left"]
    elif opt == OPTION:
        if not ast_node or ast_node[0] != "Some":
            return []
        return parse_with_options(ast_node[1], rest_opts)
    elif opt == WRAP:
        return parse_with_options(ast_node[0], rest_opts)
    else:
        # PAREN, BRACE, BRACKET, REF
        return parse_with_options(ast_node[1], rest_opts)

def parse_tok(ast_node):
    # TODO: is this correct?
    return IGNORE_NODE

def parse_string(ast_node):
    return ast_node

def parse_info(ast_node):
    return IGNORE_NODE

def parse_scope(ast_node):
    return IGNORE_NODE

def parse_expr(ast_node):
    # skip the information
    return parse_node(ast_node[0])

def parse_lvalue(ast_node):
    # skip the information
    return parse_node(ast_node[0])

def parse_lexical_vars(ast_node):
    res = [parse_tok(ast_node[0]),
           parse_with_options(ast_node[1],
                [parse_node, COMMA_LIST, PAREN])]
    return prune_sons(res)

def parse_lambda_def(ast_node):
    res = [parse_is_ref(ast_node['l_ref']),
           parse_tok(ast_node['l_tok']),
           parse_with_options(ast_node['l_params'],
               [parse_parameter, COMMA_LIST, PAREN]),
           parse_with_options(ast_node['l_use'],
               [parse_lexical_vars, OPTION]),
           parse_with_options(ast_node['l_body'],
               [parse_node, LIST, BRACE])]
    return prune_sons(res)

def parse_obj_access(ast_node):
    res = [parse_tok(ast_node[0]),
           parse_node(ast_node[1]),
           parse_with_options(ast_node[2],
           [parse_node, COMMA_LIST, PAREN, OPTION])]
    return prune_sons(res)

def parse_obj_prop_access(ast_node):
    return ast_nodes.ObjPropAccess(ast_node)

def parse_elseif(ast_node):
    return ast_nodes.ElseIf(ast_node)

def parse_else(ast_node):
    return ast_nodes.Else(ast_node)

def parse_new_elseif(ast_node):
    return ast_nodes.New_ElseIf(ast_node)

def parse_new_else(ast_node):
    return ast_nodes.New_Else(ast_node)

def parse_is_ref(ast_node):
    if ast_node and ast_node[0] and ast_node[0][0] == "Some":
        return True
    return False

def parse_foreach_variable(ast_node):
    res = [parse_is_ref(ast_node[0]), parse_lvalue(ast_node[1])]
    return prune_sons(res)

def parse_foreach_variable_or_lvalue(ast_node):
    if ast_node[0] == "Left":
        return parse_foreach_variable(ast_node[1])
    if ast_node[0] == "Right":
        return parse_lvalue(ast_node[1])
    print 'Expected "Left" or "Right" at node "%s", skipping' % ast_node[0]
    return IGNORE_NODE

def parse_foreach_arrow(ast_node):
    res = [parse_tok(ast_node[0]), parse_foreach_variable(ast_node[1])]
    return prune_sons(res)

def parse_tok_node_pair(ast_node):
    res = [parse_tok(ast_node[0]), parse_node(ast_node[1])]
    return prune_sons(res)

def parse_class_name_ref_dynamic(ast_node):
    res = [parse_lvalue(ast_node[0]), 
           parse_with_options(ast_node[1],
                [parse_obj_prop_access, LIST])]
    return prune_sons(res)

def parse_node_node_pair(ast_node):
    res = [parse_node(ast_node[0]), parse_node(ast_node[1])]
    return prune_sons(res)

def parse_catch(ast_node):
    return ast_nodes.Catch(ast_node)

def parse_declare(ast_node):
    res = [parse_node(ast_node[0]), parse_static_scalar_effect(ast_node[1])]
    return prune_sons(res)

def parse_tok_expr_pair(ast_node):
    res = [parse_tok(ast_node[0]), parse_expr(ast_node[1])]
    return prune_sons(res)

def parse_static_var(ast_node):
    res = [parse_node(ast_node[0]),
           parse_with_options(ast_node[1],
                [parse_static_scalar_effect, OPTION])]
    return prune_sons(res)

def parse_static_scalar_effect(ast_node):
    # NOTE: ast_node[0] is token info
    return parse_node(ast_node[1])

def parse_parameter(ast_node):
    return ast_nodes.Parameter([
        ast_node['p_type'], ast_node['p_ref'],
        ast_node['p_name'], ast_node['p_default']])

def parse_func_def(ast_node):
    res = [parse_is_ref(ast_node['f_ref']),
           parse_tok(ast_node['f_tok']),
           parse_node(ast_node['f_name']),
           parse_with_options(ast_node['f_params'],
               [parse_parameter, COMMA_LIST, PAREN]),
           parse_with_options(ast_node['f_return_type'],
               [parse_node, OPTION]),
           parse_with_options(ast_node['f_body'],
               [parse_node, LIST, BRACE])]
    return prune_sons(res)

def parse_interface(ast_node):
    # NOTE: ast_node[0] is token info
    return parse_with_options(ast_node[1],
            [parse_node, COMMA_LIST])

def parse_class_def(ast_node):
    res = [parse_node(ast_node['c_type']),
           parse_node(ast_node['c_name']),
           parse_with_options(ast_node['c_extends'],
               [parse_tok_node_pair, OPTION]),
           parse_with_options(ast_node['c_implements'],
               [parse_interface, OPTION]),
           parse_with_options(ast_node['c_body'],
               [parse_node, LIST, BRACE])]
    return prune_sons(res)

def parse_class_constant(ast_node):
    res = [parse_node(ast_node[0]),
           parse_static_scalar_effect(ast_node[1])]
    return prune_sons(res)

def parse_class_variable(ast_node):
    res = [parse_node(ast_node[0]),
           parse_with_options(ast_node[1],
                [parse_static_scalar_effect, OPTION])]
    return prune_sons(res)

def parse_method_def(ast_node):
    res = [parse_with_options(ast_node['m_modifiers'],
                [parse_node, WRAP, LIST]),
           parse_tok(ast_node['m_tok']),
           parse_is_ref(ast_node['m_ref']),
           parse_node(ast_node['m_name']),
           parse_with_options(ast_node['m_params'],
                [parse_parameter, COMMA_LIST, PAREN]),
           parse_with_options(ast_node['m_return_type'],
                [parse_node, OPTION]),
           parse_node(ast_node['m_body'])]
    return prune_sons(res)

def parse_interface_def(ast_node):
    res = [parse_node(ast_node['i_name']),
           parse_with_options(ast_node['i_extends'],
               [parse_interface, OPTION]),
           parse_with_options(ast_node['i_body'],
               [parse_node, LIST, BRACE])]
    return prune_sons(res)

def parse_node(ast_node):
    node_constructor = getattr(sys.modules["ast_nodes"], ast_node[0], None)
    if not node_constructor:
        print 'Unknown node "%s", skipping' % ast_node[0]
        return IGNORE_NODE
    return node_constructor(ast_node)

def parse_program(ast_node):
    return prune_sons([parse_node(x) for x in ast_node])

# Main function for module, call this with JSON file contents
def parse_json_program(s):
    return parse_program(json.loads(s))


