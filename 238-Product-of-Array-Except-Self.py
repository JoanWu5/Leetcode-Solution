class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for i in range(len(nums))]
        temp = nums[0]
        for i in range(1,len(nums)):
            result[i] = temp
            temp *=nums[i]
        temp = nums[-1]
        for i in reversed(range(0,len(nums)-1)):
            result[i] *=temp
            temp *=nums[i]
        return result

s = Solution()
result = s.productExceptSelf([1,2,3,4])
print(result)