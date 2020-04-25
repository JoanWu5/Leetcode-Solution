class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_profit = 0
        min_profit = prices[0]
        for price in prices:
            if price<min_profit:
                min_profit = price
            if price-min_profit>max_profit:
                max_profit = price-min_profit
        return max_profit

s = Solution()
print(s.maxProfit([7,6,4,3,1]))
