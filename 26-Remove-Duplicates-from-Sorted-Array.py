class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        position = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
                nums[position],nums[i] = nums[i],nums[position]
                position +=1
        nums = nums[0:position]
        return position

s = Solution()
nums= [1,1,2]
print(s.removeDuplicates(nums))
print(nums)
                
            