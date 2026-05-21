class Solution:
    def lowerBound(self, nums, target):
        i, j = 0 ,len(nums)-1
        while i <= j:
            mid = (i+j)//2
            num = nums[mid]

            if num > target:
                j = mid - 1
            elif num < target:
                i = mid + 1
            else:
                return mid
        return i

    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []

        LIS.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                ind = self.lowerBound(LIS, nums[i])
                LIS[ind] = nums[i]
        print(LIS)
        return len(LIS)