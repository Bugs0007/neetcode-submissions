class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_arr = list(s)

        s1 = []
        s2 = []

        for ch in s_arr:
            if ch.isalnum():
                s1.append(ch.lower())
        
        for i in range(len(s_arr)-1, -1, -1):
            if s_arr[i].isalnum():
                s2.append(s_arr[i].lower())

        return s1 == s2

        