from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif t == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif t == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            elif t == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(t))
            print(stack)

        return stack.pop()