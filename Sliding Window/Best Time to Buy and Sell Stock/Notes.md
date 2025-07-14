# Best Time to Buy and Sell Stock

## Problem Statement
EASY

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

### Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

### Explanation

Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

### Example 2:

Input: prices = [10,8,7,5,2]

Output: 0

### Explanation

No profitable transactions can be made, thus the max profit is 0.

## My Solution Journey

Approach 1: Brute Force-
The obvious first approach is to brute force by iterating through the array a whole time for every number to calcualte the max return of each.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
```
Time & Space Complexity
- Time complexity: O(n^2)
- - We only loop through the array a whole time for every number
- Space complexity: O(1)
- - Constant time

Approach 2: Two Pointers
The best approach is to have two pointers, one to track the current buyDay and its associated sellDay we slide until we find a smaller buyDay or the end of the list. Calculating the output profit all the while.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        buyDay = 0
        sellDay = 0
        
        for i in range(len(prices)):
            if prices[i] < prices[buyDay]:
                buyDay = i
                sellDay = buyDay
            if prices[i] == max(prices[sellDay], prices[i]):
                    sellDay = i
            output = max(output, prices[sellDay] - prices[buyDay])

        return output
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the array once
- Space complexity: O(1)
- - Constant time

## Time 
07/13/2025 | 0:23:33