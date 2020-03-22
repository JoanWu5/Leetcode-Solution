class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalsum = sum(nums)
        if totalsum%2 == 1:
            return False
        halfsum = totalsum//2
        dp = [False] * (halfsum+1)
        dp[0] = True
        for num in nums:
            for i in range(halfsum,num-1,-1):
                if dp[i-num]:
                    dp[i] = True
        return dp[halfsum]

s = Solution()
print(s.canPartition([1,2,5]))

            
