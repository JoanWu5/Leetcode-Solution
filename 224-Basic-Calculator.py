class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        sign = 1
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10+int(char)
            elif char == '+':
                result +=sign*num
                sign = 1
                num = 0
            elif char =='-':
                result+=sign*num
                sign = -1
                num = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result +=sign*num
                result*=stack.pop()
                result+=stack.pop()
                num = 0
        return result+sign*num

s = Solution()
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))