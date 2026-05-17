class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        s_arr = list(s)
        ans = 0
        start = 0

        for end in range(len(s)):
            while s_arr[end] in sub:
                sub.remove(s_arr[start])
                start += 1
            ans = max(ans, end-start+1)
            sub.add(s_arr[end])
        return ans