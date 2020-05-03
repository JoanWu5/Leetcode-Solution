class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '' or b == '':
            return a or b
        result = ''
        i1 = len(a)-1
        i2 = len(b)-1
        flag = 0
        while i1>=0 and i2>=0:
            sum1 = int(a[i1])+int(b[i2])+flag
            carry = sum1%2
            flag = sum1//2
            result =str(carry)+result
            i1 -=1
            i2 -=1
        if i1>=0 or i2>=0:
            c = a[:i1+1] or b[:i2+1]
            i = len(c)-1
            while i>=0:
                sum1 = int(c[i])+flag
                carry = sum1%2
                flag = sum1//2
                result =str(carry)+result
                i-=1
        if flag:
            result = '1'+result
        return result

s = Solution()
print(s.addBinary('11','1'))