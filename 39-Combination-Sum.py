class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #回溯法
        if len(candidates) <= 0:
            return []
        else:
            candidates.sort()
            path = []
            result = []
            self.backtrack(candidates,target,0,len(candidates),path,result)
            return result
    
    def backtrack(self,candidates,target,begin,end,path,result):
        if target == 0:
            result.append(path.copy())
        else:
            for i in range(begin,end):
                left = target-candidates[i]
                if left < 0:
                    break
                else:
                    path.append(candidates[i])
                    self.backtrack(candidates,left,i,end,path,result)
                    path.pop()
    
s = Solution()
result = s.combinationSum(candidates = [2,3,5], target = 8)  
print(result)
