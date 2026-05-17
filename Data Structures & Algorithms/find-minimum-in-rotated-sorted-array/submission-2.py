class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1

        while i < j:
            mid = (i+j)//2
            val = nums[mid]

            if val > nums[j]:
                i = mid + 1
            else:
                j = mid

        return nums[i]
