class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []
        visited = set()
        self.helper(nums,visited,path,result)
        return result
    
    def helper(self,nums,visited,path,result):
        if len(path) == len(nums):
            result.append(path.copy())
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                path.append(nums[i])
                self.helper(nums,visited,path,result)
                visited.remove(i)
                path.pop()
                    
            
    
s = Solution()
print(s.permute([1,2,3]))
