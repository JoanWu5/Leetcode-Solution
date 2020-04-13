class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        d ={}
        for item in nums1:
            d[item] = d.get(item,0)+1
        for item in nums2:
            if item in d:
                result.append(item)
                d[item] -=1
                if d[item] == 0:
                    del d[item]
        return result

s = Solution()
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
