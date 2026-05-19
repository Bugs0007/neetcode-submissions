class Solution:
    def rec(self, s, i, j, dp):
        s1 = s[i:j]
        s2 = "".join(reversed(s1))

        if(i > j):
            return

        if (i, j) in dp:
            return dp[(i, j)]

        if(s1 == s2):
            dp[(i, j)] = s1
            return dp[(i, j)]
        
        ans1 = self.rec(s, i+1, j, dp)
        ans2 = self.rec(s, i, j-1, dp)

        if(len(ans1) > len(ans2)):
            dp[(i, j)] = ans1
        else:
            dp[(i, j)] = ans2

        return dp[(i, j)]


    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        return self.rec(s, 0, len(s), {})