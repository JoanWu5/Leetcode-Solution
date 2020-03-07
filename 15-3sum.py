class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #version 1:Run Out of Time
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         c = -nums[i]-nums[j]
        #         nums_temp = nums.copy()
        #         del nums_temp[i]
        #         del nums_temp[j-1]
        #         if c in nums_temp:
        #             lst =sorted([nums[i],nums[j],c])
        #             if lst not in result:
        #                 result.append(lst)
        # return result

        #version 2 
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return []
        result = []

        for i in range(length):
            target = -nums[i]
            if i> 0 and nums[i] == nums[i-1]:
                continue
            right_p = length-1
            left_p = i+1
            while left_p<right_p:
                if nums[left_p]+nums[right_p] == target:
                    result.append([nums[left_p],nums[right_p],-target])
                    while left_p<right_p and nums[left_p] == nums[left_p+1]:
                        left_p += 1
                    while left_p<right_p and nums[right_p] == nums[right_p-1]:
                        right_p -= 1
                    left_p +=1
                    right_p -=1
                elif nums[left_p] + nums[right_p] <target:
                    left_p +=1
                else:
                    right_p -=1
        return result    


s = Solution()
result = s.threeSum([-1, 0, 1, 2, -1, -4])
print(result)
        