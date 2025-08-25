# Car Fleet

## Problem Statement
MEDIUM

There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

### Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1

Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

### Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3

Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

## My Solution Journey

Approach 1: Stack
The best approach is to have a stack to track pairs of position and speed. Iterating through the reverse sorted list of positions and removing any that catches up to another
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p = [] # pair: [pos, speed]

        for i, pos in enumerate(position):
            p.append([pos, speed[i]])
        p.sort(key=lambda x: x[0], reverse=True)
        print(p)

        timeStack = []
        for pos, speed in p:
            # speed * time + pos = target
            time = (target - pos) / speed
            timeStack.append(time)
            print("[",pos,", ",speed,"]:",time)
            if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()

        return len(timeStack)
```
Time & Space Complexity
- Time complexity: O(n log n)
- - We sorted the array so O(n log n)
- Space complexity: O(n)
- - We store up to the length of the array

## Time 
08/25/2025 | 0:44:20