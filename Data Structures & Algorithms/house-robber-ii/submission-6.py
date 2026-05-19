class Solution:
    def rec(self, i, n, nums, dp):
        if i >= n:
            return 0
        
        if dp[i] != 0:
            return dp[i]
        take = nums[i] + self.rec(i+2, n, nums, dp)
        not_take = self.rec(i+1, n, nums, dp)

        dp[i] = max(take, not_take)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp1 = [0] * n
        dp2 = [0] * n
        ans = max(self.rec(0, n-1, nums, dp1), self.rec(1, n, nums, dp2))
        return ans