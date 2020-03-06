class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything,do not copy the list, modify nums in-place instead.
        """
        #version 1 : del 0 + append 0
        # count = 0
        # zero_index = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
        #         zero_index.append(i)
        
        # for i in reversed(zero_index):
        #     del nums[i]

        # for i in range(count):
        #     nums.append(0)

        #version 2: switch 0 
        nonezero = 0
        zero = 0
        while (nonezero < len(nums)):
            if nums[nonezero] != 0:
                nums[nonezero], nums[zero] = nums[zero], nums[nonezero]
                zero += 1
            nonezero += 1
s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)
        