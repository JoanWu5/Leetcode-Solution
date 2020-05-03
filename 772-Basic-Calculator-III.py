class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = '+'
        result = 0
        cur_result = 0
        num = 0
        i = 0
        while i<len(s):
            if s[i].isdigit():
                num = num*10+int(s[i])
            elif s[i] == '(':
                j = i
                count = 0
                while i<len(s):
                    if s[i] =='(':
                        count +=1
                    elif s[i] ==')':
                        count-=1
                    if count ==0:
                        break
                    i+=1
                num = self.calculate(s[j+1:i])
            if s[i] in '+-*/' or i == len(s)-1:
                if sign=='+':
                    cur_result +=num
                elif sign == '-':
                    cur_result-=num
                elif sign =='*':
                    cur_result*=num
                else:
                    cur_result//=num
                if s[i] in "+-" or i == len(s)-1:
                    result+=cur_result
                    cur_result =0
                sign = s[i]
                num = 0
            i+=1
        return result

s = Solution()
print(s.calculate("2*(5+5*2)/3+(6/2+8)"))