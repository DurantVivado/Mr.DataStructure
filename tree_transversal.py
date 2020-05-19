'''
three methods of transversing a tree:Preorder, inorder or postorder
Three methods of traversal:
    preorder: root->left->right
    inorder: left->root->right
    postorder: left->right->root
@author: Durant 
@email: durant2019@sina.com
'''
#d = printTree(tr)
def preorder_transversal(tree,last_tree,draw=False,d=None):# for animation, input last_tree
 #if you want to animate the process, use draw = True   
    if tree and last_tree:
        if draw:
            coord1 = d.get_node_coord(last_tree)
            coord2 = d.get_node_coord(tree)
            d.draw_line(coord1,coord2,5,'red')
#            print(tree.data)
        pre_exp.append(tree.data)
        preorder_transversal(tree.left_child,tree)
        preorder_transversal(tree.right_child,tree)
        
            
    
def inorder_transversal(tree,last_tree,draw = False,d=None):
    
    if tree and last_tree:
        inorder_transversal(tree.left_child,tree)
        if draw:
            coord1 = d.get_node_coord(last_tree)
            coord2 = d.get_node_coord(tree)
            d.draw_line(coord1,coord2,5,'red')
#            print(tree.data)
        in_exp.append(tree.data)
        inorder_transversal(tree.right_child,tree)
        
       
def postorder_transversal(tree,last_tree,draw=False,d=None):
    if tree and last_tree:
        postorder_transversal(tree.left_child,tree)
        postorder_transversal(tree.right_child,tree)
        if draw:
            coord1 = d.get_node_coord(last_tree)
            coord2 = d.get_node_coord(tree)
            d.draw_line(coord1,coord2,5,'red')
#        print(tree.data)
        post_exp.append (tree.data)