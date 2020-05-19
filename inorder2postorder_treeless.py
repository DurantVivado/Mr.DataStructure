'''
RPN: Reverse Polish Notation
transform inorder to postorder expression
@author: Durant
@email: durant2019@sina.com
'''
from stack_intro import Stack
from memory_profiler import profile #memory recorder
from queue_intro import Queue
from expression_spliter import expression_spliter
@profile(precision=6,stream=open('inorder2postorder_treeless.txt','w+'))
def inorder2postorder_treeless(expression):
    s_oper = Stack()
    Q_post = Queue()
    expression = expression_spliter(expression)
    for i in expression:
        if i == ')':
            while True:
                oper = s_oper.pop()
                if oper !='(':
                    Q_post.enqueue(oper)
                else: break
        elif i == '(':
            s_oper.push(i)
        elif i in op_list:
            if s_oper.isEmpty(): s_oper.push(i);continue
            while True:
                
                if s_oper.isEmpty():s_oper.push(i);break
                top = s_oper.peak()
                if P_dict[i]> P_dict[top]:
                    s_oper.push(i);break
                else:
                    oper = s_oper.pop()
                    Q_post.enqueue(oper)
        else:
            Q_post.enqueue(i)
        
    while True:
        if s_oper.isEmpty():break
        oper = s_oper.pop()
        Q_post.enqueue(oper)
    return Q_post.queue_list()