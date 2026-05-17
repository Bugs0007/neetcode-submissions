class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 100
        for i in range(len(prices)):
            curr = prices[i]
            profit = curr - min_buy
            max_profit = max(max_profit, profit)
            if curr < min_buy:
                min_buy = curr

        return max_profit