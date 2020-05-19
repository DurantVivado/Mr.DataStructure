from stack_intro import Stack
'''
This func handles bracketed-pair expression, forging a binary tree accordingly, 
returning the root node.
@author: Durant
@email: durant201@sina.com
'''
def expression_parser_opt(expression):
    
    pStack = Stack()
    tree = Node('')
    pStack.push(tree)# push the root into stack for return
    pres_tree = tree
    for i in expression:
#        print(pStack.size())
        if i == '(':
            pres_tree.left_child = Node('')
            pStack.push(pres_tree)
            pres_tree = pres_tree.left_child
        elif i in op_list:
            if pStack.size() == 0:# two bracket item operation
                new_node = Node(i) 
                new_node.left_child = pres_tree
                new_node.right_child = Node('')
                pStack.push(new_node)
                pres_tree = new_node.right_child
            else:
                pres_tree.data = i
                pres_tree.right_child = Node('')
                pStack.push(pres_tree)
                pres_tree = pres_tree.right_child
        elif i==')':
            pres_tree = pStack.pop()
        else:
            pres_tree.data = i
            parent = pStack.pop()
            pres_tree = parent
    return pres_tree