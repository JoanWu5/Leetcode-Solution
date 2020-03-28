class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string= ''
        stack  = []
        number = 0
        for c in s:
            if c == '[':
                stack.append(string)
                stack.append(number)
                string = ''
                number = 0
            elif c == ']':
                num = stack.pop()
                prevstring = stack.pop()
                string = prevstring + num*string
            elif c.isdigit():
                number = number*10 +int(c)
            else:
                string +=c
        return string


s = Solution()
print(s.decodeString("3[a2[c]]"))

                

                

                