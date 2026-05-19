class Solution:
    def rec(self, i, nums, sum1, target, dp):

        if sum1 == target:
            return True

        if i >= len(nums) or sum1 > target:
            return False

        if dp[i][sum1] != -1:
            return dp[i][sum1]

        take = self.rec(i+1, nums, sum1 + nums[i], target, dp)
        not_take = self.rec(i+1, nums, sum1, target, dp)

        dp[i][sum1] = take or not_take

        return dp[i][sum1]

    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        return self.rec(0, nums, 0, target, dp)