class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid**2 <= x <(mid+1)**2:
                return mid
            elif  x<mid*mid:
                right = mid
            else:
                left = mid+1

s = Solution()
print(s.mySqrt(2147395599))

        