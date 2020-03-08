class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left_p = 0
        current = 0
        right_p = len(nums)-1
        while current <= right_p:
            if nums[current] == 0:
                nums[left_p], nums[current] = nums[current],nums[left_p]
                left_p +=1
                current+=1
            elif nums[current] ==2:
                nums[right_p],nums[current] = nums[current],nums[right_p]
                right_p -=1
            else:
                current +=1


s = Solution()
nums = [2,0,1]
s.sortColors(nums)
print(nums)
