class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (i-len(word)+1 == 0 or dp[i-len(word)]):
                    dp[i] = True
                    break
        return dp[-1]

s = Solution()
print(s.wordBreak("applen",["app"]))

        
