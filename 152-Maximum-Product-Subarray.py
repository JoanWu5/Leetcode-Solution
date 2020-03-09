class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1:O(n^2)
        # if len(nums) <=1:
        #     return nums[0]
        
        # max_product = nums[0]
        # temp = None
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     max_product = max(max_product,temp)
        #     for j in range(i+1,len(nums)):
        #         temp *= nums[j]
        #         max_product = max(max_product,temp)
        # return max_product

        #vresion 2:O(n)
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        if len(nums) <=1:
            return nums[0]
        for i in range(1,len(nums)):
            temp = max_product
            max_product = max(nums[i],max(max_product*nums[i],min_product*nums[i]))
            min_product = min(nums[i],min(min_product*nums[i],temp*nums[i]))
            result = max(max_product,result)
        return result
        
s = Solution()
result = s.maxProduct([-4,-3,-2]) 
print(result)
            
