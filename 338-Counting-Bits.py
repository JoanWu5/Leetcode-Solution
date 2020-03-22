class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]*(num+1)
        for i in range(1,num+1):
            if i%2 == 1:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = dp[i//2]
        return dp

s = Solution()
result = s.countBits(5)
print(result)