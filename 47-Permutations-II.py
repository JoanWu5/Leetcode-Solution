from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        visited = Counter(nums)
        def helper(nums,visited,path,result):
            if len(path) == len(nums):
                result.append(path.copy())
            else:
                for i in visited:
                    if visited[i]>0:
                        visited[i] -=1
                        path.append(i)
                        helper(nums,visited,path,result)
                        path.pop()
                        visited[i] +=1

        helper(nums,visited,path,result)
        return result