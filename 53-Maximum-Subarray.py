import sys
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1
        # maxsum = max(nums)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         sum1 = 0
        #         for k in range(i,j+1):
        #             sum1 = sum1 + nums[k]
        #         if maxsum<sum1:
        #             maxsum = sum1
        #
        # return maxsum

        #version 2
        # prefixSum = []
        # prefixSum.append(0)
        # prefixSum.append(nums[0])
        # for i in range(1,len(nums)):
        #     prefixSum.append(prefixSum[i] + nums[i])
        # maxsum = max(nums)
        # for i in range(len(prefixSum)):
        #     for j in range(i):
        #         subarray = prefixSum[i]-prefixSum[j]
        #         maxsum = max(maxsum,subarray)
        # return  maxsum

        #version 3
        maxsum = nums[0]
        minsum = 0
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            maxsum = max(sum-minsum,maxsum)
            minsum = min(sum,minsum)
        return maxsum

        #version 4 分治法
    #     return self.helper(nums,0,len(nums)-1)
    # def helper(self, nums, l,r):
    #     if l>r:
    #         return -sys.maxsize
    #     mid = int((l+r)/2)
    #     left_max = right_max =0
    #     left = self.helper(nums,l,mid-1)
    #     right = self.helper(nums,mid+1,r)
    #     sum =0
    #     for i in reversed(range(l,mid)):
    #         sum +=nums[i]
    #         left_max = max(left_max,sum)
    #     sum=0
    #     for i in range(mid+1,r+1):
    #         sum+=nums[i]
    #         right_max = max(right_max,sum)
    #     cross_max = left_max+right_max+nums[mid]
    #     return max(cross_max,left,right)


s = Solution()
result  = s.maxSubArray([1,2])
print(result)

