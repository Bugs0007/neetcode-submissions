class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res = [-1, -1]
        reslen = float('inf')
        l = 0

        for i in range(len(s)):
            window[s[i]] = 1 + window.get(s[i], 0)

            if s[i] in countT and window[s[i]] == countT[s[i]]:
                have += 1

            while have == need:
                if i-l+1 < reslen:
                    res = [l,i]
                    reslen = i-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r+1] if reslen != float('inf') else ""