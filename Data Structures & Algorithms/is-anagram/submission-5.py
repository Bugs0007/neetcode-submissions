class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)

        t_arr = sorted(t_arr)
        s_arr = sorted(s_arr)

        return(t_arr == s_arr)