class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #version 1:
        # if x<0:
        #     return False
        # x = str(x)
        # left = 0
        # right = len(x)-1
        # while left<=right:
        #     if x[left]==x[right]:
        #         left+=1
        #         right -=1
        #     else:
        #         return False
        # return True

        #version 2:
        if x<0:
            return False
        r = 1
        while x//r>=10:
            r*=10
        while r>1:
            left,x = divmod(x,r)
            x,right = divmod(x,10)
            if left!=right:
                return False
            r//=100
        return True

s = Solution()
print(s.isPalindrome(121))