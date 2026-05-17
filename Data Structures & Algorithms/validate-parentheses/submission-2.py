class Solution:
    def isValid(self, s: str) -> bool:
        c = list(s)
        st = []

        for ch in c:
            if ch in {'(','{','['}:
                st.append(ch)
            if ch == ')':
                if len(st) != 0 and st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif ch == '}':
                if len(st) != 0 and st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif ch == ']':
                if len(st) != 0 and st[-1] == '[':
                    st.pop()
                else:
                    return False
        if len(st) == 0:
            return True
        return False