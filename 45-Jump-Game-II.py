class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        left = 0
        jumps = 1
        right = nums[0]
        while right<len(nums)-1:
            next_step = 0
            for i in range(left,right+1):
                next_step = max(i+nums[i],next_step)
            left = right
            right = next_step
            jumps+=1
        return jumps

s= Solution()
print(s.jump([2,3,1,1,4]))