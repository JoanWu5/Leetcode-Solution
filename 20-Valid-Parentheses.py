class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #version 1
        # stack = []
        # for i in s:
        #     if i =='(' or i =='[' or i=='{':
        #         stack.append(i)
        #     if (i==')' or i==']' or i=='}') and stack == []:
        #         return False
        #     if i == ')' and '(' !=stack.pop() or i==']' and '['!= stack.pop() or i=='}' and '{'!= stack.pop():
        #         return False
        # if stack!=[]:
        #     return False
        # return True

        #version 2
        bracket_map = {'(':')','{':'}','[':']'}
        open_par = ['(','[','{']
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

s = Solution()
print(s.isValid(']]'))
                
                
                
