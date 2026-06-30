
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, profit = math.inf, 0

        # for price in prices:
        #     buy = min(buy, price)
        #     profit = max(profit, price - buy)

        # return profit

        l = 0
        ans = 0

        for r, price in enumerate(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                ans = max(ans, profit)
            else:
                l = r
        return ans
        
