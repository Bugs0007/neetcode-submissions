class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        water = [0] * len(height)
        left_max = self.calc_leftmax(height)
        right_max = self.calc_rightmax(height)
        ans = 0

        for i in range(len(height)):
            water[i] = min(left_max[i], right_max[i]) - height[i]
            ans += water[i]

        print(left_max)
        print(right_max)
        print(water)

        return ans

    def calc_leftmax(self, height: List[int]) -> List[int]:
        left_max = [0] * len(height)
        curr_max = 0

        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            left_max[i] = curr_max
        
        return left_max

    def calc_rightmax(self, height: List[int]) -> List[int]:
        right_max = [0] * len(height)
        curr_max = 0

        for i in range(len(height)-1, -1, -1):
            curr_max = max(curr_max, height[i])
            right_max[i] = curr_max
        
        return right_max