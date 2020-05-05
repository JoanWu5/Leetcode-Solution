class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        if len(strs) ==1:
            return strs[0]
        result = strs[0]
        for i in range(1,len(strs)):
            length = min(len(result),len(strs[i]))
            k = 0
            while k<length:
                if strs[i][k] == result[k]:
                    k+=1
                else:
                    break
            result = result[0:k]
        return result

s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))
