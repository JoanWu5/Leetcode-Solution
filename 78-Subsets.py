class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        self.getsubsets(nums,0,result,temp)
        return result

    def getsubsets(self,nums,start,result,temp):
        result.append(temp.copy())
        for i in range(start,len(nums)):
            temp.append(nums[i])
            self.getsubsets(nums,i+1,result,temp)
            temp.pop()

s = Solution()
result = s.subsets([1,2,3])    
print(result)   