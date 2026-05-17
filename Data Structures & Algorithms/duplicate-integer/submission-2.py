class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr_sorted = sorted(nums)

        for i in range(len(nums)-1):
            if arr_sorted[i] == arr_sorted[i+1]:
                return True
        return False
        