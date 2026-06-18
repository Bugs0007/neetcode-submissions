class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        # nums.sort()
        st = set()

        for num in nums:
            st.add(num)

        for num in nums:
            length = 1
            while num+length in st:
                length += 1
            ans = max(ans, length)
        return ans