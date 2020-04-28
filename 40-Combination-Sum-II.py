class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(candidates,target,index,path,result):
            if target<0:
                return
            if target == 0:
                result.append(path.copy())
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i] ==candidates[i-1]:
                    continue
                helper(candidates,target-candidates[i],i+1,path+[candidates[i]],result)
        
        result = []
        candidates.sort()
        helper(candidates,target,0,[],result)
        return result
        
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))