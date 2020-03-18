# class Stack:
#     def __init__(self):
#         self.items = []
#     def __str__(self):  
#         return self.items
#     __repr_ = __str__
#     def push(self, item):
#         self.items.append(item) 
#     def pop(self):
#         return self.items.pop()


# def postfix_calculate(s):
#     stack = Stack()
#     for x in s:
#         if x.isdigit():
#             stack.push(x)
#         elif x == "+":
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(a)+int(b))
#             print(stack.items)
#         elif x == "-":
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(b)-int(a))
#             print(stack.items)
#         elif x == "*":
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(a)*int(b))
#             print(stack.items)
#         elif x == "/":
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(b)/int(a))
#             print(stack.items)
#     return stack.pop()
    

# strings = "12345*+*+"
# result = postfix_calculate(strings)
# print(result)

a = ['a','b','c']
print(a.pop())
print(a)

