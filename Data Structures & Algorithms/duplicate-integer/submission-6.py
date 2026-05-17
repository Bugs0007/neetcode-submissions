class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set()

        for num in nums:
            st.add(num)

        return len(st) != len(nums)