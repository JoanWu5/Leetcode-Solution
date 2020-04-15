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
# a= ['c','a']
# print(''.join(a))
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create_List(self,lst):
        if lst is None or lst == []:
            return None
        head = ListNode(0)
        cur = head
        for item in lst:
            node = ListNode(item)
            cur.next = node
            cur = cur.next
        return head.next

    def partition(self,head,val):
        if head is None:
            return None
        left = ListNode(0)
        right = ListNode(0)
        curleft = left
        curright = right
        count = 0
        while head:
            if head.val<val:
                curleft.next = head
                curleft = curleft.next
            elif head.val>val:
                curright.next = head
                curright = curright.next
            else:
                count +=1
            head = head.next

        while count>0:
           node = ListNode(val)
           curleft.next = node
           curleft = curleft.next
           count -=1

        curright.next = None
        curleft.next = right.next
        return  left.next
    
    def print_ListNode(self,head):
        while head:
            print(head.val)
            head = head.next

s = Solution()
# test 1:val in listNode
head = s.create_List([1,2,3,5,10,11,4])
result = s.partition(head,5)
s.print_ListNode(result)

# test 2: val > all listNode
head = s.create_List([1,2,3,5,10,11,4])
result = s.partition(head,12)
s.print_ListNode(result)

# test 3: val < all listNode
head = s.create_List([1,2,3,5,10,11,4])
result = s.partition(head,-1)
s.print_ListNode(result)

# test4 :val not in listNode
head = s.create_List([1,2,3,5,10,11,4])
result = s.partition(head,6)
s.print_ListNode(result)


