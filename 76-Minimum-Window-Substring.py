import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        tcounter = collections.Counter(t)
        lengtht = len(tcounter)
        left = 0
        right = 0
        unique_c = 0
        windows_count = {}
        # ans tuple of the form (window length, left, right)
        ans = (float("inf"), None, None)

        while right<len(s):
            character = s[right]
            windows_count[character] = windows_count.get(character,0)+1
            
            if character in tcounter and windows_count[character] == tcounter[character]:
                unique_c +=1
            while left <= right and unique_c == lengtht:
                character = s[left]
                if right-left+1 < ans[0]:
                    ans = (right-left+1,left,right)
                windows_count[character] -=1
                if character in tcounter and windows_count[character]<tcounter[character]:
                    unique_c -=1
                left +=1
            right +=1

        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]:ans[2]+1]

s = Solution()
result = s.minWindow(s = "aa", t = "aa")
print(result)