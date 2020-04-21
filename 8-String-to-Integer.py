class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        if ls[0] =='-':
            sign = -1
        else:
            sign = 1
        if ls[0] in ['-','+']:
            del ls[0]
        result = 0
        i = 0
        while i<len(ls) and ls[i].isdigit():
            result = result*10+ord(ls[i])-ord('0')
            i+=1
        result = result*sign
        if result > pow(2,31)-1:
            return pow(2,31)-1
        elif result <-pow(2,31):
            return -pow(2,31)
        else:
            return result

s = Solution()
print(s.myAtoi(" "))


