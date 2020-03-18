class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    #version 1
    #     result = ""
    #     for i in range(len(s)):
    #         temp = self.helper(s,i,i)
    #         if len(temp) > len(result):
    #             result = temp
    #         temp = self.helper(s,i,i+1)
    #         if len(temp) > len(result):
    #             result = temp 
    #     return result

    # def helper(self,s,left,right):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -=1
    #         right +=1
    #     return s[left+1:right]

    #version 2: dp
        max_length = 0
        result = ""
        dp = [[False for i in range(len(s))]for j in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            dp[i][i] =  True
            for j in range(i+1,len(s)):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = True
                    if max_length<2:
                        max_length = 2
                        result = s[i:i+2]
                if j>i+1 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if max_length <j-i+1:
                        max_length = j-i+1
                        result = s[i:j+1]
        return result


s = Solution()
result = s.longestPalindrome("babab")
print(result)
            