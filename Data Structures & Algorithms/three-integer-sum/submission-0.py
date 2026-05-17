class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            for j in range(i+1, len(nums)):
                req = -(nums[i] + nums[j])
                for k in range(len(nums)-1, j, -1):
                    if nums[k] == req:
                        ls = [nums[i], nums[j], nums[k]]
                        if ls not in res:
                            res.append(ls)
        return res