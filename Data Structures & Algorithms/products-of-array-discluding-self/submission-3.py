class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        pref[0] = nums[0]

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i]

        suff = [1] * len(nums)
        suff[len(nums)-1] = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]

        res = [0] * len(nums)
        res[0] = suff[1]
        res[len(nums)-1] = pref[len(nums)-2]
        
        for i in range(1, len(nums)-1):
            res[i] = pref[i-1] * suff[i+1]

        return res