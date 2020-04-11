class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #version 1 
        # kk = k%len(nums)
        # rotatei = len(nums)-kk
        # temp = nums[rotatei:]
        # nums[kk:] = nums[0:rotatei]
        # nums[0:kk] = temp

        #version 2
        kk = k%len(nums)
        nums.reverse()
        nums[0:kk]= list(reversed(nums[0:kk]))
        nums[kk:] = list(reversed(nums[kk:]))


s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums,3)
print(nums)