class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stk_temp, stk_ind = stk.pop()
                result[stk_ind] = i - stk_ind
            stk.append([t, i])
        return result