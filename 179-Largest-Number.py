class LargestNumKey(str):
    def __lt__(x,y):# sort uses the lt by default
        return x+y>y+x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str,nums),key= LargestNumKey))
        return '0' if largest_num[0] == '0' else largest_num

s = Solution()
print(s.largestNumber([10,2]))