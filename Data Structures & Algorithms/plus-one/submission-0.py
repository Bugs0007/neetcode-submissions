class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = 10*num + digits[i];

        ans = num+1

        return [int(x) for x in str(ans)]