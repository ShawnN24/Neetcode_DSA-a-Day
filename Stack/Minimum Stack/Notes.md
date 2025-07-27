# Minimum Stack

## Problem Statement
MEDIUM

Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

### Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

## My Solution Journey

Approach 1: Two Stack
My best approach is to have two stacks, one to track the current values at their positions in the stack, and one to track the given minimum at a certain position in the stack
```python
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
```
Time & Space Complexity
- Time complexity: O(1)
- - All operations operate in constant time
- Space complexity: O(n)
- - We store up to the O(2n) which simplifies to O(n)

Approach 2: One Stack
The best approach is to have one stacks to track the current values at their positions in the stack and a value to track the minimum
```python
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
```
Time & Space Complexity
- Time complexity: O(1)
- - All operations operate in constant time
- Space complexity: O(n)
- - We store up to the O(n)

## Time 
07/27/2025 | 0:25:44