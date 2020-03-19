class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) <=2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0]+nums[2]
        for i in range(3,len(nums)):
            dp[i] = max(dp[i-2],dp[i-3])+nums[i]
        return max(dp[len(nums)-2],dp[len(nums)-1])  

s = Solution()
result = s.rob([2,7,9,3,1])
print(result) 