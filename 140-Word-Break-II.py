class Solution(object):
    def __init__(self):
        self.result = []

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result  = []
        dp = [False for i in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (i-len(word)+1==0 or dp[i-len(word)]):
                    dp[i] = True
                    break
        return dp

    def wordBreak(self,s,wordDict):
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.wordBreak1(s,wordDict)
        self.dfs(s,"",dp,wordDict)
        return self.result

    def dfs(self,s,path,dp,wordDict):
        if dp[-1]:
            if not s:
                self.result.append(path.strip())
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],path+" "+s[:i],dp,wordDict)

s = Solution()
print(s.wordBreak(s = "catsanddog",wordDict = ["cat", "cats", "and", "sand", "dog"]))