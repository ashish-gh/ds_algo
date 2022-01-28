from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit

