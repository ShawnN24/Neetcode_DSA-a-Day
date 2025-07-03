# Top K Frequent Elements

## Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

### Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

### Example 2:

Input: nums = [7,7], k = 1

Output: [7]

## My Solution Journey

Approach 1: Sorting
Obvious first approach would be to sort the entire array. Then iterating backward through the array to find the top K elements
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```
Time & Space Complexity
- Time complexity: O(n log n)
- - We iterate in array n times for every n nums
- Space complexity: O(n)
- - We store the length of the array n

Approach 2: Hash Set
My best approach utilized hashmaps to store each numbers count and the list of numbers that reached a given k. This would allow us to iterate once through the array.
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # mapping {num: count}
        output = {} # mapping {count: list nums}
        topKIndex = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # increment nums count

            output[freq[num]] = output.get(freq[num], [])
            output[freq[num]].append(num) # add num to list that reach given count

            if len(output[freq[num]]) == k+1: # track the bottom to capture which numbers don't exist in topK
                topKIndex += 1
            
            print(output)
        print(freq)
        print(topKIndex)
        return output[topKIndex + 1]
```
Time & Space Complexity
- Let:
- - n = length of nums list
- Time complexity: O(n)
- - We iterate the length of the array O(n)
- Space complexity: O(n)
- - We store a list of n nums for the number of times they are counted. 
- - freq stores count of each unique number which worst case is O(n)
- - output maps counts to lists of numbers. In the worst case, if all numbers are unique, the number of keys in output is at most n leading to O(n)

## Time 
07/03/2025 | 0:44:51