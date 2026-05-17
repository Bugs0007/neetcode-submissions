class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        for s in strs:
            ana = sorted(s)
            new_ana = True

            for anas in ans:
                if sorted(anas[0]) == ana:
                    anas.append(s)
                    new_ana = False
            
            if new_ana:
                new_l = []
                new_l.append(s)
                ans.append(new_l)
        return ans
        