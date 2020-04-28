class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(nums,k,index,path,result):
            if k==0:
                result.append(path.copy())
            for i in range(index,len(nums)):
                helper(nums,k-1,i+1,path+[nums[i]],result)

        result = []
        nums = list(range(1,n+1))
        helper(nums,k,0,[],result)
        return result

s = Solution()
print(s.combine(4,2))