class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        array = sorted(nums)
        for i in range(1,len(nums),2):
            nums[i] = array.pop()
        for i in range(0,len(nums),2):
            nums[i] = array.pop()

s = Solution()
nums = [1,1,1,5,4,6]
s.wiggleSort(nums)
print(nums)