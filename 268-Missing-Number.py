class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        
        #version 2:
        missing = len(nums)
        for i,num in enumerate(nums):
            missing ^=i^num
        return missing

s = Solution()
print(s.missingNumber([2,0]))
 