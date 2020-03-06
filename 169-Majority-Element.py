class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # version 1：dictionary
        # dict = {}
        # for n in nums:
        #     if n not in dict.keys() :
        #         dict[n] = 1
        #     else:
        #         dict[n] += 1
        # maxkey = max(dict, key=dict.get) #找打字典中value最大对应的key值
        # return maxkey

        #version 2：投票算法：通过不断消除不同元素直到没有不同元素，剩下的元素就是我们要找的元素。
        count = 1
        majority = nums[0]
        for n in nums[1:]:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1
        return majority
            

s = Solution()
result = s.majorityElement([2,2,1,1,1,2,2])
print(result)

    
          