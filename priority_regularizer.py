from stack_intro import Stack,LinkList_Stack
'''
This func handles with expression, turning them into bracket-paired expression
,returning as a list.
@author:Durant
@email: durant2019@sina.com
'''
op_list = ['+','-','*','/','%','^']

P_dict = {'^':3,'*':2,'/':2,'%':2,'+':1,'-':1,'(':0}
def priority_regularizer(expression):

    '''
    Method1: Add brackets to avoid comparation of priority of operators
    Method2: Regularize the sequence of operators and numbers to satisfy the stack
    for example: 4+6/5*3-2
    Method 1 returns: (4+((6/5)*3))-2
    Method 2 returns:  4-2+6/5   
    for exemplar convenience, we adopt the Method 1
    '''
    if len(expression)==1: return expression
    s_oper= Stack()#stack holding operators
    s_item = Stack() #stack holding the '+' or '-' between items
    s_same_pri = Stack() # stack holding the operator of same priority
    exp = expression_spliter(expression)
    ls = LinkList_Stack()# linked stack for printing into lists or on screen 
    ls.initList(exp)
    p = ls.head

    while p:
#        print(p.val)
#        ls.printList(ls.head,print_res=True)
        if p.val in op_list or p.val=='(':
            s_oper.push(p)
            
                
        elif p.val == ')':
            while True:
                oper = s_oper.pop()
#                ls.printList(ls.head,print_res=True)
                if not oper or oper.val=='(': break
                if oper.val in ['+','-']:
                    s_item.push(oper)
                top = s_oper.peak().val
                if P_dict[oper.val]>P_dict[top]:
                    insert_brackets(oper.prev,oper.next,ls)
                elif P_dict[oper.val]==P_dict[top]:
                    #when two operator's priorities are same, parenthesize it according to sequence into stack
                    s_same_pri.push(oper)
                    while True:
                        oper_tmp = s_oper.pop()
#                        print('op_tmp',oper_tmp.val)
                        if oper_tmp.val=='(':break
                        if P_dict[oper.val]==P_dict[oper_tmp.val]:
                            s_same_pri.push(oper_tmp)
                            
                        elif P_dict[oper.val]<P_dict[oper_tmp.val]: 
                            insert_brackets(oper_tmp.prev,oper_tmp.next,ls)
#                            ls.printList(ls.head,print_res=True)
#                            break
                        else: break
                    while True:
                        oper_tmp = s_same_pri.pop()
                        if not oper_tmp : break
#                        print('op_tmp',oper_tmp.val)
                        insert_brackets(oper_tmp.prev,oper_tmp.next,ls)
          
            while True:# parenthesize the item inside brackets
                oper = s_item.pop()
                if oper == None: break
#                print("oper3.val",oper.val)
#                ls.printList(ls.head,print_res=True)
                insert_brackets(oper.prev,oper.next,ls)
        p = p.next
        
    while True:
        oper = s_oper.pop()
#        ls.printList(ls.head,print_res=True)
        
        if s_oper.isEmpty():
            if oper: insert_brackets(oper.prev,oper.next,ls)
#            ls.printList(ls.head,print_res=True)
            break
        if oper.val in ['+','-']:
            s_item.push(oper)
#        print("oper2.val",oper.val)
        
        top = s_oper.peak().val
        if P_dict[oper.val]>P_dict[top]:
            insert_brackets(oper.prev,oper.next,ls)
        elif P_dict[oper.val]==P_dict[top]:
            s_same_pri.push(oper)
            while True:
                oper_tmp = s_oper.pop()
                if not oper_tmp:break
#                print('op_tmp',oper_tmp.val)
                if P_dict[oper.val]==P_dict[oper_tmp.val] :
                    s_same_pri.push(oper_tmp)
                elif P_dict[oper.val]<P_dict[oper_tmp.val]: 
                    insert_brackets(oper_tmp.prev,oper_tmp.next,ls)
#                    ls.printList(ls.head,print_res=True)
#                    break
                else: break
            while True:
                oper_tmp = s_same_pri.pop()
                if not oper_tmp: break
#                print('op_tmp',oper_tmp.val)
                insert_brackets(oper_tmp.prev,oper_tmp.next,ls)

    while True:
        oper = s_item.pop()
        if not oper: break
#        print("oper3.val",oper.val)
#        ls.printList(ls.head,print_res=True)
        insert_brackets(oper.prev,oper.next,ls)
#        if s_item.isEmpty(): break
        
    
    res = ls.printList(ls.head,print_res=False)
    return res

def insert_brackets(r,m,ls):
    #if there is already brackets then quit
    
    if r.val == ')':
        l_count=r_count=0
        while True:
            if r.val=='(':l_count+=1
            elif r.val==')': r_count+=1
            if l_count-r_count == 0 or r.prev==None: break
            r = r.prev
    if m.val == '(':
        
        l_count=r_count=0
        while True:
            if m.val=='(':l_count+=1
            elif m.val==')': r_count+=1
            if r_count-l_count == 0 or m.next == None: break
            m = m.next
    if r.prev!=None and  r.prev.val== '(' and m.next!=None and m.next.val==')':return
    else:
        ls.insert(r,'(','front')
        ls.insert(m,')','back')