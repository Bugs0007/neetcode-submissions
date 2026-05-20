class Solution:
    def pal(self, i, j, s):
        ans = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            ans += 1
            i -= 1
            j += 1
        return ans


    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            even = self.pal(i,i+1,s)
            odd = self.pal(i,i,s)
            ans += even+odd
        return ans