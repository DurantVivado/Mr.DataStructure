'''
spliting an expression using regex
@author : Durant
@email : durant2019@sina.com
'''
def expression_spliter(expression):
    #split the expression into list, using POWERFUL REGEX MODULE to ignite your productivity 
    #when you plan to add new operators, add them to the string \
    import re
    expression = ' '+expression
    bracketed_number = '[\(][\+\-][0-9\.]+[\)]'
    unbracketed_number = '(?<=[\+\-\*\/\(\%\^])[\+\-][0-9\.]+'
    normal_unsigned = '(?<=[0-9\.\(\)\+\-\*\/\%\^])[0-9\.]+|\s[0-9\.]+' 
    operator = '[\+\-\*\/\(\)\%\^]'
    return re.findall('(?:'+bracketed_number+'|'+unbracketed_number+'|'+normal_unsigned+'|'+operator+')',expression) #(-1)|±3|2|+-*/^%
    #return re.findall('(?:[0-9\.]+|[\+\-\*\/\(\)\%\^])',expression)