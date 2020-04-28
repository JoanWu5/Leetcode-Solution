class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.helper(nums,0,[],result)
        return result

    def helper(self,nums,index,path,result):
        result.append(path)
        for i in range(index,len(nums)):
            if i>index and nums[i] == nums[i-1]:
                continue
            self.helper(nums,i+1,path+[nums[i]],result)

s= Solution()
print(s.subsetsWithDup([1,2,2]))