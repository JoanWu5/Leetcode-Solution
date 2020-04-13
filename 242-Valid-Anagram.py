from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #version 1
        # if Counter(s) == Counter(t):
        #     return True
        # else:
        #     return False

        #version 2:
        dict1 = {}
        for item in s:
            dict1[item] = dict1.get(item,0)+1
        for item in t:
            if item not in dict1:
                return False
            else:
                dict1[item] -=1
                if dict1[item] == 0:
                    del dict1[item]   
        return not dict1
s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))