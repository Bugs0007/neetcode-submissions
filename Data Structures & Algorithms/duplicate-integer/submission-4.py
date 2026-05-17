class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_arr = set()

        for num in nums:
            set_arr.add(num)

        if len(set_arr) == len(nums):
            return False
        return True
        