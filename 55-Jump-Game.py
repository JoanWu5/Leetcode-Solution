class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i in range(len(nums)):
            if max_jump < i:
                return False
            else:
                max_jump = max(max_jump,nums[i]+i)
        
        if max_jump >= len(nums)-1:
            return True
        else:
            return False

s = Solution()
result = s.canJump([3,2,1,0,4])
print(result)
