class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += '´' + s + '˳'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if s[i] == '´':
                start = i+1
                end = start
                word = ""
                while s[end] != '˳':
                    end += 1
                word = s[start:end]
                res.append(word)
        return res