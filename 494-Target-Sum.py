class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #version 1:Time Limit Exceeded
        # total = sum(nums)
        # dp= [0]*(2*total+1)
        # temp = [0]
        # for num in nums:
        #     itemp = []
        #     for i in temp:
        #         dp[total+(i-num)] +=1
        #         itemp.append(i-num)
        #         dp[total+(i+num)] +=1
        #         itemp.append(i+num)
        #     temp = itemp

        # result = 0
        # for temp1 in temp:
        #     if temp1 == S:
        #         result+=1
        # return result

        #version 2:
        total = sum(nums)
        if len(nums) == 1:
            if S == -nums[0] or S==nums[0]:
                return 1
            else:
                return 0
        dp= [0]*(2*total+1)
        dp[nums[0]+total] =1
        dp[-nums[0]+total] +=1
        for i in range(1,len(nums)):
            next1 = [0]*(2*total+1)
            for j in range(-total,total+1):
                if dp[j+total]>0:
                    next1[j+total-nums[i]] +=dp[j+total]
                    next1[j+total+nums[i]] +=dp[j+total]
            dp = next1
        if S>1000 or S>total:
            return 0
        else:
            return dp[S+total]

s = Solution()
print(s.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],1000))