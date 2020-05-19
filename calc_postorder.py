'''
calculate the value of post expression
@author: Durant 
@email: durant2019@sina.com
'''
#______________________________CalcTree________________________________________       
class DenominatorZeroError(Exception):
    "Check if Node is Null"
    def __str__(self):
        return u"Denominator is Zero!"
class UnsupportedOperatorError(Exception):
    "Check if Node is Null"
    def __str__(self):
        return u"Unsupported Operator!"
    
def Calculator(operator,num_a,num_b):
    if operator == '+': return (num_a+num_b)
    elif  operator == '-': return (num_a - num_b)
    elif operator == '*': return (num_a*num_b)
    elif operator == '/' :
        if num_b!=0: return (num_a/num_b)
        else : raise DenominatorZeroError
    elif operator == '^': return pow(num_a,num_b)
    elif operator == '%': return (num_a%num_b)
    
    else: raise UnsupportedOperatorError
        

def CalcPost(post_exp):
    #calculate the value of post expression
    import re
    s_num = Stack()
    calc_ans = 0.0
    if len(post_exp)==1 and post_exp not in op_list: return float(post_exp[0])
    if len(post_exp)==0: return None
    for i in post_exp:
        if i in op_list:
            num_a = s_num.pop()
            num_b = s_num.pop()
            if '(' in num_a : num_a = re.split(r'[()]',num_a)[1]
            if '(' in num_b : num_b = re.split(r'[()]',num_b)[1]
            calc_ans = Calculator(i,float(num_b),float(num_a))
            s_num.push(str(calc_ans))
           
        else:
            s_num.push(i)
    return calc_ans