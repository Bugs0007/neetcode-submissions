class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = nums[0]
        suff[len(nums)-1] = nums[len(nums)-1]

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]

        ans = []

        for i in range(len(nums)):
            if i == 0:
                ans.append(suff[i+1])
            elif i == len(nums)-1:
                ans.append(pref[i-1])
            else:
                prod = suff[i+1] * pref[i-1]
                ans.append(prod)
        return ans