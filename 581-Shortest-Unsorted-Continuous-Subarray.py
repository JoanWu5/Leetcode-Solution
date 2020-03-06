class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1:sort and compare
        # sorted_nums = sorted(nums)
        # begin = 0
        # end = 0
        # for i in range(len(nums)):
        #     if nums[i] != sorted_nums[i]:
        #         begin = i
        #         break
        # for i in reversed(range(len(nums))):
        #     if nums[i] != sorted_nums[i]:
        #         end = i
        #         break
        # if begin == end:
        #     return 0
        # return end-begin+1

        #version 2 : find left and right 
        left = 0
        right = -1
        temp_left = nums[-1]
        temp_right = nums[0]

        for i in range(len(nums)):
            if temp_right > nums[i]:
                right = i
            else:
                temp_right = nums[i] 

        for i in reversed(range(len(nums))):
            if temp_left < nums[i]:
                left = i
            else:
                temp_left = nums[i]
        
        if right - left <= 0:
            return 0
        else:
            return right- left + 1
            
s = Solution()
result = s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
print(result)