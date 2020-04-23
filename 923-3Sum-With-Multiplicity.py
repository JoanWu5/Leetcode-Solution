class Solution(object):
    def threeSumMulti(self, nums, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
            """
        if len(nums)<3:
            return []
        result = 0
        nums.sort()
        for i in range(len(nums)):
            target1 = target-nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right]<target1:
                    left+=1
                elif nums[left]+nums[right]>target1:
                    right -=1
                elif nums[left]!= nums[right]:
                    kleft = 1
                    kright = 1
                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                        kleft +=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                        kright +=1
                    result += kleft*kright
                    left+=1
                    right -=1
                else:
                    M = right-left+1
                    result+=M*(M-1)//2
                    break
        return result%(10**9+7)

s = Solution()
print(s.threeSumMulti([1,1,2,2,2,2],5))