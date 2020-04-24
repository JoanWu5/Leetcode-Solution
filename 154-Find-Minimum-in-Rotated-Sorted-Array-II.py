class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # nums[lo] <= nums[mi] <= nums[hi], min is nums[lo]
    # nums[lo] > nums[mi] <= nums[hi], (lo, mi] is not sorted, min is inside
    # nums[lo] <= nums[mi] > nums[hi], (mi, hi] is not sorted, min is inside
        if len(nums) ==1:
            return nums[0]
        left = 0
        right = len(nums)-1
        if nums[right]>nums[0]:
            return nums[0]
        while left< right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<nums[left]:
                right = mid
                left +=1
            else:
                right-=1
        return nums[left]

s = Solution()
print(s.findMin([1,2]))