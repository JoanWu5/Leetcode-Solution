class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n<=0:
        #     return False
        # if n == 1:
        #     return True
        # while n>1:
        #     if n%2 == 1:
        #         return False
        #     n = n//2
        # return True
        return n>0 and (n & n-1)==0
s = Solution()
print(s.isPowerOfTwo(218))
        