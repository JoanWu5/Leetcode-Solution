class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #version 1
        if n < 5:
            return 0
        if n< 10:
            return 1
        return(n//5+self.trailingZeroes(n//5))

        #version 2:
        result = 0
        while n:
            result +=n//5
            n = n//5
        return result


s = Solution()
print(s.trailingZeroes(10))
