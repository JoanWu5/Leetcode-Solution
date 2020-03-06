class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #version 1 
        # profit = 0
        # for i in range(len(prices)-1):
        #     current_price = prices[i]
        #     current_profit = 0
        #     max_current_price = max(prices[i+1:])
        #     if current_price < max_current_price:
        #         current_profit = max_current_price-current_price
        #     if current_profit > profit:
        #         profit = current_profit
        # return profit

        #version 2 
        profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif profit < price - min_price:
                profit = price - min_price
        
        return profit


s1 = Solution()
result = s1.maxProfit([7,6,4,3,1])
print(result)