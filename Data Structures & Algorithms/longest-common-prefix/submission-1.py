class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0

        s1 = strs[0]
        s2 = strs[-1]

        while i < len(s1) and i < len(s2):
            if s1[0:i+1] == s2[0:i+1]:
                i+=1
            else:
                break

        return s1[0:i]