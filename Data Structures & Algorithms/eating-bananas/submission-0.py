class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r_low = 1
        r_high = max(piles)
        r_ans = float('inf')

        while r_low <= r_high:
            r_mid = (r_low + r_high)//2
            t = self.timetoeat(piles, r_mid)

            if t > h:
                r_low = r_mid+1
            else:
                r_ans = r_mid
                r_high = r_mid-1
        return r_ans

    def timetoeat(self, piles: List[int], r: int) -> int:
        time = 0
        for pile in piles:
            t1 = pile//r
            t2 = 1 if pile%r != 0 else 0

            time += t1 + t2

        return time