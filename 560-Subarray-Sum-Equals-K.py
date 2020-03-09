class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    #错误：回溯法，不能保证连续
    #     res = []
    #     path = []
    #     self.sumk(nums,k,0,len(nums),path,res)
    #     return len(res)
        
    # def sumk(self,nums,target,begin,end,path,res):
    #     if target==0:
    #         res.append(path.copy())
    #     for i in range(begin,end):
    #         print(i,path,res)
    #         path.append(nums[i])
    #         target -=nums[i]
    #         self.sumk(nums,target,i+1,end,path,res)
    #         target +=nums[i]
    #         path.pop()

    #正确解法：
        acc = 0
        count = 0
        d = {}
        for num in nums:
            acc +=num
            if acc == k:
                count +=1
            if acc-k in d:
                count +=d[acc-k]
            if acc in d:
                d[acc] +=1
            else:
                d[acc] = 1
        return count
        
s = Solution()
result = s.subarraySum([1,1,1],2)
print(result)