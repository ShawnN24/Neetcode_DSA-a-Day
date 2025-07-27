class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum.append(min(self.minimum[-1] if self.minimum else val, val))
        print("push_stack:",self.stack)
        print("push_min:",self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        print("pop_stack:",self.stack)
        print("pop_min:",self.minimum)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]