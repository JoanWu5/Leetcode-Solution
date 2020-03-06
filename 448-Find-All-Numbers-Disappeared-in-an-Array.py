class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # do not use extra space and the time is O(N)
        disappear = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1 
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                disappear.append(i+1)
        
        return disappear

s = Solution()
disappear = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(disappear)