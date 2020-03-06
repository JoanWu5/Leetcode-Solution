class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #version 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #
        #version 2
        #tips: emumerate
        # seq = ['one', 'two', 'three']
        # for i, element in enumerate(seq):
        # print(i, element)
        # 0 one
        h = {}
        for i,element in enumerate(nums):
            n = target - element
            if n not in h:
                h[element] = i
            else:
                return [h[n],i]

s1 = Solution()
result = s1.twoSum([2,7,9,11],9)
print(result)