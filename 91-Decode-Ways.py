class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0:2]=[1,1]
        for i in range(2,len(s)+1):
            if 0<int(s[i-1])<=9:
                dp[i] = dp[i-1]
            if 10<=int(s[i-2]+s[i-1])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]

s = Solution()
print(s.numDecodings('226'))
