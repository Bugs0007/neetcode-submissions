class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float('inf')

        for i in range(len(prices)):
            curr = prices[i]

            if profit < curr-low:
                profit = curr-low
            
            if curr < low:
                low = curr
        return profit
            