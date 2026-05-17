class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            mid = (i+j)//2
            m = nums[mid]

            if target > m:
                i = mid + 1
            elif target < m:
                j = mid - 1
            else:
                return mid
        return -1