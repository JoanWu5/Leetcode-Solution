class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #version 1
        # if len(nums)<=0:
        #     return -1
        # else:
        #     low = 1
        #     high = len(nums)-1
        #     while(low<=high):
        #         mid = (low+high)//2
        #         count = sum(x<=mid for x in nums)
        #         if count>mid:
        #             high = mid-1
        #         else:
        #             low = mid+1
        #     return low

        #version 2 
        if len(nums)<=0:
            return -1
        else:
            slow = 0
            fast = 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            
            finder = 0
            while True:
                finder = nums[finder]
                slow = nums[slow]
                if slow == finder:
                    return slow

s = Solution()
result = s.findDuplicate([1,3,4,2,2])
print(result)
