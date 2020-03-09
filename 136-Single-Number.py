class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #异或
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

s = Solution()
result = s.singleNumber([2,2,1])
print(result)