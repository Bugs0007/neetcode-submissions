class Solution:
    def rec(self, i, coins, amount, dp):
        if i >= len(coins):
            return float("inf")
        elif amount < 0:
            return float("inf")
        elif amount == 0:
            return 0
        elif dp[i][amount] != -1:
            return dp[i][amount]

        take = 1 + self.rec(i, coins, amount-coins[i], dp)
        not_take = self.rec(i+1, coins, amount, dp)

        dp[i][amount] = min(take, not_take)
        return dp[i][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [[-1 for i in range(amount+1)] for j in range(n)]
        ans = self.rec(0, coins, amount, dp)
        return -1 if ans == float("inf") else ans