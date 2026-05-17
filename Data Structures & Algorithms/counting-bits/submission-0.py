class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            num = i
            while num != 0:
                num = num & num-1
                count += 1
            ans.append(count)
        return ans