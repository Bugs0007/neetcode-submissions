class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s = sorted(s)
        s_t = sorted(t)

        return s_s == s_t