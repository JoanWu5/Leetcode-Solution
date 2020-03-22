import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount ==0:
            return 0
        dp = [sys.maxsize]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i-coins[j]>=0:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[-1] == sys.maxsize:
            return -1
        else:
            return dp[-1]

s = Solution()
result = s.coinChange(coins = [2], amount = 3)
print(result)
