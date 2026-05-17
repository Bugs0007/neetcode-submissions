class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Hash_Set = set(nums)
        ans = 0
        
        for num in Hash_Set:
            if num-1 not in Hash_Set:
                length = 1
                while num+length in Hash_Set:
                    length += 1
                ans = max(ans, length)
        return ans