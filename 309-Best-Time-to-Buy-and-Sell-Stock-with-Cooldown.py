class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy[i] 表示第 i 天，且以 buy 或者 coolwown 结尾的最大利润
        # sell[i] 表示第 i 天，且以 sell 或者 cooldown 结尾的最大利润
        if not prices or len(prices) <=1:
            return 0
        buy = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        buy[0] = -prices[0]
        buy[1] = max(-prices[0],-prices[1])
        sell[1] = max(0,prices[1]-prices[0])
        for i in range(2,len(prices)):
            buy[i] = max(sell[i-2]-prices[i],buy[i-1])
            sell[i] = max(sell[i-1],buy[i-1]+prices[i])
        result = max(buy[len(prices)-1],sell[len(prices)-1])
        return result

s = Solution()
result = s.maxProfit([1,2,3,0,2])
print(result)
