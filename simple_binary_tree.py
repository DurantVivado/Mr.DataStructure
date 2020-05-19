'''
classic simple binary tree model
@author: Durant
@email: durant2019@hust.edu.cn
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Linked_binary_Tree:
    def __init__(self,root_data):
        self.root = Node(root_data)

    def insert_left(self,pre_node,left_data):
        #insert one particular node at the left side
        left_node = Node(left_data)
        if pre_node.left_child == None:
           pre_node.left_child = left_node
        else:
            pre_node.left_child.data = left_data
    
    def insert_right(self,pre_node,right_data):
        #insert one particular node at the right side
        right_node = Node(right_data)
        if pre_node.right_child == None:
           pre_node.right_child = right_node
        else:
            pre_node.right_child.data = right_data