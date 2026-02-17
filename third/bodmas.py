def evaluate_expression(expression):
    operator_precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '//': 2,
        '^': 3
    }
    
    def perform_operation(op, b, a):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b
        if op == '//':
            return a // b
        if op == '^':
            return a ** b
 
    tokens = expression.replace('//', ' // ').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').split()
 
    value=[]
    operator=[]
 
    i=0
    while i < len(tokens):
        token = tokens[i]
       
        if token == '(':
            operator.append(expression[i])
 
       
        elif token == ')':
            while operator and operator[-1] != '(':
                b = value.pop()
                a = value.pop()
                op = operator.pop()
                value.append(perform_operation(a, b, op))
            operator.pop()  
           
        if token.isdigit():
            value.append(int(token))
 
        elif token in operator_precedence:
            while(operator and operator_precedence.get(operator[-1],0) >= operator_precedence[token]):
                op=operator.pop()
                b=value.pop()
                a=value.pop()
                value.append(perform_operation(op,b,a))
           
            operator.append(token)
       
        i += 1
 
    while operator:
        op = operator.pop()
        b = value.pop()
        a = value.pop()
        value.append(perform_operation(op, b, a))
 
    return value[0]
 
expression=input("Enter your expression : ")
result=evaluate_expression(expression)
print("Result : ",result)