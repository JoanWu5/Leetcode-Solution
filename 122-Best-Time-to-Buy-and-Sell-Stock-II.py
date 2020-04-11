class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_profit +=prices[i]-prices[i-1]
        return max_profit
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))