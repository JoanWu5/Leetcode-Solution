class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #version 1 
        # if target>nums[-1]:
        #     return len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif nums[i]>target:
        #         return i
            
        #version 2:O(log2n)
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return left

s = Solution()
print(s.searchInsert([1,3,5,6],0))