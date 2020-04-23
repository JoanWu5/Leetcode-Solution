class Solution(object):
    def threeSum(self, nums,target1):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            target = target1-nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right] == target:
                    result.append([nums[left],nums[right],nums[i]])
                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right -=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right -=1
        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            threeResult = self.threeSum(nums[i+1:],target-nums[i])
            for item in threeResult:
                result.append([nums[i]]+item)
        return result

s = Solution()
print(s.fourSum(nums = [1, 0, -1, 0, -2, 2], target = 0.))
        
