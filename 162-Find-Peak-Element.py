class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1 :0(n)
        # if len(nums) == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[-1]>nums[-2]:
        #     return len(nums)-1

        # for i in range(1,len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] >nums[i+1]:
        #         return i

        #version 2:O(logn)
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left
        
s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))