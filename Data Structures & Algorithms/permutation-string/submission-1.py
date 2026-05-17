class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s = sorted(s1)

        for i in range(len(s2)-n+1):
            curr = s2[i:i+n]
            if sorted(curr) == s:
                return True

        return False