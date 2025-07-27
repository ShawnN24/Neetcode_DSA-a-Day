class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack

        for c in s:
            if c == '(' or c == '{' or c == '[':
                print("APPENDED:",c)
                stack.append(c)
            elif c == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False