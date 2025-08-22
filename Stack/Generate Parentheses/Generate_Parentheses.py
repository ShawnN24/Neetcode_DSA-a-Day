from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(opened, closed):
            # base case
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                backtrack(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()

        # start with 0 opened & 0 closed parenthesis
        backtrack(0, 0)
        
        return res