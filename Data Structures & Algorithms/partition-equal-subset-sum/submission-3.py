class Solution:
    def rec(self, i, nums, sum1, target, dp):
        if i>=len(nums):
            return False
        elif(sum1 > target):
            return False
        elif(sum1 == target):
            return True
        
        if dp[i][sum1] != -1:
            return dp[i][sum1]

        take = self.rec(i+1, nums, sum1+nums[i], target, dp)
        not_take = self.rec(i+1, nums, sum1, target, dp)

        dp[i][sum1] = take or not_take
        return dp[i][sum1]

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        n = len(nums)
        total = sum(nums)
        dp = [[-1 for j in range((total//2)+1)] for i in range(n)]

        return self.rec(0, nums, 0, total//2, dp)