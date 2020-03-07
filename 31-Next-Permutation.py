class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        down_index = None
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                down_index = i
                break
        if down_index is None:
            nums = nums.reverse()
        else:
            for i in range(len(nums)-1,down_index,-1):
                if nums[i] > nums[down_index]:
                    nums[i],nums[down_index] = nums[down_index],nums[i]
                    break
            i = down_index+1
            j = len(nums)-1
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1

s= Solution()
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)


