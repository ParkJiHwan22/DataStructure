class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0

def infixToPostfix(expr):   # 주어진 중위 표현식을 후위 표현식으로 변환
    precedence = {'+':1, '-':1, '*':2, '/':2, '(':0}
    output = []
    s = Stack()
    number = ""
    
    for token in expr:
        if token.isdigit():
            number += token
        else:
            if number:
                output.append(number)
                number = ""
            if token == '(':
                s.push(token)
            elif token == ')':
                while s.peek() != '(':
                    output.append(s.pop())
                s.pop()  # pop the '('
            else:
                while not s.isEmpty() and precedence[s.peek()] >= precedence[token]:
                    output.append(s.pop())
                s.push(token)
    
    if number:
        output.append(number)
    
    while not s.isEmpty():
        output.append(s.pop())
    
    return output

def evalPostfix( expr ): # 주어진 후위 표현식을 계산하여 결과 값을 반환
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else:
            s.push( float(token) )
            
    
    return s.pop()

def calculate(expr): # 주어진 중위 표현식을 계산하여 결과 값을 반환
    postfix_expr = infixToPostfix(expr.replace(" ", ""))  # 공백 제거
    return evalPostfix(postfix_expr)

expr1 = "12 + (12 * 23)/ 9"
expr2 = "3 - 2 + 4 * 5"

print(expr1, '-->', calculate(expr1))
print(expr2, '-->', calculate(expr2))










# 후위식 계산 프로그램

# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self, item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop()
#         raise IndexError("pop from empty stack") # 스택이 비어있다면 오류를 발생시킴
    
#     def isEmpty(self):
#         return len(self.items) == 0


# def evalPostfix( expr ):
#     s = Stack()
#     for token in expr:
#         if token in "+-*/":
#             val2 = s.pop()
#             val1 = s.pop()
#             if (token == '+'): s.push(val1 + val2)
#             elif (token == '-'): s.push(val1 - val2)
#             elif (token == '*'): s.push(val1 * val2)
#             elif (token == '/'): s.push(val1 / val2)
#         else:
#             s.push( float(token) )
            
    
#     return s.pop()

# expr1 = ['0', '2', '/', '3', '-', '3', '2', '*', '+']
# expr2 = ['1', '2', '/', '4', '+', '1', '4', '/', '+']

# print(expr1, '-->', evalPostfix(expr1))
# print(expr2, '-->', evalPostfix(expr2))