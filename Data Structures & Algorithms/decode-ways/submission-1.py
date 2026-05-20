class Solution:
    def rec(self, i, j, s, dp):
        if j >= len(s):
            return 1
        
        if dp[i][j] != 0:
            return dp[i][j]
        n = s[i:j+1]
        num = int(n)

        if num > 26:
            self.rec(j, j, s, dp)
        elif num == 0:
            return 0
        else:
            dp[i][j] = self.rec(i, j+1, s, dp) + self.rec(j+1, j+1, s, dp)

        return dp[i][j]

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        if s[-1] == "0" and s[-2] not in ["1", "2"]:
            return 0
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        return self.rec(0,0,s,dp)//2