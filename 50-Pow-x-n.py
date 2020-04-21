class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = n<0
        if abs(n)<=1:
            return x**n
        n = abs(n)
        result = 1
        while n>=2:
            if n%2 ==1:
                result *=x
            x = x*x
            n = n//2
        result *=x
        if flag:
            return 1/result
        else:
            return result

s = Solution()
print(s.myPow(2,-2))

            


