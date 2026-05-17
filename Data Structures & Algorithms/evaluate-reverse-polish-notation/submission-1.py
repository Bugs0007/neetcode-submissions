class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ans = 0
        for token in tokens:
            if token not in ['+','-','*','/']:
                stk.append(int(token))
            else:
                if token == '+':
                    ans = stk.pop() + stk.pop()
                elif token == '-':
                    ans = -(stk.pop()) + stk.pop()
                elif token == "*":
                    ans = stk.pop() * stk.pop()
                else:
                    div = stk.pop()
                    num = stk.pop()
                    ans = int(num/div)
                stk.append(ans)
        return stk.pop()