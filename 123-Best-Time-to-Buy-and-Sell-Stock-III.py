class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        k = 2
        dp = [[0 for j in range(len(prices))]for i in range(k+1)]
        for kk in range(1,k+1):
            mmin =  prices[0]
            for i in range(1,len(prices)):
                mmin = min(mmin,prices[i]-dp[kk-1][i-1])
                dp[kk][i] = max(dp[kk][i-1],prices[i]-mmin)
        return dp[k][len(prices)-1]

s = Solution()
print(s.maxProfit([2,1,4]))