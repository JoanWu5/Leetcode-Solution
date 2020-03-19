class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1: dp
        # if len(nums) <=1:
        #     return len(nums)
        # count = [1 for i in range(len(nums))]
        # for i in range(len(nums)-2,-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] < nums[j]:
        #             count[i] = max(count[j]+1,count[i])
        # return max(count)

        #version 2:dp & binary search
        tails = [0]*len(nums)
        count = 0
        for  x in nums:
            i=0
            j=count
            while i!=j:
                m = (i+j)//2
                if tails[m] <x:
                    i = m+1
                else:
                    j = m
            tails[i] = x
            count = max(i+1,count)
        return count


s = Solution()
result = s.lengthOfLIS([10,9,2,5,3,7,101,18])
print(result)