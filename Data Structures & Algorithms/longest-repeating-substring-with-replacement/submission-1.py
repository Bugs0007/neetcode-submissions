class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_set = set()
        for ch in s:
            hash_set.add(ch)

        ans = 0
        for ch in hash_set:
            ch_count = 0
            l = 0
            for i in range(len(s)):
                if s[i] == ch:
                    ch_count += 1
                while i-l+1 - ch_count > k:
                    if s[l] == ch:
                        ch_count -= 1
                    l += 1
                ans = max(ans, i-l+1)
                # else:
                #     ans = max(ans, i-1+1)
        return ans