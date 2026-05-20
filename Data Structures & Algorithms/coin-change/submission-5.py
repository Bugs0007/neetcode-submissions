class Solution:
    def rec(self, i, coins, target, dp):
        if target == 0:
            return 0
        elif i >= len(coins):
            return float('inf')
        elif coins[i] == 0:
            return float('inf')
        elif target < 0:
            return float('inf')

        if dp[i][target] != -1:
            return dp[i][target]

        curr = coins[i]
        
        take = 1 + self.rec(i, coins, target - coins[i], dp)
        not_take = self.rec(i+1, coins, target, dp)
        dp[i][target] = min(take, not_take)
        return dp[i][target]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
        rev = (sorted(coins))[::-1]
        ans = self.rec(0, rev, amount, dp)
        return -1 if ans == float('inf') else ans